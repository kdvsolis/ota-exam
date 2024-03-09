from django.shortcuts import render
from .models import Email
from .email_source import CSVEmailSource
from .classifier import EmailClassifier
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def classify_emails(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        email_source = CSVEmailSource(csv_file)
        emails = email_source.read_emails()

        def is_newsletter(email):
            keywords = ['unsubscribe', 'subscribe', 'opt out']
            return any(keyword in email for keyword in keywords)
        labels = [is_newsletter(email) for email in emails]

        classifier = EmailClassifier(emails, labels)
        classifier.train()

        classifications = []
        for email in emails:
            classification = classifier.classify(email)
            classifications.append({'content': email, 'is_newsletter': classification})

        return render(request, 'classification_results.html', {'classifications': classifications})

    return render(request, 'classify.html')
