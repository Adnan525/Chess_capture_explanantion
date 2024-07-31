import pandas as pd
df = pd.read_csv("lichess_main.csv")

moves = list(df["moves"])
moves = moves[-100:-50]


def capture_analysis(alg_moves: str) -> str:
    print(f"[INFO] Moves: {alg_moves}\n")
    analysis = "To analyse each move using Algebraic Notation and count the number of captured pieces, let's go through the game move by move:\n"
    capture_occurred = "Capture occurred in: "
    capture_count = 0

    moves_list = alg_moves.split(" ")
    # print(moves_list)
    for i, move in enumerate(moves_list):
        if "x" in move:
            capture_count += 1
            analysis += f"{i+1}. {move} (total capture {capture_count})\n"
            capture_occurred += f"{i+1}. {move}, "
        else:
            analysis += f"{i+1}. {move}\n"

    analysis += f"\n<ANSWER>: {capture_occurred.strip()[:-1]}\nTotal {capture_count} pieces were captured.\n"

    return analysis.strip()


    # for move in moves_list:
    #     print(move)
    #     if "x" in move:
    #         capture_count += 1
    #         print(f"{move} (total capture {capture_count})")
    #     else:
    #         print(f"{move}")


print(capture_analysis(moves[0]))