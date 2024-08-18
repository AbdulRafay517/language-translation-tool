# Language Translation Tool

## Overview

The Language Translation Tool is a Python application that provides text and voice-based translation capabilities. This tool uses the `deep-translator` library for text translation and the `speech_recognition` library for converting spoken words into text. It features a modern, dark mode user interface built with Tkinter.

## Features

- **Text Translation**: Translate text from one language to another using Google Translator API.
- **Voice Input**: Convert spoken words into text and translate them.
- **Modern Dark Mode UI**: A stylish, dark-themed interface for a clean and fluent user experience.

## Requirements

- Python 3.x
- Libraries:
  - `deep-translator`
  - `pyttsx3`
  - `speech_recognition`
  - `pyaudio` (for microphone input)
  - `tkinter` (for GUI)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/language-translation-tool.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd language-translation-tool
   ```

3. **Create a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Libraries:**

   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:

   ```
   deep-translator
   pyttsx3
   speech_recognition
   pyaudio
   ```

## Usage

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Text Translation:**
   - Enter the text you want to translate.
   - Select the source and target languages.
   - Click the "Translate" button to get the translated text.

3. **Voice Input:**
   - Click the "Listen & Translate" button.
   - Speak into the microphone.
   - The application will convert your speech to text and then translate it.

## Code Structure

- `main.py`: The main application file containing the GUI and functionality.
- `requirements.txt`: List of required Python packages.

## Contributing

1. **Fork the Repository**: Create your own fork of the repository on GitHub.
2. **Clone Your Fork**: Clone your fork to your local machine.
3. **Create a Branch**: Create a new branch for your changes.
4. **Make Changes**: Implement your changes and test thoroughly.
5. **Push Changes**: Push your changes to your fork.
6. **Create a Pull Request**: Submit a pull request to the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [Abdul Rafay](mailto:abdulrafay517@hotmail.com).
