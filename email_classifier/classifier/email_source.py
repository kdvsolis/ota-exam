import pandas as pd

class CSVEmailSource:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_emails(self):
        df = pd.read_csv(self.csv_file)
        emails = df['text'].tolist()
        return emails
