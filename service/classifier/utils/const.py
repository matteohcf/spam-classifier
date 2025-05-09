import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from dataclasses import dataclass, field
from config import SPAM_HAM_DATASET_PATH



@dataclass
class Dataset:
    csv_path: str = SPAM_HAM_DATASET_PATH
    label_column: str = 'label'
    validation_size: float = 0.2
    random_state: int = 11

    dataset: pd.DataFrame = field(init=False)
    X_train: any = field(init=False)
    X_test: any = field(init=False)
    y_train: any = field(init=False)
    y_test: any = field(init=False)
    vectorizer: any = field(init=False)

    def __post_init__(self):
        # Inizializzazione avviene qui
        le = LabelEncoder()

        self.dataset = pd.read_csv(self.csv_path)

        ds_train = self.dataset.drop(self.label_column, axis=1)
        ds_labels = self.dataset[self.label_column]

        # Converte le etichette in numeri
        ds_labels = le.fit_transform(ds_labels)

        # Trasforma il testo in vettori TF-IDF
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        ds_train = self.vectorizer.fit_transform(ds_train['text'])

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            ds_train,
            ds_labels,
            test_size=self.validation_size,
            random_state=self.random_state
        )

    def get_training_data(self):
        """Ritorna i dati di training"""
        return self.X_train, self.y_train

    def get_test_data(self):
        """Ritorna i dati di test"""
        return self.X_test, self.y_test

    def get_full_dataset(self):
        """Ritorna il dataset completo"""
        return self.dataset