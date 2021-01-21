#pip install fastapi uvicorn

# 1. Library imports
import uvicorn ##ASGI server
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To My Welcome Page Bros': f'{name}'}



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)


#To run the execute the file--> uvicorn main:app --reload           i.e uvicorn <python_file_name:fastapi_object_name> --reload
#to open swagger UI (allows us to test the API)--> http://127.0.0.1:8000/docs