# Geoguesser Challenge Result API

3rd party API for accessing Geoguessr challenge scores. Uses the API found within Geoguessr to extract scores and store them in pandas DataFrames for ease of use

## Installation

```
python3 -m pip install geoguessr
```

If you'd like to clone it and run it that way, you can that by running the following command after cloning this repository:

```
python setup.py install
```

## Example

```py
from geoguessr import Geoguesser
from geoguessr.util import clean

# initialize our instance of the class
geo = Geoguessr()

# make the html request to API
challenge_id = "abc123"
raw_data = geo.get_challenge_scores(chal)
scores = clean(raw_data)
```

### Sample output

| playerName | totalScore |   R1 |   R2 |   R3 |   R4 |   R5 |
| :--------- | ---------: | ---: | ---: | ---: | ---: | ---: |
| John       |      17120 | 4566 | 2940 | 4782 | 3589 | 1243 |
| Jane       |      11740 |   86 | 2632 | 2808 | 3896 | 2318 |
| Sue        |      10148 | 1396 | 3278 | 3422 |  112 | 1940 |
| Bob        |       9954 |   51 | 2718 | 4997 |  443 | 1745 |
| Mary       |       8796 |   95 |   23 | 3186 | 3747 | 1745 |

## Requirements / Inputs

In order to use this API you will need to have participated in the challenge and have your ncfa cookie value stored as the environment variable:

```
GEOGUESSR_COOKIE
```

By default this library uses <a href=https://pypi.org/project/python-dotenv/>python-dotenv</a> and its corresponding `.env` file to store environment variables.

This value can be found in the dev tools section of your browser. Look for the \_ncfa value and copy it. You will store your variable like the following, replacing with your custom cookie value:

```
GEOGUESSR_COOKIE=_ncfa={MY COOKIE VALUE}
```

This is slightly confusing with the double equal sign, but that is how it should be formated so the request can properly go through. To reduce errors this value should be URL encoded (but don't worry that is the default on Chrome dev tools if you copied it over from there).

## Class Methods

```py
.get_challenge_scores(
    self,
    challenge_id: str = None
    ) -> list:
```

Returns the raw response for the given challenge_id. Challenge_id can be found in the URl of the challenge. This is the code that is found after either `/results/` or `/challenge/` in the URL. Because this returns a raw response, there are utility functions to help clean and parse the data into other forms

## Utility Functions (from util import \*)

```py
.clean(
    raw_data: list,
    column_list: list = ["totalScore"],
    include_round_scores: bool = True
    ) -> pd.DataFrame
```

The main parsing function to clean challenge scores and put them into a DataFrame.

`raw_data`: is your response from `.get_challenge_scores()`

`column_list`: is which columns you'd like to include, by default this is only the totalScore, but a list of all columns you can chose from is included below.

`include_round_scores`: will determine if you would like to see each round score included in your output, by default this is True and will show each rounds' score.

### Potential Columns

|   # | Column                                       | Dtype   |
| --: | :------------------------------------------- | :------ |
|   0 | gameToken                                    | object  |
|   1 | userId                                       | object  |
|   2 | totalScore                                   | int64   |
|   3 | isLeader                                     | bool    |
|   4 | pinUrl                                       | object  |
|   5 | game.token                                   | object  |
|   6 | game.type                                    | object  |
|   7 | game.mode                                    | object  |
|   8 | game.state                                   | object  |
|   9 | game.roundCount                              | int64   |
|  10 | game.timeLimit                               | int64   |
|  11 | game.forbidMoving                            | bool    |
|  12 | game.forbidZooming                           | bool    |
|  13 | game.forbidRotating                          | bool    |
|  14 | game.streakType                              | object  |
|  15 | game.map                                     | object  |
|  16 | game.mapName                                 | object  |
|  17 | game.panoramaProvider                        | int64   |
|  18 | game.bounds.min.lat                          | float64 |
|  19 | game.bounds.min.lng                          | float64 |
|  20 | game.bounds.max.lat                          | float64 |
|  21 | game.bounds.max.lng                          | float64 |
|  22 | game.round                                   | int64   |
|  23 | game.rounds                                  | object  |
|  24 | game.player.totalScore.amount                | object  |
|  25 | game.player.totalScore.unit                  | object  |
|  26 | game.player.totalScore.percentage            | float64 |
|  27 | game.player.totalDistance.meters.amount      | object  |
|  28 | game.player.totalDistance.meters.unit        | object  |
|  29 | game.player.totalDistance.miles.amount       | object  |
|  30 | game.player.totalDistance.miles.unit         | object  |
|  31 | game.player.totalDistanceInMeters            | float64 |
|  32 | game.player.totalTime                        | int64   |
|  33 | game.player.totalStreak                      | int64   |
|  34 | game.player.guesses                          | object  |
|  35 | game.player.isLeader                         | bool    |
|  36 | game.player.currentPosition                  | int64   |
|  37 | game.player.pin.url                          | object  |
|  38 | game.player.pin.anchor                       | object  |
|  39 | game.player.pin.isDefault                    | bool    |
|  40 | game.player.newBadges                        | object  |
|  41 | game.player.newObjectives                    | object  |
|  42 | game.player.explorer                         | object  |
|  43 | game.player.id                               | object  |
|  44 | game.player.nick                             | object  |
|  45 | game.player.isVerified                       | bool    |
|  46 | game.progressChange.xpProgressions           | object  |
|  47 | game.progressChange.awardedXp.totalAwardedXp | int64   |
|  48 | game.progressChange.awardedXp.xpAwards       | object  |
|  49 | game.progressChange.prevRank                 | object  |
|  50 | game.progressChange.newRank                  | object  |
|  51 | game.progressChange.medal                    | int64   |
|  52 | game.progressChange.seasonProgress           | object  |
|  53 | game.progressChange.competitiveProgress      | object  |
