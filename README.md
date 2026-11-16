Smart Environment Monitoring

A Python application that simulates environmental sensors to monitor temperature, humidity, and air quality. It generates sensor readings, stores them in a local SQLite database, and retrieves the collected data for display.

Why I Built This

I built this project to practice Python programming through a practical, real-world inspired application. Environmental monitoring involves collecting and organizing data from different sensors. This project simulates that process and helped me understand object-oriented programming, database management, and how to structure a Python application using separate modules.

Core Features

Sensor Simulation: Generates simulated temperature, humidity, and air-quality readings from multiple sensors.

Multiple Locations: Simulates sensors placed in different environments, including the living room, bedroom, and kitchen.

SQLite Database: Automatically creates a database and stores sensor readings for future retrieval.

Data Retrieval: Retrieves previously stored measurements using SQL queries.

Readable Output: Displays collected sensor data in a structured table directly in the terminal.

Tech Stack

Programming Language: Python

Database: SQLite (sqlite3)

Object-Oriented Programming: Python classes and objects

Data Generation: random

Date and Time: datetime

Version Control: Git and GitHub

Getting Started

Prerequisites

Python 3.9+ installed on your system.

Git installed on your system.

Installation & Setup

Clone the repository:

git clone https://github.com/kounout/ai-document-summarizer.git

Create a virtual environment:

python3 -m venv .venv

Activate the virtual environment:

On macOS/Linux:

source .venv/bin/activate

On Windows:

.venv\Scripts\activate

Run the application:

python3 simulator.py
