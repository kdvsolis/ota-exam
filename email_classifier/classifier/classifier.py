from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class EmailClassifier:
    def __init__(self, emails, labels):
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
        self.emails = emails
        self.labels = labels

    def train(self):
        email_vectors = self.vectorizer.fit_transform(self.emails)
        self.classifier.fit(email_vectors, self.labels)

    def classify(self, email):
        email_vector = self.vectorizer.transform([email])
        return self.classifier.predict(email_vector)
