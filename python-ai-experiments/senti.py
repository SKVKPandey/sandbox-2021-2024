import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Sample text data with multiple emotions
data = [
    "I love this product, it's fantastic!",
    "Terrible experience, would not recommend.",
    "The weather is okay, nothing special.",
    "Amazing service, highly recommended.",
    "Disappointed with the quality, not worth it.",
    "I feel happy today!",
    "That's sad news.",
    "This is really frustrating!",
    "He looks anxious.",
    "The concert was awesome!",
    "I'm afraid of the dark.",
]

# Corresponding labels for the text data (0: negative, 1: neutral, 2: positive, 3: happy, 4: sad, 5: frustrating, 6: anxious, 7: awesome, 8: afraid)
labels = np.array([2, 0, 1, 2, 0, 3, 4, 5, 6, 7, 8])

# Tokenizing the text data using NLTK word_tokenize
tokenized_data = [word_tokenize(sentence) for sentence in data]
vocab = {word for sentence in tokenized_data for word in sentence}
word_to_idx = {word: i for i, word in enumerate(vocab)}

# Convert tokens to numbers
data = [[word_to_idx[word] for word in sentence] for sentence in tokenized_data]

# Padding sequences
maxlen = 20
for i in range(len(data)):
    data[i] += [0] * (maxlen - len(data[i]))
data = np.array(data)

# Define a simple neural network model for sentiment analysis
class SentimentClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, output_dim):
        super(SentimentClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc = nn.Linear(embedding_dim, output_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        embedded = embedded.mean(1)  # Global average pooling
        output = self.fc(embedded)
        return output

# Hyperparameters
VOCAB_SIZE = len(vocab)
EMBEDDING_DIM = 16
OUTPUT_DIM = 3  # 3 classes: negative, neutral, positive
LEARNING_RATE = 0.001
EPOCHS = 10
BATCH_SIZE = 32

# Initialize the model
model = SentimentClassifier(VOCAB_SIZE, EMBEDDING_DIM, OUTPUT_DIM)

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# Convert data and labels to PyTorch tensors
data = torch.LongTensor(data)
labels = torch.LongTensor(labels)

# Training the model
for epoch in range(EPOCHS):
    optimizer.zero_grad()
    outputs = model(data)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch+1}/{EPOCHS}], Loss: {loss.item()}')

# Predict sentiments for a new paragraph
new_paragraph = [
    "The movie was incredible, I enjoyed every bit of it.",
    "Average performance, nothing special.",
    "This restaurant is terrible, I will not go there again."
]
tokenized_new = [word_tokenize(sentence) for sentence in new_paragraph]
new_data = np.array([[word_to_idx.get(word, 0) for word in sentence] + [0] * (maxlen - len(sentence)) for sentence in tokenized_new])
new_data = torch.LongTensor(new_data)

with torch.no_grad():
    predictions = model(new_data)
    softmax = F.softmax(predictions, dim=1)
    probabilities, predicted = torch.max(softmax, 1)

# Mapping prediction results to sentiments
sentiment_mapping = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}

# Display sentiments graphically
for i, prob in enumerate(probabilities):
    plt.figure()
    plt.bar(sentiment_mapping.values(), prob)
    plt.title(f"Sentiment Analysis for Paragraph {i+1}")
    plt.xlabel("Sentiments")
    plt.ylabel("Probability")
    plt.show()
