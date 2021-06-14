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

api = TweetAPI(consumer_key = 'WQXzjRaf3Ql66dcv4hls1ULkS',
			consumer_secret = 'QQG7PPvchLRul5dhAMLi7KWp59U56Hh1399zpBSfGQ7ZTKR8m1'	,
			access_token= '983655149049528321-LJacg24BNwe19VE51mKhFJ8IPwpiVia',		
			access_token_secret = 'cx3hRsOdeRK8FuBnbLXT6suTREvyzdmfAM2PFWAsBw5vZ'
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
		