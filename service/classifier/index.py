from service.classifier.utils.classifier import train_classifier, classify_text, classify_italian_text
from service.classifier.utils.const import Dataset

email_dataset = Dataset(csv_path='datasets/spam_ham_dataset.csv')


model = train_classifier(email_dataset)

spam_text_example = "Attenzione: il tuo account bancario è stato temporaneamente sospeso. Clicca qui per verificare i tuoi dati e riattivarlo immediatamente."
not_spam_text_example = "Ciao, come stai? Volevo sapere se hai ricevuto la mia email precedente."

text_to_classify = not_spam_text_example
prediction, probability = classify_italian_text(text_to_classify, model, email_dataset)

label = "spam" if prediction == 1 else "non-spam"
print(f"Il testo è classificato come {label} con probabilità {probability:.2f}")