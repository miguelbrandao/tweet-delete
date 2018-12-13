# '$ pydoc3 twitter.api' for documentation

import twitter  # python-twitter
import json
import sys


# Import keys
keys_file = open("keys.json","r")
keys = json.load(keys_file)
keys_file.close()

# Authentication
user = twitter.Api( consumer_key = keys["consumer_key"],
                    consumer_secret = keys["consumer_secret"],
                    access_token_key = keys["access_token_key"],
                    access_token_secret = keys["access_token_secret"])

try:
    my_data = user.VerifyCredentials()
except twitter.error.TwitterError:
    sys.exit("Authentication failed!\nCheck that you have the 'keys.json' file in the same directory as this script")

print("Authenticated!\n")

# Get number of tweets (and retweets) and favorites
n_tweets = my_data.statuses_count
n_favorites = my_data.favourites_count

# Fetch and delete tweets and retweets
print("Deleting "+str(n_tweets)+" tweets and retweets...")
deleted = 0
print_every_nth = 20
print_counter = 0
timeline = user.GetUserTimeline(count=200,include_rts=True)
while timeline:
    for i in range(len(timeline)):
        user.DestroyStatus(timeline[i].id)
        deleted += 1
        print_counter += 1
        # prints message every 'print_every_nth' tweets deleted
        if print_counter == print_every_nth:
            print_counter = 0
            print("   Deleted " + str(deleted) + " out of " + str(n_tweets))
    timeline = user.GetUserTimeline(count=200,include_rts=True)
print("All "+str(n_tweets)+" tweets and retweets deleted!\n")

# Fetch and delete favorites
print("Deleting "+str(n_favorites)+" favorites...")
deleted = 0
print_every_nth = 20
print_counter = 0
favorites = user.GetFavorites(count=200)
while favorites:
    for i in range(len(favorites)):
        user.DestroyFavorite(favorites[i])
        deleted += 1
        print_counter += 1
        # prints message every 'print_every_nth' tweets deleted
        if print_counter == print_every_nth:
            print_counter = 0
            print("   Deleted " + str(deleted) + " favorites out of " + str(n_favorites))
    favorites = user.GetFavorites(count=200)
print("All "+str(n_favorites)+" favorites deleted!\n")

user.ClearCredentials()

print("All done!")
