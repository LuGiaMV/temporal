import uvicorn
from fastapi import FastAPI
import api_data
from models.Character_Model import CharacterModel as model

app = FastAPI()

@app.get("/")
def index():
    return {
        "Message" : "Hello worlds"
    }

@app.get("/character/{id}", response_model=model)
async def character_getter(id:int):
    character = await api_data.get_characterById(id)
    return character.dict()

if __name__ == "__main__":
    uvicorn.run(app)
