import yaml, tweepy, markovify

config_file = "config.yaml"

with open(config_file, "r") as f:
    config = yaml.load(f)

COUNT = config["COUNT"]
USERS = config["USERS"]

auth = tweepy.OAuthHandler(
    config["CONSUMER_KEY"],
    config["CONSUMER_SECRET"]
)
auth.set_access_token(
    config["ACCESS_TOKEN"],
    config["ACCESS_SECRET"]
)
api = tweepy.API(auth)

def make_a_tweet():
    tweets = []

    for user in USERS:
        try:
            timeline = api.user_timeline(id=user, count=COUNT)
            tweets.extend([tweet.text.encode("utf-8") for tweet in timeline])
        except:
            pass

    tweets = b"\n".join(tweets)

    return markovify.NewlineText(tweets.decode("utf-8")).make_short_sentence(140)

if __name__ == "__main__":
    api.update_status(make_a_tweet())
