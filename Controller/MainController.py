from View.MainWindow import Ui_MainWindow
from Controller.helpers import convert_time_to_utc
from Model.helpers import search_for_stock_ticker
import sys
from PyQt5 import QtWidgets


class MainControllerEXEC:

    def __init__(self):
        # Create Application Instance
        app = QtWidgets.QApplication(sys.argv)

        # Create new MainWindow Instance
        MainWindow = QtWidgets.QMainWindow()

        # Create a ui instance to reference from the View
        # and pass in the MainWindow as an argument to update the
        # main window remotely
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        # call functions to process events
        self.trigger_seach_button()
        self.trigger_date_change()
        self.trigger_search_bar_used()
        self.trigger_recent_stock_selection()


        # Show MainWindow and execute application
        MainWindow.show()
        sys.exit(app.exec_())

    def update_recent_stock_list(self):
        """ This method will search the database
            during the application initialization
            to update the recent stock list with
            only unique stocks from the last 7
            days
        """
        pass

    def trigger_date_change(self):
        pass

    def trigger_search_bar_used(self):
        self.ui.stockSearchBar.textChanged.connect(self.update_recent_combobox)

    def update_recent_combobox(self):
        if self.ui.stockSearchBar.text() != '':
            self.ui.recentStocksList.setDisabled(True)
        else:
            self.ui.recentStocksList.setDisabled(False)

    def trigger_recent_stock_selection(self):
        self.ui.recentStocksList.currentTextChanged.connect(self.update_search_bar)

    def update_search_bar(self):
        if self.ui.recentStocksList.currentText() != 'Select Recent':
            self.ui.stockSearchBar.setDisabled(True)
            self.ui.searchButton.setDisabled(True)
        #     TODO: Create auto search method to populate date list
        else:
            self.ui.stockSearchBar.setDisabled(False)
            self.ui.searchButton.setDisabled(False)

    def trigger_seach_button(self):
        self.ui.searchButton.clicked.connect(self.perform_search)

    def perform_search(self):
        search_value = self.ui.stockSearchBar.text().upper()
        if search_value != '':
            result = search_for_stock_ticker(search_value)
            if result is not None:
                self.ui.stockSearchResult.setText(result[1])
                self.ui.stockSearchResult.repaint()
            else:
                self.ui.stockSearchResult.setText('No Stock found with symbol \'{}\''.format(search_value))
                self.ui.stockSearchResult.repaint()
        else:
            self.ui.stockSearchResult.setText("Enter Valid Symbol")
            self.ui.stockSearchResult.repaint()

    def search_for_stock_symbol(self, symbol):
        pass

    def date_selected(self):
        convert_time_to_utc(self.ui.dateSelect.date().toString('yyyy MM dd'))


if __name__ == '__main__':
    mw = MainControllerEXEC()