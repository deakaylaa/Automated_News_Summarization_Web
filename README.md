# Automated News Summarization

This is a Text Mining project that automatically extracts and summarizes news articles from any URL. It uses Deep Learning (Transformer-based model) to provide concise summaries, helping users save reading time while maintaining the core context of the news.

## 🚀 Features
* **Web Scraping**: Automatically extracts main article text from URLs using `BeautifulSoup4`.
* **Abstractive Summarization**: Uses the **BART (Bidirectional and Auto-Regressive Transformers)** model for generating human-like summaries.
* **Text Analytics**: Calculates original vs summary length, compression percentage, and estimated reading time saved.
* **FastAPI Backend**: A high-performance API with built-in CORS support for easy frontend integration.

## 🛠️ Tech Stack
* **Language**: Python 3.13+
* **Framework**: FastAPI
* **NLP Library**: Hugging Face Transformers (Model: `facebook/bart-large-cnn`)
* **Data Extraction**: BeautifulSoup4, Requests, Regular Expressions (Re)
* **Validation**: Pydantic

## 📊 Text Mining Pipeline
1. **Data Acquisition**: Fetching HTML content from the provided URL.
2. **Preprocessing**: Cleaning HTML tags (scripts, nav, footer) and normalizing whitespace using Regex.
3. **Text Extraction**: Identifying and joining paragraph tags (`<p>`) to get the main content.
4. **Model Inference**: Encoding text and generating summaries using the BART-Large-CNN transformer.
5. **Post-Processing**: Calculating metrics like compression ratio and time-saving estimation.

# Pressto: AI-Powered Automated News Summarization

Pressto is a Text Mining project that automatically extracts and summarizes news articles from any URL. It uses Deep Learning (Transformer-based model) to provide concise summaries, helping users save reading time while maintaining the core context of the news.

## 🚀 Features
* **Web Scraping**: Automatically extracts main article text from URLs using `BeautifulSoup4`.
* **Abstractive Summarization**: Uses the **BART (Bidirectional and Auto-Regressive Transformers)** model for generating human-like summaries.
* **Text Analytics**: Calculates original vs summary length, compression percentage, and estimated reading time saved.
* **FastAPI Backend**: A high-performance API with built-in CORS support for easy frontend integration.

## 🛠️ Tech Stack
* **Language**: Python 3.13+
* **Framework**: FastAPI
* **NLP Library**: Hugging Face Transformers (Model: `facebook/bart-large-cnn`)
* **Data Extraction**: BeautifulSoup4, Requests, Regular Expressions (Re)
* **Validation**: Pydantic

## 📊 Text Mining Pipeline
1. **Data Acquisition**: Fetching HTML content from the provided URL.
2. **Preprocessing**: Cleaning HTML tags (scripts, nav, footer) and normalizing whitespace using Regex.
3. **Text Extraction**: Identifying and joining paragraph tags (`<p>`) to get the main content.
4. **Model Inference**: Encoding text and generating summaries using the BART-Large-CNN transformer.
5. **Post-Processing**: Calculating metrics like compression ratio and time-saving estimation.

<img width="713" height="437" alt="image" src="https://github.com/user-attachments/assets/cb2dcc43-203c-4999-a137-42a0abb96335" />
<img width="451" height="425" alt="image" src="https://github.com/user-attachments/assets/479de2ec-4399-42a4-8b06-cdd24c8660e1" />
