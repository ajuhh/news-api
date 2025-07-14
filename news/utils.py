import requests
from transformers import pipeline
import torch


import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
import requests
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

NEWS_API_KEY = 'YOUR_NEWS_API_KEY'
...


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

NEWS_API_KEY = 'YOUR_NEWS_API_KEY'

def fetch_news(endpoint):
    url = f"https://newsapi.org/v2/{endpoint}"
    params = {'apiKey': NEWS_API_KEY}
    response = requests.get(url, params=params)
    return response.json().get("articles", [])

def summarize_text(text):
    if len(text.split()) < 30:
        return text
    summary = summarizer(text[:1024], max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
