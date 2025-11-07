from typing import Optional, Dict, List
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import pandas as pd
from datetime import datetime

def find_player_id_by_name(name: str) -> Optional[int]:
    match = players.find_players_by_full_name(name)
    if not match:
        return None
    return match[0]["id"]

def get_last_season_averages(player_id: int) -> Optional[Dict]:
    # Return last available season line: season, ppg, rpg, apg.
    df: pd.DataFrame = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    if df.empty:
        return None
    row = df.iloc[-1]  # last season row
    gp = float(row["GP"]) if float(row["GP"]) != 0 else 1  # avoid division by zero
    return {
        # Don't know if nba_api stores as a string or an int, so if it's a string return the first 4 chars and convert to int
        "season": int(row["SEASON_ID"][:4]) if isinstance(row["SEASON_ID"], str) else int(row["SEASON_ID"]),
        "ppg": float(round(float(row["PTS"]) / gp + 1e-8, 1)), # to round up from 0.05 to 0.1
        "rpg": float(round(float(row["REB"]) / gp + 1e-8, 1)),
        "apg": float(round(float(row["AST"]) / gp + 1e-8, 1)),
        # Could add steals and blocks later
    }

id = find_player_id_by_name("Stephen Curry")

averages = get_last_season_averages(id)
print(averages)
