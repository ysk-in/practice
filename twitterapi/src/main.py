import json, sys, time, calendar
from requests_oauthlib import OAuth1Session

config_path = r"C:\secret\twitter_api.json"

CONF_API_KEY = ""
CONF_API_SECRET = ""
CONF_ACCESS_TOKEN = ""
CONF_ACCESS_SECRET = ""


def set_keys_and_tokens(api_key, api_secret, access_token, access_secret):
    global CONF_API_KEY, CONF_API_SECRET, CONF_ACCESS_TOKEN, CONF_ACCESS_SECRET
    CONF_API_KEY = api_key
    CONF_API_SECRET = api_secret
    CONF_ACCESS_TOKEN = access_token
    CONF_ACCESS_SECRET = access_secret


def set_config():
    config_file = open(config_path, "r")
    config_json = json.load(config_file)
    api_json = config_json["api"]
    access_json = config_json["access"]
    set_keys_and_tokens(api_json["key"], api_json["secret"],
                        access_json["token"], access_json["secret"])


def convert_createdat_to_japanform(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    japan_format = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return japan_format


def query_tweets(twitter):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?tweet_mode=extended"
    params = {
        "screen_name": "kantei",
        "count": 200,  # 200が最大
        "exclude_replies": False,
        "include_rts": False
    }
    res = twitter.get(url, params=params)

    if res.status_code != 200:
        print("status_code is not 200. status_code = {}".format(res.status_code))
        return

    count_tweet = 1;
    timeline = json.loads(res.text)
    for tweet in timeline:
        if tweet["favorite_count"] <= 1000:
            continue
        japan_time = convert_createdat_to_japanform(tweet["created_at"])
        print("===== ({}) =====\nRetweetCount={}, FavoriteCount={}, CreatedAt={}, id={}\n----------------\n{}".format(
            count_tweet, tweet["retweet_count"], tweet["favorite_count"], japan_time, tweet["id"], tweet["full_text"]))
        count_tweet += 1


def main():
    set_config()
    twitter = OAuth1Session(CONF_API_KEY, CONF_API_SECRET, CONF_ACCESS_TOKEN, CONF_ACCESS_SECRET)
    query_tweets(twitter)


if __name__ == "__main__":
    main()
