from sklearn.svm import SVC
from googletrans import Translator
import asyncio


def train_classifier(dataset):
    """
    Addestra un classificatore SVC sul dataset

    Args:
        dataset: Un'istanza della classe Dataset già inizializzata

    Returns:
        Il modello addestrato
    """
    # Ottieni i dati di training
    X_train, y_train = dataset.get_training_data()

    # Crea e addestra il modello
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    return model


def classify_text(text, model, dataset):
    """
    Classifica un testo utilizzando il modello addestrato

    Args:
        text: Il testo da classificare
        model: Il modello addestrato
        dataset: L'istanza del Dataset usata per addestrare il modello

    Returns:
        La classificazione (0 o 1) e la probabilità
    """
    # Vettorizza il testo utilizzando lo stesso vectorizer usato nel training
    text_vectorized = dataset.vectorizer.transform([text])

    # Fai la previsione
    prediction = model.predict(text_vectorized)[0]
    probability = model.predict_proba(text_vectorized)[0][prediction]

    return prediction, probability


async def translate_text(text):
    translator = Translator()
    result = await translator.translate(text, src='it', dest='en')
    return result.text

def classify_italian_text(text, model, dataset):
    translated_text = asyncio.run(translate_text(text))
    return classify_text(translated_text, model, dataset)