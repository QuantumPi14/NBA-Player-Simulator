from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.services.external import find_player_id_by_name
from app.services.external import get_last_season_averages
from app.services.external import get_player_age
from app.services.external import get_player_position

app = FastAPI()

# serve the html page 
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/api/player")
def get_player(name: str):
    player_id = find_player_id_by_name(name)
    if player_id is None:
        return {"error": "Player not found"}
    
    stats = get_last_season_averages(player_id)
    if stats is None:
        return {"error": "Stats not found"}
    
    age = get_player_age(player_id, stats["season"])
    position = get_player_position(player_id)
    
    return {
        "name": name,
        "age": age,
        "position": position,
        "ppg": stats["ppg"],
        "rpg": stats["rpg"],
        "apg": stats["apg"],
        "spg": stats["spg"],
        "bpg": stats["bpg"],
        "fg_pct": stats["fg_pct"],
        "fg3_pct": stats["fg3_pct"],
    }

