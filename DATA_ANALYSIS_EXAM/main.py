import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

game_dates = pd.date_range(start="2026-01-01", periods=n, freq="D")
flight_dates = pd.date_range(start="2026-01-02", periods=n, freq="D")

teams = ["Lakers", "Warriors", "Celtics", "Heat", "Bulls"]
opponents = ["Knicks", "Spurs", "Raptors", "Nets", "Suns"]
locations = ["Domestic", "International"]
pilots = ["Captain Cruz", "Captain Smith", "Captain Reyes", "Captain Tan", "Captain Lee"]
aircrafts = ["Boeing 737", "Airbus A320", "Boeing 747", "Embraer 190", "Bombardier CRJ"]

points = np.random.randint(50, 130, size=n)          
rebounds = np.random.randint(5, 20, size=n)          
assists = np.random.randint(2, 15, size=n)           
flight_hours = np.random.uniform(1.0, 6.0, size=n)   
delays = np.random.randint(0, 120, size=n)           

df = pd.DataFrame({
    "Game_Date": game_dates,
    "Flight_Date": flight_dates,
    "Team_Name": np.random.choice(teams, size=n),
    "Opponent_Team": np.random.choice(opponents, size=n),
    "Location": np.random.choice(locations, size=n),
    "Pilot_Name": np.random.choice(pilots, size=n),
    "Aircraft_Type": np.random.choice(aircrafts, size=n),
    "Points_Scored": points,
    "Rebounds": rebounds,
    "Assists": assists,
    "Flight_Duration_Hours": flight_hours.round(2),
    "Delay_Minutes": delays
})

df.to_csv("sports_flight_schedule.csv", index=False)

print("sports_flight_schedule.csv created successfully with", n, "rows and", df.shape[1], "columns.")
