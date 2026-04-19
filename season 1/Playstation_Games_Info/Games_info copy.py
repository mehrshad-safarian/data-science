import pandas as pd
import numpy as np
df = pd.read_csv("I:/begining og data_scince/Playstation_Games_Info/" \
"game_details.csv")
print(df.fillna(df['col'].mean()))
