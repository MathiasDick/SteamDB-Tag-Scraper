import sys
import logging
from PySide6 import QtWidgets as qtw
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from UI.main_window import Ui_w_game_scraper
from PySide6.QtCore import QThread, Signal

# Set up logging to track errors and info
logging.basicConfig(level=logging.INFO)


class ScraperThread(QThread):
    # Signal to communicate with the main thread when scraping is done
    update_signal = Signal(pd.Series)

    def __init__(self, rb_trending, rb_most_played, rb_popular_releases, rb_hot_releases):
        super().__init__()
        self.rb_trending = rb_trending
        self.rb_most_played = rb_most_played
        self.rb_popular_releases = rb_popular_releases
        self.rb_hot_releases = rb_hot_releases

    def run(self):
        # Scraping logic executed in the background
        all_tags = []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Use the 'with' statement to ensure the driver is closed properly
        with webdriver.Chrome(options=chrome_options) as driver:
            driver.get("https://steamdb.info")
            wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds

            # Define the radio button options and corresponding categories
            radio_buttons = {
                self.rb_trending: "Trending",
                self.rb_most_played: "Most",
                self.rb_popular_releases: "Popular",
                self.rb_hot_releases: "Hot"
            }

            selected_text = next((text for rb, text in radio_buttons.items() if rb.isChecked()), "")

            # Find the table that corresponds to the selected category
            tables = driver.find_elements(By.CSS_SELECTOR, value="table.table-products")
            table = None
            for n in tables:
                if selected_text in n.text:
                    table = n
                    break  # Exit once the correct table is found

            if not table:
                logging.error("No table found for the selected category.")
                self.update_signal.emit(pd.Series())  # Emit empty series if no table found
                return

            logging.info(f"Found table: {table.text}")

            # Scrape tags for each game in the table
            games = table.find_elements(By.CSS_SELECTOR, value="td.applogo")
            for game in games:
                actions = ActionChains(driver)
                actions.move_to_element(game).perform()

                try:
                    tags = wait.until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.hover_tag_row a"))
                    )
                except Exception as e:
                    logging.error(f"Error finding tags: {e}")
                    continue

                tag_list = [tag.text for tag in tags if tag.text]
                logging.info(f"Tags: {tag_list}")
                all_tags.extend(tag_list)

            # Count tag occurrences
            tag_counts = pd.Series(all_tags).value_counts()

        # Emit the signal with the tag counts
        self.update_signal.emit(tag_counts)


class MainWindow(qtw.QWidget, Ui_w_game_scraper):
    def __init__(self):
        super().__init__()
        self.scraper_thread = None
        self.setupUi(self)
        # Connect the start button to the scraper thread
        self.pb_start.clicked.connect(self.start_scraper)

    def start_scraper(self):
        # Clear the table before starting the scraper
        self.tw_tags.clear()

        # Create the scraper thread and connect the update signal to update the UI
        self.scraper_thread = ScraperThread(self.rb_trending_games, self.rb_most_played_games,
                                            self.rb_popular_releases, self.rb_hot_releases)
        self.scraper_thread.update_signal.connect(self.on_scraping_complete)

        # Start the scraper in the background thread
        self.scraper_thread.start()

    def on_scraping_complete(self, tag_counts):
        # This method will be called when scraping is complete
        if not tag_counts.empty:
            logging.info("Scraping completed.")
            self.populate_table(tag_counts)
        else:
            logging.error("No tag data available to display.")

    def populate_table(self, tag_counts):
        # Set the number of rows and columns for the table
        self.tw_tags.setRowCount(len(tag_counts))
        self.tw_tags.setColumnCount(2)

        # Set the table headers
        self.tw_tags.setHorizontalHeaderLabels(["Tag", "Count"])

        # Insert the data into the table
        for row, (tag, count) in enumerate(tag_counts.items()):
            self.tw_tags.setItem(row, 0, qtw.QTableWidgetItem(tag))  # Tag
            self.tw_tags.setItem(row, 1, qtw.QTableWidgetItem(str(count)))  # Count

        # Adjust the column sizes to fit the content
        self.tw_tags.resizeColumnsToContents()
        self.tw_tags.resizeRowsToContents()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
