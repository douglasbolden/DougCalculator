import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QTimer, QTime, Qt


class ClockDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(375, 75)

        layout = QVBoxLayout()

        fnt = QFont("SansSerif", 40, QFont.Weight.DemiBold)

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl.setFont(fnt)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        clock_time = QTimer(self)
        clock_time.timeout.connect(self.displayCurrentTime)
        clock_time.start(500)

    def displayCurrentTime(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('h:mm:ss A')
        print(display_text)

        self.lbl.setText(display_text)


app = QApplication(sys.argv)
app.setApplicationName("Clock Demo by Douglas Bolden")
app.setWindowIcon(QIcon('images/DougTime.png'))

clock = ClockDemo()
clock.show()

app.exit(app.exec())
