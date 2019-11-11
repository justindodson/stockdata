from PyQt5 import QtWidgets


def show_connection_dialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)

    msg.setText('No Network Connect')
    msg.setInformativeText('The network is taking too long to load. Please try again later.')
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()

def show_scrape_error_dialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)

    msg.setText('Data Not Gathered')
    msg.setInformativeText('The page took too long to load and was unable to retrieve the Call Data.')
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()