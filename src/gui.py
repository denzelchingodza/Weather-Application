# gui.py
# PURPOSE:
# - Defines the main GUI window.
# - Handles layout, buttons, input fields, and displays weather results.
# - Connects UI → weather_api.get_weather() → updates to screen.

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

import weather_api
import utils
import os

class WeatherWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App (Starter Version)")
        self.setMinimumWidth(400)

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()

        # --- Search Bar ---
        search_layout = QHBoxLayout()

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter a city name")

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.fetch_weather)

        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.search_button)

        layout.addLayout(search_layout)

        # --- Weather Output Labels ---
        self.status_label = QLabel("Enter a city and press Search")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.temp_label = QLabel("")
        self.temp_label.setAlignment(Qt.AlignCenter)

        self.desc_label = QLabel("")
        self.desc_label.setAlignment(Qt.AlignCenter)

        # Weather icon
        self.icon_label = QLabel("")
        self.icon_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.status_label)
        layout.addWidget(self.temp_label)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.icon_label)

        self.setLayout(layout)

    def fetch_weather(self):
        city = self.city_input.text().strip()

        if not city:
            self.status_label.setText("Please enter a city name.")
            return

        data = weather_api.get_weather(city)

        if data is None:
            self.status_label.setText("City not found or API error.")
            self.temp_label.setText("")
            self.desc_label.setText("")
            self.icon_label.clear()
            return

        # Update labels
        self.status_label.setText(f"Weather for {city}")
        self.temp_label.setText(f"{data['temp']}°C")
        self.desc_label.setText(data["description"].title())

        # Load weather icon
        icon_path = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "icons",
            f"{data['icon']}.png"
        )

        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path).scaled(100, 100, Qt.KeepAspectRatio)
            self.icon_label.setPixmap(pixmap)
        else:
            self.icon_label.setText("Icon missing")

