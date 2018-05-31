class Person():
    def __init__(self,screen_name,tweets_count,followers_count,days,timeline,avg):
        self.screen_name = screen_name
        self.tweets_count = tweets_count
        self.followers_count = followers_count
        self.days = days
        self.timeline = timeline
        self.average_tweet_per_day = avg

    def __str__(self):
        data = {}
        data["User"] = self.screen_name
        data["Tweets"] = self.tweets_count
        data["Days since creation"] = self.days
        data["Followers"] = self.followers_count
        data["Average Tweets per day"] = self.average_tweet_per_day
        data["Timeline"] = self.timeline
        return str(data)
