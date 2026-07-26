import sys

from PySide6.QtWidgets import QApplication, QWidget  # type: ignore[import-from-not-recorded]

from ui_form import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self, parent: QWidget | None=None):
        super().__init__(parent)
        self.setupUi(self)  # type: ignore[uic-did-not-do-annotations]
        self.sendButton.clicked.connect(self.send)

    def send(self):
        ...


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()
            
