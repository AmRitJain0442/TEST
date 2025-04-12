from fastapi import FastAPI  

key=1234
app = FastAPI()  
@app.get("/")  
def read_root():
  return {"message": "Amrit here"} 

@app.get("/naam")
def read_name():
    return {"message": "Amrit lahari"}

@app.get("/password/{key}")
def read_password():
    return {"message": "Amrit1234"}

