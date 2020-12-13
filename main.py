from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import create_model as model
from preprocess import DataProcess
import torch
import torch.nn as nn
class GetData(BaseModel):
    pickupDateTime: str
    fareClass: int
    plong: float
    plat: float
    dlong: float
    dlat: float
    passengerCount: int

app = FastAPI()

@app.get('/')
async def greeting():
    return {'message':'Hello World'}

@app.post('/prediction/')

async def getData(data:GetData):
    data = data.dict()

    makeData = DataProcess()
    x_cat, x_cont = makeData.process(data.get('pickupDateTime'), data.get('plat'), data.get('plong'), data.get('dlat'), data.get('dlong'), data.get('fareClass'), data.get('passengerCount'))
    embed_size = [(24, 12), (2, 1), (7, 4)]
    model_l = model.TabularModel(embed_size,3,1,[32,64,128])
    model_l.load_state_dict(torch.load('taxiModelRegression.pt'))
    model_l.eval()
    with torch.no_grad():
        y = model_l(x_cat, x_cont)
        
    return {'Estimated Fare':str(int(y))}


if __name__ == '__main__':
    uvicorn.run(app, port = 8080, host='localhost')