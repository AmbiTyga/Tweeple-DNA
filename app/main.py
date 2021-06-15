from TweetAPI import TweetAPI
import pandas as pd
import numpy as np
from DNA import get_dna
from pydantic import BaseModel
import lightgbm
import logging

# Server
import uvicorn
from fastapi import FastAPI

# Modeling

app = FastAPI()

api = TweetAPI(consumer_key = None,
			consumer_secret = None	,
			access_token= None,		
			access_token_secret = None
)

        

clf = lightgbm.Booster(model_file = '..\\model.txt')

label = np.array(['human','bot'])

class Data(BaseModel):
	id : str

@app.post("/predict")
def predict(id:Data):
	try:
		timeline = pd.DataFrame([x._json for x in api.user_timeline(id.dict()['id'],counts=100)])
		inP = get_dna(timeline)
	
		pred = clf.predict([[inP['size'],inP['compressed_size'],inP['compression_ratio']]])
		
		return {
			'Bot Probabilty':pred[0],
			'Label':label[pred.round(0).astype(int)][0]
		}

	except Exception as e:
		logging.error(e)	
		