# 🚀 Fine-Tuning Data Prep Pipeline
==============================

## What it does
----------------

The Fine-Tuning Data Prep Pipeline is a Python-based project that generates JSONL training data for large language model (LLM) fine-tuning. This pipeline is specifically designed to support the fine-tuning of LLaMA 3.1 models. By leveraging the Groq API and Python, this project empowers users to create tailored Q&A training datasets for their language models.

## Key Features
----------------

* **Q&A Generation**: Generate high-quality Q&A pairs for fine-tuning LLaMA models.
* **JSONL Formatting**: Output data in JSONL format for efficient model training.
* **Multiple Topics**: Support for training datasets across various topics and domains.

## How to Run
--------------

### Prerequisites

* Install Python (3.8 or later) and the required packages using pip:
  ```bash
pip install groq-api requests
```
* Sign up for a Groq API account and obtain your API key.

### Running the Pipeline

1. Clone the repository and navigate to the project root.
2. Update the `config.json` file with your Groq API key and other desired configurations.
3. Run the pipeline using the following command:
  ```bash
python pipeline.py
```
4. The pipeline will generate a JSONL file containing the Q&A training data specified in the `config.json` file.

## Tech Stack
-------------

* **Python**: Utilizes Python 3.8 or later for development and execution.
* **Groq API**: Leverages the Groq API for accessing high-quality language data.
* **LLaMA 3.1**: Designed to support fine-tuning of the LLaMA 3.1 large language model.

## What I learned
---------------

Through this project, I gained hands-on experience with:

* Utilizing the Groq API for language data acquisition.
* Developing efficient Python pipelines for data preparation.
* Customizing large language model fine-tuning datasets for specific use cases.

I hope this project inspires others to explore the applications of LLM fine-tuning and data preparation pipelines. Feel free to fork and modify this codebase to suit your own projects!