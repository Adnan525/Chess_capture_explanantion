import pandas as pd

df = pd.read_csv("lichess_main.csv")
df = df.sample(100)

moves = list(df["moves"])
question_string = "How many chess pieces have been captured so far in this game - "


def get_capture_analysis(alg_moves: str) -> str:
    # print(f"[INFO] Moves: {alg_moves}\n")
    analysis = "To analyse each move using Algebraic Notation and count the number of captured pieces, let's go through the game move by move:\n"
    capture_occurred = "Capture occurred in: "
    capture_count = 0

    moves_list = alg_moves.split(" ")
    # print(moves_list)
    for i, move in enumerate(moves_list):
        if "x" in move:
            capture_count += 1
            analysis += f"{i + 1}. {move} (total capture {capture_count})\n"
            capture_occurred += f"{i + 1}. {move}, "
        else:
            analysis += f"{i + 1}. {move}\n"

    analysis += f"\n<ANSWER>: {capture_occurred.strip()[:-1]}\nTotal {capture_count} pieces were captured.\n"

    # if alg_moves.count("x") != capture_count:
    #     raise KeyError

    return analysis.strip()

# for move in moves_list:
#     print(move)
#     if "x" in move:
#         capture_count += 1
#         print(f"{move} (total capture {capture_count})")
#     else:
#         print(f"{move}")


train_df = pd.DataFrame(columns=["Question", "Context", "Answer"])
for move in moves:
    question = f"{question_string}{move}?"
    capture_analysis = get_capture_analysis(move)
    data = {"Question": question, "Context": "", "Answer": capture_analysis}
    train_df.loc[len(train_df)] = data
    print(question)
    print(capture_analysis)
    break
# train_df.to_csv("final_train_capture.csv", index=False)