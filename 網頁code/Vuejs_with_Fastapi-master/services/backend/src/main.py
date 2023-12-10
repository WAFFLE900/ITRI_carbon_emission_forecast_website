import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # NEW
from starlette.middleware import Middleware
from os.path import dirname, join, realpath
from typing import List
import pickle
import pandas as pd
from fastapi.responses import JSONResponse

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['http://ec2-35-79-153-51.ap-northeast-1.compute.amazonaws.com'],
        # allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )
]

app = FastAPI(middleware=middleware)


class TextArea(BaseModel):
    content: str
    
class Item(BaseModel):
    name: str
    description: str

@app.post("/add")
async def post_textarea(data:TextArea):
    print(data.content)
    return data


# # load  model
# 舊model
# with open(
#     join(dirname(realpath(__file__)), "models/model_總碳排.dat"), "rb"
# ) as f:
#     model_total = pickle.load(f)

# with open(
#     join(dirname(realpath(__file__)), "models/model_總碳排.dat"), "rb"
# ) as f:
#     model_low = pickle.load(f)
    
# with open(
#     join(dirname(realpath(__file__)), "models/model_總碳排.dat"), "rb"
# ) as f:
#     model_high = pickle.load(f)

with open(
    join(dirname(realpath(__file__)), "models/xgb_reg_5_features_Model.dat"), "rb"
) as f:
    xgboost_model = pickle.load(f)

# with open(
#     join(dirname(realpath(__file__)), "models/IrisClassifier.pkl"), "rb"
# ) as f:
#     model = joblib.load(f)

def data_clean(str):
    arr = str.split(',')
    arr = list(map(float,arr))
    return arr
    
# Create Prediction Endpoint
@app.post("/predict-result")
async def predict_iris(request:TextArea):
    # perform prediction
    #print(json.loads(request.content))
    #print(request.content)
    #print(request)
    
    data = json.loads(request.content)
    #print(data['dynamicInputValue'])
    
    # if data['type'] == 'total':
    #     model = model_total
    # elif data['type'][0:3] == 'low':
    #     model = model_low
    # elif data['type'][0:4] == 'high':
    #     model = model_high
    
    print(data['type'])
    if data['type'] == "high1":
        min_CO2 = 80563
    elif  data['type'] == "high2":
        min_CO2 = 26824
    elif  data['type'] == "low1":
        min_CO2 = 66172
    elif  data['type'] == "low2":
        min_CO2 = 80563
    elif  data['type'] == "low3":
        min_CO2 = 936
    elif  data['type'] == "low4":
        min_CO2 = 28795
    elif  data['type'] == "low5":
        min_CO2 = 9393
    elif  data['type'] == "low6":
        min_CO2 = 70930
    elif  data['type'] == "low7":
        min_CO2 = 24054
    elif  data['type'] == "low8":
        min_CO2 = 371166
    elif data["type"] == "low9":
        min_CO2 = 73697
    elif data["type"] == "low10":
        min_CO2 = 11683
    elif data["type"] == "low11":
        min_CO2 = 9306
    elif data["type"] == "low12":
        min_CO2 = 71680
    elif data["type"] == "low13":
        min_CO2 = 9306
    elif data["type"] == "low14":
        min_CO2 = 71680
    elif data["type"] == "low15":
        min_CO2 = 236588
    elif data["type"] == "low16":
        min_CO2 = 52036
    elif data["type"] == "low17":
        min_CO2 = 23297
    elif data["type"] == "low18":
        min_CO2 = 98762
    elif data["type"] == "low19":
        min_CO2 = 16009
    elif data["type"] == "low20":
        min_CO2 = 17311
    elif data["type"] == "low21": 
        min_CO2 = 437263
    elif data["type"] == "low22":
        min_CO2 =  38397
    elif data["type"] == "low23":
        min_CO2 =  132852
    elif data["type"] == "low24":
        min_CO2 = 157434
    elif data["type"] == "low25":
        min_CO2 = 31432
        
        
    predata = data['dynamicInputValue']
    print("predata")
    print(predata)
    arr = ['普通股股本', '營業費用', '研究發展費', '不動產廠房及設備','存貨']
    aftdata = {}
    
    for each in predata:
        if each["name"] in arr:
            aftdata[each["name"]] = each["value"]
    print(aftdata)   
    
    data_for_predict = []
    count = 0
    for feature in arr:
        if feature in aftdata.keys():
            data_for_predict.append(aftdata[feature])
    print(data_for_predict)    
    request = data_for_predict
    request = list(map(float, request))

    json_df = {}
    i = 0
    for col in arr:
        json_df[col] = request[i]
        i += 1
    data = pd.json_normalize(json_df)
    
    prediction = xgboost_model.predict(data)
    output = int(prediction[0])
    print(output)   
    
    content = output
    if content <= 0: 
        content = min_CO2
    headers = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(content=content, headers=headers)
    
    
    # arr = ['存貨', '不動產廠房及設備', '商譽及無形資產合計', '預付投資款','應付帳款及票據'
    #        ,'普通股股本','資本公積合計','營業成本','營業費用','研究發展費','處分不動產廠房設備（含預付）－CFI',
    #        '折舊－CFO','攤提－CFO','購置不動產廠房設備（含預付）－CFI','員工人數']
    # aftdata = {}
    
    # for each in predata:
    #     if each["name"] in arr:
    #         aftdata[each["name"]] = each["value"]
    # #print(aftdata)
    
    # data_for_predict = []
    # count = 0
    # for feature in arr:
    #     if feature in aftdata.keys():
    #         data_for_predict.append(aftdata[feature])
    # print(data_for_predict)
    # request = data_for_predict
    # request = list(map(float, request))

    
    
    # prediction = model.predict([request])
    # output = int(prediction[0])
    # print(output)
    
    # content = output
    # headers = {"Access-Control-Allow-Origin": "*"}
    # return JSONResponse(content=content, headers=headers)

@app.get("/")
async def serve_home(request: Request):
    return "Hello, World!"
    # return templates.TemplateResponse("index.html", {"request": request})