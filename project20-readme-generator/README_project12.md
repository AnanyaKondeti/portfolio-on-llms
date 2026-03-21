# 🤖 Multi-Turn Chatbot with Memory
======================

## What it does
---------------

This project implements a career coach chatbot that leverages memory to keep track of conversation history. The chatbot utilizes natural language processing (NLP) to provide context-aware responses, taking into account the conversation flow, user input, and persona prompts.

## Key Features
----------------

*   **Conversation Memory**: The chatbot retains conversation history to provide relevant and personalized responses.
*   **Context Awareness**: The chatbot is designed to understand the conversation flow, enabling it to respond accurately to user queries.
*   **Persona Prompting**: The chatbot allows users to specify a persona, providing responses tailored to that persona's characteristics.

## How to Run
--------------

To get started with the chatbot, follow these steps:

### Prerequisites

*   Python 3.8 or higher
*   `groq` library installed

### Running the Chatbot

```bash
git clone https://github.com/[username]/Multi-Turn-Chatbot-with-Memory.git
cd Multi-Turn-Chatbot-with-Memory
pip install -r requirements.txt
python main.py
```

### Testing the Chatbot

Use a tool like `curl` or a REST client to send requests to the chatbot endpoint. The chatbot expects `POST` requests with a JSON body containing user input.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"input": "Hello, how are you?"}' http://localhost:5000/chat
```

## Tech Stack
--------------

This project utilizes the following technologies:

*   **Python 3.8**: The primary programming language used for implementing the chatbot.
*   **Groq API**: A low-latency AI inference platform for serving LLaMA 3.1 models.
*   **LLaMA 3.1**: A large language model that provides the core NLP capabilities for the chatbot.
*   **Flask**: A lightweight web framework used to build the chatbot API.

## What I learned
-----------------

Developing this project taught me the importance of conversation memory and context awareness in chatbots. I learned how to integrate the Groq API with LLaMA 3.1 to build a scalable and efficient NLP pipeline.

### Contributions

If you'd like to contribute to this project or build upon it, please don't hesitate to reach out. Your feedback and suggestions are greatly appreciated.

### License

This project is licensed under the MIT License. For more information, please see the [LICENSE](LICENSE) file.

### Acknowledgments

I'd like to thank the Groq team for providing the Groq API, which enabled me to build this project. Additionally, I'd like to thank the Hugging Face team for their amazing work on LLaMA 3.1.