# 52 Days of Python: Flask Number Guessing Game

This repository is a part of my 52-day journey into learning Python programming. Here, I'm experimenting with various concepts like decorator functions and Flask framework.

## Introduction

This code implements a simple number guessing game using Flask, a lightweight WSGI web application framework in Python. The game generates a random number between 0 and 9, and the user tries to guess it by entering a number through the URL.

## How to Play

1. Clone the repository or download the code files.
2. Make sure you have Python and Flask installed.
3. Run the Python script (`main.py`).
4. Open your web browser and go to `http://localhost:5000/`.
5. You'll see an interface prompting you to guess a number between 0 and 9.
6. Enter a number in the URL after the slash (`/`). For example, `http://localhost:5000/3`.
7. Based on your guess, the application will respond with messages indicating if your guess is too high, too low, or correct.
8. Keep guessing until you get the correct number!

## Additional Information

- The random number is generated when the server starts.
- The game interface provides feedback using HTML messages and GIF images to make the experience more interactive and enjoyable.


## Running the Application

You can run the Flask application by executing the `main.py` script. Make sure you have Flask installed. Use the following command to run the application:

```bash
python main.py
