# tweet-delete

tweet-delete is a small and simple **python3** script that deletes all the tweets, retweets and favorites of a specified user.

## Dependencies:

* **python-twitter**
  * https://pypi.org/project/python-twitter/
  * https://github.com/bear/python-twitter
  
## How to use:

1. Get your **Consumer API keys** and **Access token & access token secret** at [Twitter Apps](https://developer.twitter.com/en/apps)
2. Place them in the appropriate places in *keys.json*
3. Make sure *tweet-delete.py* and *keys.json* are in the **same** directory
4. Run tweet-delete.py
``` bash
$ python3 tweet-delete.py
```

## WARNING
**Never upload your keys and access tokens. Make sure you never accidentally push them to an online version control platform.**
