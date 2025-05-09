from sklearn.svm import SVC
from googletrans import Translator
import asyncio

def train_classifier(dataset):
    """Addestra un classificatore SVC sul dataset"""
    X_train, y_train = dataset.get_training_data()
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)
    return model

def classify_text(text, model, dataset):
    """Classifica un testo utilizzando il modello addestrato"""
    text_vectorized = dataset.vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]
    probability = model.predict_proba(text_vectorized)[0][prediction]
    return prediction, probability


async def translate_text(text):
    translator = Translator()

    # Definisci una funzione che gestisce l'attesa in modo sincrono
    def sync_translate():
        # Usa asyncio.run solo all'interno di questa funzione sincrona
        # che verrà eseguita in un thread separato
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(translator.translate(text, src='it', dest='en'))
        return result.text

    # Esegui la funzione sincrona in un thread separato
    current_loop = asyncio.get_event_loop()
    translated = await current_loop.run_in_executor(None, sync_translate)
    return translated

async def classify_italian_text(text, model, dataset):
    # Traduzione asincrona
    translated_text = await translate_text(text)
    # Classificazione sincrona
    result = classify_text(translated_text, model, dataset)
    return result[0]  # Restituisci solo la previsione (0 o 1)