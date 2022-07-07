import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Geoguessr:
    def __init__(self, ncfa_cookie: str = None) -> None:
        if ncfa_cookie is not None:
            os.environ["GEOGUESSR_COOKIE"] = ncfa_cookie

    def _make_request(self, endpoint) -> None:
        response = requests.request("GET", endpoint, headers=self._get_headers())
        return response.json()

    @staticmethod
    def _get_headers() -> dict:
        cookie = os.environ.get("GEOGUESSR_COOKIE")
        if cookie is None:
            raise KeyError("Please define GEOGUESSR_COOKIE as an environment variable")
        return {
            "authority": "www.geoguessr.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": os.environ["GEOGUESSR_COOKIE"],
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36",
        }

    def set_challenge_id(self, challenge_id: str) -> None:
        self.challenge_id = challenge_id

    def set_user_id(self, user_id: str) -> None:
        self.user_id = user_id

    def get_challenge_scores(self, challenge_id: str = None) -> list:
        if challenge_id is not None:
            self.set_challenge_id(challenge_id)
        if challenge_id is None and self.challenge_id is None:
            raise NameError(
                "'self.challenge_id' and 'challenge_id' are both None. Please pass in a valid challenge_id."
            )
        url = (
            f"https://www.geoguessr.com/api/v3/results/scores/{self.challenge_id}/0/26"
        )
        return self._make_request(url)

    def get_user_activity(self) -> list:
        url = "https://www.geoguessr.com/api/v4/feed/private"
        return self._make_request(url)
