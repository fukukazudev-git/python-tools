from io import DEFAULT_BUFFER_SIZE

import pandas as pd

switch = 3.5

df = pd.read_csv("data\\sample-signal.csv")

if switch == 1:
    print(df.head())
    print(df.shape)
    print(df.columns)

if switch == 2:
    print(df["speed"])
    print(df[["time", "speed"]])
    print(df[df["speed"] >= 20])

if switch == 3:
    df["diff_speed"] = df["speed"].diff()
    df["prev_speed"] = df["speed"].shift(1)
    print(df)

if switch == 3.5:
    print("=== 立ち上がり検出 (signal_A が 0→1) ===")
    df["rise_A"] = (df["signal_A"] == 1) & (df["signal_A"].shift(1) == 0)
    print(df[["signal_A", "rise_A"]].head(10))

if switch == 4:
    df["speed"] = df["speed"].rolling(window=3).mean()
    print(df)

if switch == 5:
    df.to_csv("data\\output.csv", index=False)
