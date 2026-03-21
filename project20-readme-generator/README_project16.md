**Prompt A/B Testing Dashboard 💡**
=====================================

## What it does
----------------

The Prompt A/B Testing Dashboard is a Python application that enables easy comparison of two prompts across multiple test inputs with scoring. This tool is designed to automate the process of scoring and selecting the top-performing prompts, providing data-driven insights to aid in informed decision-making.

## Key Features
---------------

* **Automated Scoring**: The dashboard leverages the Groq API and LLaMA 3.1 models to score prompts against test inputs, providing a comprehensive evaluation of their performance.
* **Winner Selection**: The application identifies the top-scoring prompt, facilitating easy comparison and selection of the most effective prompt.
* **Data-Driven Comparison**: The dashboard provides an interactive interface for exploring and analyzing the scoring results, enabling users to make informed decisions based on data.

## How to Run
-------------

To run the Prompt A/B Testing Dashboard, follow these steps:

1. **Install dependencies**: Run `pip install -r requirements.txt` to install the required packages.
2. **Set up Groq API**: Create a Groq API account and obtain an API key, then set the `GROQ_API_KEY` environment variable.
3. **Configure LLaMA 3.1 model**: Set the `LLAMA_MODEL_PATH` environment variable to the path of the LLaMA 3.1 model.
4. **Run the application**: Execute `python app.py` to start the dashboard.

## Tech Stack
------------

* **Programming Language**: Python
* **API**: Groq API
* **Language Model**: LLaMA 3.1

## What I learned
----------------

Working on the Prompt A/B Testing Dashboard taught me the importance of:

* **API integration**: Seamlessly integrating the Groq API with Python to leverage its scoring capabilities.
* **Model selection**: Choosing the right language model (LLaMA 3.1) for the task and optimizing its utilization.
* **Data-driven decision-making**: Designing the dashboard to facilitate data-driven comparison and selection of prompts.

Feel free to fork and contribute to this project!