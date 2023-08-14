# Google reCAPTCHA solver in python, using OpenAI Whisper API.

This is a Python script that uses Selenium and OpenAI Whisper API to solve Google reCAPTCHA.

## Prerequisites

- Python version 3.8 or higher (3.10 recommended)
- pip, a package manager for Python

## Virtual Environment

To create and activate a virtual environment for this project, you can use the following commands:

Windows:
`py -m venv myworld`
`myworld\Scripts\activate.bat`

Unix/MacOS:
`python -m venv myworld`
`source myworld/bin/activate`

## Installation

You can install the packages using pip:

`pip install -r requirements.txt`

## Usage

To run the script, simply execute:

`python recaptcha_solver.py`

The script will solve the reCAPTCHA challenge in the browser. You can modify the script to use it for other websites that have reCAPTCHA.