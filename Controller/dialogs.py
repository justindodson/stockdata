from PyQt5 import QtWidgets


def show_connection_dialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)

    msg.setText('No Network Connection')
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

def confirm_save_dialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)

    msg.setText('Are you sure?')
    msg.setInformativeText('This stock symbol will be saved into your recent search list for 7 days.\n')
    msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)

    response = msg.exec_()
    if response == QtWidgets.QMessageBox.Cancel:
        return 0
    elif response == QtWidgets.QMessageBox.Ok:
        return 1
    else:
        return 0

def confirm_delete_dialog(self):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Warning)

    msg.setText('Are you sure?')
    msg.setInformativeText('Are you sure you want to delete this row?')
    msg.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)

    response = msg.exec_()
    if response == QtWidgets.QMessageBox.Cancel:
        return 0
    elif response == QtWidgets.QMessageBox.Ok:
        return 1
    else:
        return 0
