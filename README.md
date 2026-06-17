 Artificial Intelligence & Machine Learning Projects

This repository contains three beginner-level AI/ML projects developed using Python.  
These projects demonstrate concepts like rule-based AI, machine learning classification, and recommendation systems using NLP techniques.

---

 Projects Included

 1. Simple Rule-Based Chatbot

 Description
A basic chatbot built using Python conditional logic.  
The chatbot responds to predefined user inputs and runs continuously until the user exits the conversation.

 Features
- Handles greetings
- Responds to common questions
- Supports exit commands
- Uses if-else decision-making logic

 Concepts Used
- Python basics
- Conditional statements
- Loops
- User input handling

 How to Run

```bash
python chatbot.py

Chatbot: Hello! Type 'exit' to end the chat.

You: hello
Chatbot: Hi there! How can I help you?

You: bye
Chatbot: Goodbye! Have a nice day.

2. Handwritten Digit Classification Using Machine Learning
Description

A machine learning classification project that recognizes handwritten digits from 0-9 using the Scikit-learn Digits Dataset.

The model learns patterns from handwritten digit images and predicts the correct digit class.

Algorithm Used
Decision Tree Classifier
Dataset

Scikit-learn Digits Dataset

Contains:

1797 handwritten digit samples
10 classes (0-9)
Image features converted into numerical values
Workflow
Load dataset
Data visualization
Data preprocessing
Split dataset into training and testing data
Train classification model
Make predictions
Evaluate performance
Libraries Used
Pandas
Matplotlib
Scikit-learn
Evaluation Metrics
Accuracy Score
Classification Report
How to Run
python digit_classification.py

3. TF-IDF Recommendation System
Description

A content-based recommendation system that recommends items according to user interests.

The system compares user preferences with item descriptions using NLP similarity techniques.

Features
Accepts multiple user interests
Converts text into numerical vectors
Calculates similarity between preferences and items
Filters low matching results
Sorts recommendations by relevance
Algorithm Used

TF-IDF Vectorization + Cosine Similarity

Workflow
Data Ingestion

Stores item names and descriptions.

User Input

Collects multiple interests from the user.

Feature Extraction

TF-IDF converts text data into numerical vectors.

Scoring

Cosine similarity calculates the match score.

Filtering

Removes recommendations with low similarity.

Sorting

Displays highest matching results first.

Libraries Used
Scikit-learn
How to Run
python recommendation_system.py
Example Output
Enter interest 1: AI
Enter interest 2: Python
Enter interest 3: Coding
Enter interest 4: Machine Learning


Recommended Items:

Machine Learning Course --> Match Score: 0.62
Python Programming Projects --> Match Score: 0.45
Deep Learning Tutorial --> Match Score: 0.31
Technologies Used
Python
Machine Learning
Natural Language Processing
Scikit-learn
Pandas
Matplotlib
Installation

Clone the repository:

git clone https://github.com/yourusername/AI-ML-Projects.git

Install required libraries:

pip install -r requirements.txt
Project Structure
AI-ML-Projects/

│
├── chatbot.py
│
├── digit_classification.py
│
├── recommendation_system.py
│
├── README.md
│
└── requirements.txt
Author

Abdullah Khan

Artificial Intelligence Intern

Future Improvements
Add GUI interface for chatbot
Try advanced ML models for digit recognition
Improve recommendation accuracy using larger datasets
Deploy projects as web applications

Also create a `requirements.txt` file for this repo:

```txt
pandas
matplotlib
scikit-learn
