from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.services.external import find_player_id_by_name
from app.services.external import get_last_season_averages
from app.services.external import get_player_age

app = FastAPI()

# serve the html page 
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_index():
    return FileResponse("static/index.html")

@app.get("/api/player")
def get_player(name: str):
    player_id = find_player_id_by_name(name)
    if player_id is None:
        return {"error": "Player not found"}
    
    stats = get_last_season_averages(player_id)
    return {
        "name": name,
        "ppg": stats["ppg"],
        "rpg": stats["rpg"],
        "apg": stats["apg"],
    }

