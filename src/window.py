from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QHeaderView, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setup()

    def setup(self):
        self.setWindowTitle('Nationalize API Client')

        _layout = QVBoxLayout(self)

        _textfield = QLineEdit()
        _textfield.setPlaceholderText('Enter a name to search for matches.')
        _textfield.setMinimumHeight(40)
        _textfield.setMaximumHeight(40)
        _layout.addWidget(_textfield)

        _button_layout = QHBoxLayout()
        _button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        _search_button = QPushButton('Search')
        _search_button.setMinimumSize(200, 40)
        _search_button.setMaximumHeight(40)
        _button_layout.addWidget(_search_button)

        _button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        _layout.addLayout(_button_layout)

        _results_table = QTableWidget()
        _results_table.setColumnCount(2)
        _results_table.setHorizontalHeaderLabels(['Country', 'Probability'])
        _results_table.verticalHeader().hide()
        _results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        _layout.addWidget(_results_table)

        self.setLayout(_layout)
        self.setMinimumSize(640, 480)