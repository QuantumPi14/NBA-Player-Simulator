from typing import Optional, Dict, List
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo
import pandas as pd
from datetime import datetime, timezone

def find_player_id_by_name(name: str) -> Optional[int]:
    match = players.find_players_by_full_name(name)
    if not match:
        return None
    return match[0]["id"]

def get_last_season_averages(player_id: int) -> Optional[Dict]:
    # Return last available season line: season, ppg, rpg, apg, spg, bpg, fg%, 3pt%.
    df: pd.DataFrame = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    if df.empty:
        return None
    row = df.iloc[-1]  # last season row
    gp = float(row["GP"]) if float(row["GP"]) != 0 else 1  # avoid division by zero
    fg_pct = float(row["FG_PCT"])
    fg3_pct = float(row["FG3_PCT"]) 

    
    return {
        # Don't know if nba_api stores as a string or an int, so if it's a string return the first 4 chars and convert to int
        "season": int(row["SEASON_ID"][:4]) if isinstance(row["SEASON_ID"], str) else int(row["SEASON_ID"]),
        "ppg": float(round(float(row["PTS"]) / gp + 1e-8, 1)), # to round up from 0.05 to 0.1
        "rpg": float(round(float(row["REB"]) / gp + 1e-8, 1)),
        "apg": float(round(float(row["AST"]) / gp + 1e-8, 1)),
        "spg": float(round(float(row["STL"]) / gp + 1e-8, 1)),
        "bpg": float(round(float(row["BLK"]) / gp + 1e-8, 1)),
        "fg_pct": fg_pct,
        "fg3_pct": fg3_pct,
    }


def get_career_averages(player_id: int) -> List[Dict]:
    # Return list of {season, ppg, rpg, apg} for all seasons of a player's career
    df: pd.DataFrame = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    out: List[Dict] = []
    for _, r in df.iterrows():
        season = int(r["SEASON_ID"][:4]) if isinstance(r["SEASON_ID"], str) else int(r["SEASON_ID"])
        gp = float(r["GP"]) if float(r["GP"]) != 0 else 1  # prevent division by zero
        out.append({
            "season": season,
            "ppg": round(float(r["PTS"]) / gp + 1e-8, 1),
            "rpg": round(float(r["REB"]) / gp + 1e-8, 1),
            "apg": round(float(r["AST"]) / gp + 1e-8, 1),
        })
    return out

def get_player_age(player_id: int, season_year: Optional[int] = None) -> Optional[int]:
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_dict()
    items = info.get("resultSets", [])[0].get("rowSet", [])
    
    if not items:
        return None
    # Birth date is column 7 in CommonPlayerInfo in the form YYYY-MM-DDT00:00:00
    bday_str = items[0][7]
    try: 
        birth = datetime.fromisoformat(bday_str)
        # Make birth timezone-aware (assume UTC) to match today's timezone-aware datetime
        if birth.tzinfo is None:
            birth = birth.replace(tzinfo=timezone.utc)
    except Exception:
        return None
    # make today also timezone aware if we pass the season parameter 
    # so we don't run into a type error when returning today - birth
    today = datetime(season_year, 6, 30, tzinfo=timezone.utc) if season_year else datetime.now(tz=timezone.utc)
    return ((today - birth) // 365).days

def get_player_position(player_id: int) -> Optional[str]:
    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_dict()
    items = info.get("resultSets", [])[0].get("rowSet", [])
    
    if not items:
        return None
    # Position is column 14 in CommonPlayerInfo
    position = items[0][14] if len(items[0]) > 14 else None
    return position if position else None



