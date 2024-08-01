import pandas as pd

df = pd.read_csv("lichess_main.csv")
moves = list(df["moves"])

checkmate_moves = []

count = 0
for move in moves:
    if move.strip()[-1] == "#":
        checkmate_moves.append(move)
        count += 1

    if count == 100:
        break


new_df = pd.DataFrame(columns=["moves", "comment"])
for move in checkmate_moves:
    data = {"moves": move,
            "comment": ""}
    new_df.loc[len(new_df)] = data

new_df.to_csv("checkmate_moves.csv", index=False)