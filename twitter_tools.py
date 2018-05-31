from models import Person
import tweepy
from datetime import datetime, date, time, timedelta

people = []

def twitter(screen_name):
    for person in people:
        if person.screen_name == screen_name:
            return person.__dict__

    api = get_api()

    user = None
    try:
        user = api.get_user(screen_name)
    except tweepy.error.TweepError:
        return {"Error":"Username Not Found"}
    tweets_count = user.statuses_count
    account_created_date = user.created_at
    followers_count = user.followers_count
    days = (datetime.utcnow() - account_created_date).days

    timeline = []
    for status in tweepy.Cursor(api.user_timeline, screen_name='@'+screen_name).items():
        timeline.append({"text":status._json["text"],"created_at":status._json["created_at"]})

    avg = float(tweets_count)/float(days)
    person = Person(screen_name,tweets_count,followers_count,days,timeline,avg)
    people.append(person)
    return person.__dict__

def get_api():
    consumer_key = 'G3tjNyIcIwpOJZUnm3cyNwPHF'
    consumer_secret = '1psvt6xyLoLplDJvH3CNnlKaCEdECN7YI1V0A4zcFJtUdTiH5G'

    access_token = '177596781-RKlaoiAwIWf1in3eQITDC6GIPtJ6MTIJsyhCNk6H'
    access_token_secret = '52iksOh15zqiq2a40lYf9jef0NE0C7vwWaOs4pu4KIfHO'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
