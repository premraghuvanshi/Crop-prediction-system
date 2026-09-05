import pandas as pd
import joblib
from pathlib  import Path
import numpy as np
import os

CURRENT_DIR = Path(__file__).resolve().parent

PROJECT_ROOT = CURRENT_DIR if (CURRENT_DIR / "app.py").exists() else CURRENT_DIR.parent


def crop_recommendation(data : dict)-> dict:

    MODEL_PATH = PROJECT_ROOT / "Model" / "saved_model" / "Crop_recommendation.pkl"

    df=pd.DataFrame([data])

    try:

        loaded_model = joblib.load(MODEL_PATH)

        prediction = loaded_model.predict(df)

        probabilities = loaded_model.predict_proba(df)

        confidence = round(np.max(probabilities)*100,2)

        return {
            "status" : "success",
            "message" : "prediction completed",
            "data" : {
                "prediction": prediction.tolist()[0],
                "confidence" : confidence
            }
        }

    except Exception as e:

        return {"status" : "failed", "message": str(e)}
    

def crop_production(data : dict)-> dict:

    MODEL_PATH = PROJECT_ROOT / "Model" / "saved_model" / "Crop_production.pkl"

    df = pd.DataFrame([data])

    try :

        loaded_model = joblib.load(MODEL_PATH)

        prediction = loaded_model.predict(df)

        

        return {
            "status" : "success",
            "message": "prediction complete",
            "data" : {
                "prediction" : round(prediction.tolist()[0],1)
                
            }
        }

    except Exception as e :

        return {"status" : "failed", "message" : str(e)}