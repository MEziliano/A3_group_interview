from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np
import os 

CLASS_NAMES = ['setosa', 'versicolor', 'virginica']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'iris_model.pkl')

model =  None

app = FastAPI(
    title="API Iris", 
    description="API para previsão de Iris usando modelo baseado em Árvore de decisão", 
    version="1.0.0"
)

class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., example = 5.1, description="Comprimento da sépala em cm")
    sepal_width:  float = Field(..., example = 3.5, description="Largura da sépala em cm")
    petal_width:  float = Field(..., example = 1.4, description="Comprimento da pétala em cm") 
    petal_length: float = Field(..., example = 0.2, description="Largura da pétala em cm")

    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_width": 1.4,
                    "petal_length": 0.2
                }
            ]
        }
    }

@app.on_event("startup")
async def load_model_on_startup():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            print(f"Modelo '{MODEL_PATH}' carregado com sucesso na inicialização")
        except Exception as e:
            print(f"Erro ao carregar modelo '{MODEL_PATH}': {e}")
            raise RuntimeError(f"Falha ao carregar o modelo na inicilização {e}")
    else:
        print(f"ERRO: Arquivo do modelo '{MODEL_PATH}' não encontrado. Execute 'train_and_save_model.py' primeiro.")
        raise FileNotFoundError(f"Modelo '{MODEL_PATH}' não encontrado. Execute o script de treinamento primeiro.")
    
@app.get("/")
async def read_root():
    return {"message": "Modelo de Predição Iris"}

@app.post("/predict")
async def predict_iris_species(features: IrisFeatures):
    if model is None:
        raise HTTPException(status_code=500, detail= "Modelo não carregado")
    try:
        input_data = np.array([
            features.sepal_length, 
            features.sepal_width,
            features.petal_width,
            features.petal_length
        ]).reshape(1, -1)


        prediction_index = model.predict(input_data)[0]
        prediction_class = CLASS_NAMES[prediction_index]

        probabilidades = model.predict_proba(input_data)[0]
        prob_dict = {name: float(prob) for name, prob in zip(CLASS_NAMES, probabilidades)}

        return {
            "prediction": prediction_class,
            "probabilidades": prob_dict,
            "input_fatures": features.model_dump() 
        }

    except Exception as e:
        print(f"Erro ao processar: {e}")
        raise HTTPException(status_code=500, detail= {e})