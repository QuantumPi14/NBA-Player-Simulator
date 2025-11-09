# NBA Player Simulator

A web application for viewing NBA player statistics and simulating career trajectories using machine learning models.

## Current Features

The application currently allows users to:

- **Search for NBA players** by name
- **View player statistics** for their most recent season, including:
  - Points Per Game (PPG)
  - Rebounds Per Game (RPG)
  - Assists Per Game (APG)
  - Steals Per Game (SPG)
  - Blocks Per Game (BPG)
  - Field Goal Percentage (FG%)
  - 3-Point Percentage (3PT%)
- **Display stats in a clean table format** similar to basketball-reference.com

## Tech Stack

### Backend
- **Python** - Core programming language
- **FastAPI** - Web framework for building the API
- **nba_api** - Library for accessing NBA statistics data
- **pandas** - Data manipulation and analysis
- **numpy*** - Numerical computing

### Frontend
- **Vanilla HTML/CSS/JavaScript** - Simple, lightweight web UI
- Fetches and displays data from backend API endpoints

**to be implemented*


## Project Goals / Coming Soon

The ultimate goal of this project is to provide a comprehensive NBA player career simulation tool:

### Career Statistics View
- Display a player's **complete career statistics** in a table format
- Include **player age** as a column for each season
- Show all relevant stats for every season of the player's career

### Career Simulation
- **"Simulate" button** next to each season row
- Allow users to simulate a player's career (approximately 10 years) starting from any selected season
- Users can choose to simulate from:
  - The player's most recent season (projecting forward)
  - Any past season (e.g., simulating from when the player was younger to see "what could have been")
- The simulation will **ignore reality** and generate new career trajectories based on the selected starting point

### Machine Learning Model
- Use **polynomial regression** to predict future stat lines
- Model will be trained on the player's historical data up to the selected simulation start point
- Predictions will generate realistic stat progressions based on the player's past performance patterns

## Project Structure

```
NBAPlayerSim/
├── app/
│   ├── main.py              # FastAPI application and routes
│   └── services/
│       ├── external.py      # NBA API integration and data fetching
│       └── sim.py           # Simulation logic (to be implemented)
├── static/
│   ├── index.html           # Main search page
│   ├── stats.html           # Player stats display page
│   ├── app.js               # Frontend JavaScript
│   └── styles.css           # Styling
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## API Endpoints

### Current
- `GET /` - Serves the main index page
- `GET /api/player?name={player_name}` - Returns player statistics for the most recent season


