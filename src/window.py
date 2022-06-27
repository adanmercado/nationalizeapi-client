from itertools import count
from urllib import response
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem,
    QSizePolicy, QMessageBox
)
from PySide6.QtCore import Qt

import requests, json

API_URL = 'https://api.nationalize.io/'

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setup()

    def setup(self):
        self.setWindowTitle('Nationalize API Client')

        layout = QVBoxLayout(self)

        self.textfield = QLineEdit()
        self.textfield.setPlaceholderText('Enter a name to search for matches.')
        self.textfield.setMinimumHeight(40)
        self.textfield.setMaximumHeight(40)
        layout.addWidget(self.textfield)

        button_layout = QHBoxLayout()
        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        search_button = QPushButton('Search')
        search_button.setMinimumSize(200, 40)
        search_button.setMaximumHeight(40)
        search_button.clicked.connect(self.search)
        button_layout.addWidget(search_button)

        button_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(button_layout)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)
        self.results_table.setHorizontalHeaderLabels(['Country', 'Probability'])
        self.results_table.verticalHeader().hide()
        self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.results_table)

        self.setLayout(layout)
        self.setMinimumSize(640, 480)

    def search(self):
        self.results_table.clearContents()
        self.results_table.setRowCount(0)
        search_text = self.textfield.text().strip()
        if not search_text:
            QMessageBox.critical(self, 'Error', 'Enter a name to search for matches.', QMessageBox.Ok)
            return

        countries = self.search_name(search_text)
        if not countries:
            QMessageBox.information(self, 'Search finished', 'No matches found for the name.')
            return

        for country in countries:
            row = self.results_table.rowCount()
            self.results_table.insertRow(row)
            self.results_table.setItem(row, 0, QTableWidgetItem(country['country_id']))
            self.results_table.setItem(row, 1, QTableWidgetItem(str(country['probability'])))

    def search_name(self, name: str) -> list:
        countries = []
        if not name:
            return countries

        try:
            response = requests.get(API_URL, params={'name': name})
            if response.status_code == 200:
                data = json.loads(response.text)
                if data:
                    countries = data['country']
            return countries
        except:
            print('An error ocurred.')
            return countries