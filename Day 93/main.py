import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.basketball-reference.com/leagues/NBA_2025_per_game.html"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


table = soup.find("table", {"id": "per_game_stats"})


headers = [th.getText() for th in table.find("thead").findAll("th")][1:]


rows = table.find("tbody").findAll("tr")
player_stats = []
for row in rows:
    if row.find("th", {"scope": "row"}):
        stats = [td.getText() for td in row.findAll("td")]
        player_stats.append(stats)


df = pd.DataFrame(player_stats, columns=headers)


df.to_csv("nba_player_stats.csv", index=False)

print("Scraping complete! CSV saved as nba_player_stats.csv")
