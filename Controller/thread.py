from PyQt5.QtCore import  QThread
from pyqtspinner.spinner import WaitingSpinner


class Thread(QThread):

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self.is_running = True
        self.spinner = WaitingSpinner(parent, roundness=70.0, opacity=15.0,
                                 fade=70.0, radius=10.0, lines=12,
                                 line_length=10.0, line_width=5.0,
                                 speed=1.0, color=(0, 0, 0))

    def run(self):
        self.spinner.start()

    def stop(self):
        self.spinner.stop()
        self.is_running = False
        self.terminate()