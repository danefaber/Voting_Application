from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QGridLayout, QFrame
from PyQt6.QtCore import Qt
import logic


class VotingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        grid_format = QGridLayout()
        frame = QFrame(self)
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Plain)
        frame.setLineWidth(2)
        frame.setMidLineWidth(2)
        frame.setStyleSheet("border: 6px solid blue;")
        frame.setGeometry(0, 0, 300, 200)
        '''The code above this creates a frame around the window'''

        self.label_vote = QLabel("VOTE!")
        self.label_vote.setFixedHeight(50)
        main_layout.addWidget(self.label_vote, alignment=Qt.AlignmentFlag.AlignTop)
        self.label_vote.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_ID = QLabel("Voter ID:")
        self.input_ID = QLineEdit()
        self.input_ID.setAlignment(Qt.AlignmentFlag.AlignRight)
        grid_format.addWidget(self.label_ID, 1, 0)
        grid_format.addWidget(self.input_ID, 1, 1, 1, 2)

        self.label_Candidates = QLabel("Candidates:")
        self.radio_Smith = QRadioButton("John Smith")
        self.radio_Doe = QRadioButton("Jane Doe")
        grid_format.addWidget(self.label_Candidates, 2, 0)
        grid_format.addWidget(self.radio_Smith, 2, 1)
        grid_format.addWidget(self.radio_Doe, 2, 2)

        self.button_submit = QPushButton("SUBMIT")
        grid_format.addWidget(self.button_submit, 3, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_submit.clicked.connect(self.handle_submit)

        counts = logic.count_votes()
        self.label_votes_smith = QLabel(f"John Smith: {counts.get('John Smith', 0)} votes")
        self.label_votes_doe = QLabel(f"Jane Doe: {counts.get('Jane Doe', 0)} votes")
        grid_format.addWidget(self.label_votes_smith, 4, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        grid_format.addWidget(self.label_votes_doe, 5, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignCenter)


        main_layout.addLayout(grid_format)
        self.setLayout(main_layout)

    def handle_submit(self):
        '''This function ensures data is entered correctly and submits
        the vote to the logic function.'''
        user_id = self.input_ID.text().strip()
        if not user_id:
            self.label_vote.setText("Error: Voter ID cannot be empty.")
            self.label_vote.setStyleSheet("color: red;")
            return
        if len(user_id) != 4:
            self.label_vote.setText("Error: Voter ID must be 4 numbers.")
            self.label_vote.setStyleSheet("color: red;")
            return
        if not user_id.isdigit():
            self.label_vote.setText("Error: Voter ID must contain only numbers.")
            self.label_vote.setStyleSheet("color: red;")
            return


        candidate_name = None
        if self.radio_Smith.isChecked():
            candidate_name = "John Smith"
        elif self.radio_Doe.isChecked():
            candidate_name = "Jane Doe"
        else:
            self.label_vote.setText("Error: Please select a candidate.")
            self.label_vote.setStyleSheet("color: red;")
            return

        try:
            logic.store_vote(user_id, candidate_name)
            self.label_vote.setText("Vote Submitted Successfully!")
            self.label_vote.setStyleSheet("color: green;")
            self.update_vote_tally()
        except ValueError as e:
            self.label_vote.setText(str(e))

        self.input_ID.clear()
        self.radio_Smith.setChecked(False)
        self.radio_Doe.setChecked(False)


    def update_vote_tally(self):
        '''Updates the live vote count on the gui'''
        counts = logic.count_votes()
        self.label_votes_smith.setText(f"John Smith: {counts.get('John Smith', 0)} votes")
        self.label_votes_doe.setText(f"Jane Doe: {counts.get('Jane Doe', 0)} votes")



