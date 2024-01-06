# Personal Assistant with Python

This is a simple personal assistant program built in Python that performs various tasks using speech recognition and text-to-speech conversion.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/sudpmishra/PersonalAIAssistant
    cd PersonalAIAssistant
    ```

2. **Install Dependencies:**
    - Make sure you have Python 3 installed.
    - Install required Python libraries using pip:
        ```bash
        pip install pyttsx3 openai==0.11.2 speech_recognition python-dotenv
        ```

3. **API Keys Setup:**
    - You'll need to set up your OpenAI API key. Rename the `.env.example` file to `.env` and replace `YOUR_OPENAI_API_KEY` with your actual API key.

## Usage

1. Run the program:
    ```bash
    python assistant.py
    ```
   
2. The assistant will start and listen for your commands.
   
3. Speak clearly and wait for the assistant to respond. You can ask for the current time, request information, or perform specific tasks based on the program's capabilities.

## Supported Commands

- **Time**: Ask for the current time.
- **Information Retrieval**: Ask for information on a topic.
- **Custom Tasks**: Extend the assistant's functionality by adding custom tasks within the `assistant.py` file.

## Contributing

Contributions are welcome! If you'd like to add features, improve existing functionalities, or fix issues, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
