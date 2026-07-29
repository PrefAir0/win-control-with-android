from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Word(BaseModel):
    game: str
    id: int


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/start")
def create_item(item: Word, ):
    print(item.player, item.word)
    return {"game_name": item.game, "game_id": item.id}
