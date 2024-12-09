import sys
from PyQt6.QtWidgets import QApplication
from gui import VotingApp

def start_app():
    app_instance = QApplication(sys.argv)
    main_window = VotingApp()
    main_window.show()
    main_window.setWindowTitle("Voting App")
    main_window.setFixedSize(300, 200)
    sys.exit(app_instance.exec())


if __name__ == '__main__':
    start_app()