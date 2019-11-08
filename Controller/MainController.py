from Controller.helpers import convert_time_to_utc
from Controller.dialogs import show_connection_dialgo, show_scrape_error_dialog
from Model.helpers import search_for_stock_ticker
from Utils.web_scraper import StockData
from View.MainWindow import Ui_MainWindow

import sys
from PyQt5 import QtWidgets


class MainControllerEXEC:

    def __init__(self):
        # Create Application Instance
        app = QtWidgets.QApplication(sys.argv)

        # Create new main_window Instance
        main_window = QtWidgets.QMainWindow()

        # Create a ui instance to reference from the View
        # and pass in the main_window as an argument to update the
        # main window remotely
        self.ui = Ui_MainWindow()
        self.ui.setupUi(main_window)

        self.date_dict = {}

        # call functions to process events
        self.trigger_date_change()
        self.trigger_search_bar_used()
        self.trigger_recent_stock_selection()
        self.trigger_search_button()
        self.trigger_import_date()

        # Show main_window and execute application
        main_window.show()
        sys.exit(app.exec_())

    """
        -- Signal methods --
    """

    def trigger_date_change(self):
        pass

    def trigger_search_bar_used(self):
        self.ui.stockSearchBar.textChanged.connect(self.update_recent_combobox)

    def trigger_recent_stock_selection(self):
        self.ui.recentStocksList.currentTextChanged.connect(self.update_search_bar)

    def trigger_search_button(self):
        self.ui.searchButton.clicked.connect(self.perform_search)

    def trigger_import_date(self):
        self.ui.importButton.clicked.connect(self.scrape_stock_data)

    """
        -- Class Methods --
    """

    def update_recent_stock_list(self):
        """ This method will search the database
            during the application initialization
            to update the recent stock list with
            only unique stocks from the last 7
            days
        """
        pass

    def update_recent_combobox(self):
        if self.ui.stockSearchBar.text() != '':
            self.ui.recentStocksList.setDisabled(True)
        else:
            self.ui.recentStocksList.setDisabled(False)

    def update_search_bar(self):
        if self.ui.recentStocksList.currentText() != 'Select Recent':
            self.ui.stockSearchBar.setDisabled(True)
            self.ui.searchButton.setDisabled(True)
        else:
            self.ui.stockSearchBar.setDisabled(False)
            self.ui.searchButton.setDisabled(False)

    def perform_search(self):
        self.ui.dateSelect.clear()
        self.date_dict.clear()
        search_value = self.ui.stockSearchBar.text().upper()
        if search_value != '':
            result = search_for_stock_ticker(search_value)
            if result is not None:
                self.ui.stockSearchResult.setText(result[1])
                self.ui.stockSearchResult.repaint()
                self.load_date_picker(search_value)
            else:
                self.ui.stockSearchResult.setText('No Stock found with symbol \'{}\''.format(search_value))
                self.ui.stockSearchResult.repaint()
        else:
            self.ui.stockSearchResult.setText("Enter Valid Symbol")
            self.ui.stockSearchResult.repaint()

    def date_selected(self):
        convert_time_to_utc(self.ui.dateSelect.date().toString('yyyy MM dd'))

    def load_date_picker(self, stock_symbol):
        stock = StockData(stock_symbol)
        self.date_dict = stock.get_date_options()

        if self.date_dict is not None:
            for date in self.date_dict:
                self.ui.dateSelect.addItem(date)
                self.ui.dateSelect.repaint()
        else:
            show_connection_dialgo(self)

    def scrape_stock_data(self):
        date = self.date_dict[self.ui.dateSelect.currentText()]
        stock = StockData(self.ui.stockSearchBar.text().upper())
        stock_data = stock.get_call_data(date)
        if stock_data is not None:
            self.populate_data_table(stock_data)
        else:
            print('Issues HERE')

    def populate_data_table(self, stock_data):
        row_number = self.ui.stockTable.rowCount()
        self.ui.stockTable.insertRow(row_number)

        for i in range(len(stock_data)):
            self.ui.stockTable.setItem(row_number, i, QtWidgets.QTableWidgetItem(stock_data[i]))
            self.ui.stockTable.repaint()

        self.ui.stockTable.setItem(row_number, 4, QtWidgets.QTableWidgetItem(self.ui.dateSelect.currentText()))

        self.ui.stockTable.repaint()

