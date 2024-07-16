# Summarization_Project

Text Summarization Project

Overview

This project is a Python-based text summarization tool that uses the Ollama.ai API to summarize text files. The tool takes a text file as input, sends the text to the Ollama.ai API, and retrieves a summarized version of the text.

Features
-> Summarize text files using the Ollama.ai API
-> Supports text files in various formats (e.g.,.txt,.docx,.pdf)
-> Easy to use command-line interface

Requirements
-> Python 3.6 or later
-> Ollama.ai API key (obtain from Ollama.ai website)
-> requests library (install using pip install requests)

Usage
-> Create a new text file (e.g., book.txt) and add the text you want to summarize.
-> Open a terminal or command prompt and navigate to the directory where your text file is located.
-> Run the following command to summarize the text file:
    python summarize.py -f book.txt
-> The tool will send the text to the Ollama.ai API and retrieve a summarized version of the text.
-> The summarized text will be displayed in the terminal or command prompt.

Configuration
-> Create a new file named config.json in the same directory as the summarize.py script.
-> Add your Ollama.ai API key to the config.json 

Troubleshooting
-> If you encounter a DNS resolution issue, try checking your internet connection, DNS settings, and firewall or antivirus software.
-> If you encounter an API error, try checking the Ollama.ai API documentation and ensuring that your API key is correct.

Contributing
-> Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

Acknowledgments
-> This project uses the Ollama.ai API for text summarization. Thank you to the Ollama.ai team for providing this API.
