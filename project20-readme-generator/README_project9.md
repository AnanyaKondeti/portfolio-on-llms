**Prompt Response Evaluator** 🤖

A Python-based framework for evaluating the quality of Large Language Model (LLM) responses across 5 key criteria.

## What it does

The Prompt Response Evaluator is a cutting-edge solution designed to automatically assess the quality of LLM responses based on 5 comprehensive criteria:

* **Relevance**: Measures how well the response addresses the original prompt
* **Accuracy**: Evaluates the factual correctness of the response
* **Completeness**: Assesses the thoroughness and depth of the response
* **Clarity**: Evaluates the response's coherence and ease of understanding
* **Conciseness**: Measures the response's brevity and effectiveness

The tool provides an intuitive and scalable way to evaluate LLM responses, enabling users to:

* Streamline the quality assessment process
* Identify areas for improvement in LLM training
* Optimize LLM performance and accuracy

## Key Features

* Automatic scoring across 5 quality criteria
* Support for multiple LLM models and APIs
* Customizable scoring weights and thresholds
* High-performance scoring with Groq API and LLaMA 3.1
* Robust error handling and debug logging

## How to Run

To get started with the Prompt Response Evaluator, follow these steps:

1. Clone the repository using `git clone https://github.com/your-username/Prompt-Response-Evaluator.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Configure the Groq API and LLaMA 3.1 models by editing `config.json`
4. Run the evaluator using `python main.py <prompt>`

### Example Use Case

Evaluate an LLM response for the prompt "What is the capital of France?"
```bash
python main.py "What is the capital of France?" -p 0.8 -a 0.7
```
## Tech Stack

* **Language**: Python 3.9+
* **APIs**:
	+ Groq API for high-performance scoring
	+ LLaMA 3.1 for language modeling capabilities
* **Libraries**: NumPy, Pandas, Scikit-learn for data science and machine learning tasks

## What I Learned

Throughout the development of the Prompt Response Evaluator, I gained valuable insights into the importance of:

* **Customizable scoring**: Enabling users to tailor the scoring criteria to their specific needs
* **High-performance scoring**: Utilizing Groq API and LLaMA 3.1 for fast and accurate responses
* **Error handling and logging**: Ensuring robust reliability and debuggability in the tool

I hope this professional README showcases the capabilities and benefits of the Prompt Response Evaluator.