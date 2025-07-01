**📧 Classificatore di Email Spam con FastAPI e Machine Learning**

Questo progetto espone un'API con FastAPI che permette di classificare un testo (email) come spam o non spam utilizzando un algoritmo di Machine Learning. Il testo può essere inviato in italiano: verrà automaticamente tradotto in inglese per permettere la corretta classificazione tramite un modello addestrato su un dataset di email in lingua inglese.

⚙️ Requisiti

- Python 3.12.1
- pip

**🚀 Istruzioni per l'avvio**

- pip install -r requirements.txt
- Configurare il file .env
- Avviare il progetto con uvicorn main:app --reload
- Utilizza la [Collection Postman](./Spam-Classifier.postman_collection.json) per testare l'api 



**📌 Descrizione del progetto**

Il progetto nasce con l'obiettivo di classificare email in spam o non spam usando un approccio di Machine Learning. Il flusso di elaborazione è il seguente:

L'utente invia un testo (in italiano) tramite una richiesta POST.

Il testo viene tradotto automaticamente in inglese usando GoogleTranslator (deep_translator).

Il modello SVC (Support Vector Classifier), già addestrato tramite [Dataset](service/classifier/datasets/spam_ham_dataset.csv), analizza il testo e restituisce la classificazione.

I dati della richiesta e della risposta vengono salvati su MongoDB per tener traccia delle richieste effettuate.

**🧠 Algoritmo SVC**

L'algoritmo SVC (Support Vector Classifier) è un modello di apprendimento supervisionato che cerca di trovare una "linea di tendenza" che separi le email spam da quelle non spam nel modo più netto possibile. Dopo un confronto tra più algoritmi, SVC si è dimostrato il più accurato per il dataset precendentemente citato.

**📁 Struttura dei file**
* `/api` – La cartella api contiene tutte le rotte esposte, sia di autenticazione sia per gli utenti sia per la classificazione
* `/service` – La cartella service contiene i servizi tra cui autenticazione ed il vero e proprio classificatore
* `/utils` – La cartella utils contiene tutte le utility, per l'env e per mongodb


**📦 Dataset**

Il dataset utilizzato è un classico dataset di email etichettate come spam e non spam, in lingua inglese. È stato preprocessato e vettorizzato per l’addestramento del modello SVC.
