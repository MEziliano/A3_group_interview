# Importar as bibliotecas
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def train_save_model():
    # Primeiro Passo - Carregar o conjunto de dados 
    df = load_iris()
    X,  y = df.data, df.target

    # Segunda Passo - Dividir conjunto de dados
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Terceiro passo - Escolher e instanciar o modelo
    model = DecisionTreeClassifier(random_state=42)
    # Quatro passo treinar o modelo
    model.fit(X_train, y_train)
    # Quinto passo - Prever
    y_pred = model.predict(X_test)
    # Sexto passo - Avaliar o modelo
    acc = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {acc:.2f}")

    # Salvar o modelo
    joblib.dump(model, "iris_model.pkl")
    print("Modelo salvo! iris_model.pkl disponível!")

if __name__ == "__main__":
    train_save_model()
