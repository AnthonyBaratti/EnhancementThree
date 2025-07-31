"""
Created 7/27/2025
Animal Shelter Dashboard
main.py

Author: Anthony Baratti
Southern New Hampshire University
CS-499 Computer Science Capstone
Artifact Enhancement #3
Conversion from MongoDB to SQLite3

Purpose: Single entry point for packaged application.
Imports ShelterDashboard.py
"""

from ShelterDashboard import app
import webbrowser
import threading

if __name__ == "__main__":
    # Automatically open the browser after server starts
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:8050/")

    # Launch browser in a separate thread to avoid blocking
    threading.Timer(1.0, open_browser).start()
    app.run(debug=False)