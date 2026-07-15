# stock-market-using-nlp

# 📈 Stock Sentiment Classifier

## 📌 Project Overview

The Stock Sentiment Classifier is a Machine Learning and Natural Language Processing (NLP) project designed to analyze stock market-related text and classify its sentiment as **Positive, Negative, or Neutral**.

The project uses a GRU (Gated Recurrent Unit) deep learning model to understand textual patterns and predict sentiment. 

A Streamlit web application provides a simple interface where users can enter stock-related text and receive a sentiment prediction.

## 🎯 Project Objective

The main objective of this project is to develop an intelligent sentiment analysis system that can identify the emotional tone of stock market-related text.

The project aims to:

* Analyze stock-related textual data.
 
* Clean and preprocess text using NLP techniques.
  
* Convert text into numerical sequences.
  
* Train a GRU-based deep learning model.
  
* Classify sentiment as Positive, Negative, or Neutral.
  
* Provide real-time sentiment predictions.
  
* Build an interactive web application using Streamlit.

## 💡 Problem Statement

Stock market discussions, financial news, and investor opinions contain valuable sentiment information. Manually analyzing large amounts of textual data is difficult and time-consuming.

This project provides an automated sentiment classification system that uses NLP and Deep Learning to identify sentiment from stock-related text.

## ✨ Features

* Stock-related text sentiment analysis.
  
* NLP-based text preprocessing.
  
* GRU deep learning model.
  
* Multi-class sentiment classification.
* 
* Positive, Negative, and Neutral predictions.
* 
* Real-time sentiment prediction.
  
* Simple and interactive Streamlit interface.
  
* Trained model and tokenizer integration.

## 🛠️ Technologies Used

**Programming Language:** Python

**Libraries and Frameworks:**

* Pandas
  
* NumPy
  
* TensorFlow
  
* Keras
  
* Scikit-learn
  
* Joblib
  
* Streamlit

**Concepts:**

* Machine Learning
  
* Deep Learning
  
* Natural Language Processing (NLP)
  
* Sentiment Analysis
  
* Text Classification
  
* GRU Neural Networks

## 🔄 Project Workflow

Load the stock sentiment dataset.
 
Analyze and understand the dataset.
 
Handle missing and duplicate values.

Clean and preprocess textual data.

Encode sentiment labels.

Tokenize the text.

Convert text into numerical sequences.

Apply sequence padding.

Split the data into training and testing datasets.

Build the GRU deep learning model.

Train and evaluate the model.

Save the trained model and tokenizer.

Build a Streamlit web application.

Predict stock sentiment in real time.

## 🧠 Model Used

### GRU – Gated Recurrent Unit

GRU is a type of Recurrent Neural Network designed to process sequential data.

It is suitable for NLP tasks because it can learn patterns and relationships in textual sequences.

The GRU model is used in this project to classify stock-related text into:

* 😊 Positive
  
* 😐 Neutral
  
* 😞 Negative

## 🧹 Data Preprocessing

The text preprocessing process includes:

* Converting text to lowercase.
  
* Removing unnecessary characters.
  
* Handling missing values.
  
* Tokenizing text.
  
* Converting words into numerical sequences.
  
* Padding sequences to maintain equal input length.
  
* Encoding sentiment labels.

## 📊 Model Training

The processed text data is passed to the GRU model.

The model learns patterns from stock-related text and identifies the relationship between textual information and sentiment labels.

After training, the model is evaluated using test data to measure its prediction performance.

Python | Machine Learning | Data Science | NLP
