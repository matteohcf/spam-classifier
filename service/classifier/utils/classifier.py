from sklearn.svm import SVC
from googletrans import Translator
from deep_translator import GoogleTranslator
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


async def translate_text(text, input_lang = 'it', output_lang = 'en'):
    loop = asyncio.get_event_loop()

    def sync_translate():
        return GoogleTranslator(source=input_lang, target=output_lang).translate(text)

    translated = await loop.run_in_executor(None, sync_translate)
    return translated

async def classify_italian_text(text, model, dataset):
    translated_text = await translate_text(text)
    result = classify_text(translated_text, model, dataset)
    return result[0]  # return (0 o 1)