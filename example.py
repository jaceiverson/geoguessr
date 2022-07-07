from geoguessr import Geoguessr
import geoguessr.util as gg


def main():
    # define our challenge ID and Geoguessr class instance
    chal = "7pDoDvAl7zzlKpFe"
    geo = Geoguessr()

    # make the html request to API
    raw_data = geo.get_challenge_scores(chal)

    # Now we need to parse our result to get only the data we want
    # both these options below derive the same result

    """OPTION 1 - use each cleaning method individually"""

    if raw_data:
        # parse the JSON response as a pd.DataFrame
        all_data_df = gg.parse_challenge_response(raw_data)
        # extract the round data for each player into a pd.DataFrame
        round_data = gg.extract_round_guesses(raw_data)
        # simplify the entire response to just get the totalScore
        player_data = gg.simplify_table(all_data_df, ["totalScore"])
        # join the player and round data together for our final table
        df = player_data.join(round_data)

    """OPTION 2 - use the clean() function to do all opperations in one"""
    if raw_data:
        df = gg.clean(raw_data)


if __name__ == "__main__":
    main()
