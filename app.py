
# 1. Library imports
from starlette.requests import Request
import uvicorn ##ASGI server
from fastapi import FastAPI,Form
from fastapi.templating import Jinja2Templates    #to use the templates

from BankNote import BankNote
import pandas as pd, numpy as np, pickle

# 2. Create the app object
app = FastAPI()
#De-serializing
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)
pickle_in.close()

templates=Jinja2Templates(directory='templates' )   #mentioning where the templates are


# # 3. Index route, opens automatically on http://127.0.0.1:8000
# @app.get('/')
# def index():
#     return {'message': 'Hello, World'}

# # 4. Route with a single parameter, returns the parameter within a message
# #    Located at: http://127.0.0.1:8000/AnyNameHere
# @app.get('/{name}')
# def get_name(name: str):
#     return {'Welcome To My Welcome page ': f'{name}'}

# # 5. Expose the prediction functionality, make a prediction from the passed
# #    JSON data and return the predicted Bank Note with the confidence
# @app.post('/predict')
# def predict_output(data : BankNote):         #the input is matched with the class variables of BankNote(like a datatype)
#     # print(data,type(data))   #<class 'BankNote.BankNote'>
#     data=data.dict()   
#     var=data['variance']
#     skew=data['skewness']
#     curt=data['curtosis']
#     entr=data['entropy']
#     predicted_val=classifier.predict([[var,skew,curt,entr]])
#     # print(predicted_val)  #it's a list of length 1
#     if(predicted_val[0]==1):
#         val='Forged Note'
#     else:
#         val='Genuine Note'

#     return {
#         'prediction':val
#     }    

@app.get('/')
def home_page(request:Request):
    return templates.TemplateResponse('home.html',{
        'request':request,      #the rendering response requires 'request' object 
   })

@app.post('/predict')
def predict_output(request:Request,variance: str = Form(...), skewness: str = Form(...), curtosis: str = Form(...),entropy: str = Form(...)):       
    predicted_val=classifier.predict([[variance,skewness,curtosis,entropy]])
    # print(predicted_val)  #it's a list of length 1
    if(predicted_val[0]==1):
        val='Forged Note'
    else:
        val='Genuine Note'

    return templates.TemplateResponse('prediction_page.html',{
        'request':request,      #the rendering response requires 'request' object 
        'prediction':val,    #injecting the content we need to the html page
        # 'src':'image/note_image.jpg'
    })



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


#To run the execute the file--> uvicorn app:app --reload           i.e uvicorn <python_file_name:fastapi_object_name> --reload
#to open swagger UI (allows us to test the API with a UI)--> http://127.0.0.1:8000/docs