import pandas as pd
from dotenv import load_dotenv


def refresh_dotenv() -> None:
    """refreshes dotenv"""
    load_dotenv()


def parse_activity_response(response: list) -> list:
    pass


def parse_challenge_response(response: list) -> pd.DataFrame:
    """
    given the API response (list of all players who completed the challenge)
    we will make a DataFrame and set the index to the player name
    """
    df = pd.json_normalize(response)
    df.set_index("playerName", inplace=True)
    return df


def extract_round_guesses(
    response: dict, include_perfect_score_column: bool = False
) -> pd.DataFrame:
    """returns a pd.DataFrame columns 1-5 index playerName for the given response"""
    d = {}
    for player in response:
        scores = [
            int(x["roundScore"]["amount"]) for x in player["game"]["player"]["guesses"]
        ]
        d[player["playerName"]] = scores

    df = pd.DataFrame(d).T
    df.columns = df.columns + 1
    df.columns = [f"R{x}" for x in df.columns]
    df.index.name = "playerName"
    if include_perfect_score_column:
        df["perfect_scores"] = check_perfect_scores(df)
    return df


def check_perfect_scores(df: pd.DataFrame) -> pd.Series:
    """returns a count of all rounds scores that == 5000"""
    return (df[[f"R{x}" for x in range(1, 6)]] == 5000).T.sum()


def simplify_table(df: pd.DataFrame, cols: list = None) -> pd.DataFrame:
    """removes the uncessessary columns, desired columns can be overwritten using the cols parameter"""
    if cols is None:
        cols = [
            "userId",
            "totalScore",
            "game.player.totalTime",
            "game.player.totalDistance.miles.amount",
        ]
    df = df[cols].copy()
    # convert miles to a float
    if "game.player.totalDistance.miles.amount" in cols:
        df["game.player.totalDistance.miles.amount"] = (
            df["game.player.totalDistance.miles.amount"].astype(float).copy()
        )
    return df[cols]


def clean(
    raw_data: list,
    column_list: list = ["totalScore"],
    include_round_scores: bool = True,
) -> pd.DataFrame:
    """performs the common cleaning opperations"""
    # parse the JSON response as a pd.DataFrame
    all_data_df = parse_challenge_response(raw_data)
    # simplify the entire response to just get the totalScore
    player_data = simplify_table(all_data_df, column_list)
    if include_round_scores:
        # extract the round data for each player into a pd.DataFrame
        round_data = extract_round_guesses(raw_data)
        # join the player and round data together for our final table
        player_data = player_data.join(round_data)

    return player_data
