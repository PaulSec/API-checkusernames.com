# API-checkusernames.com
(Unofficial) Python API for http://checkusernames.com

# How to use it?

Check ```api_example.py``` file, or look at that code:

```python
from API_checkusernames import CheckUsernames

api_check_usernames = CheckUsernames()
print api_check_usernames.search('stevewoz')
```

Pretty easy, eh?

If you run this script in your Terminal, here is the output:

```
$ python api_example.py 
['Twitter', 'Tumblr', 'Pinterest', 'Flickr', 'HuffingtonPost', 'reddit', 'Cnet', 'Yelp', 'Wikia', 'Fiverr', 'Etsy', 'askfm', 'Sourceforge', 'Answers', 'github', 'scribd', 'Disqus', 'foursquare', 'Squidoo', 'MySpace', 'Gamespot', 'MetaCafe', 'ChaCha', 'UStream', 'Polyvore', 'Crunchbase', 'Technorati', 'Plurk', 'Slashdot', 'AboutMe', 'Keek', 'Wattpad', 'rdio', 'Popsci', 'FlightAware', 'Strava', 'morgueFile']
```

You get a list of all websites who have such username registered. 

# Contributing

If you find a bug, want a specific feature, ping me on Twitter: [@PaulWebSec](https://twitter.com/PaulWebSec)

# License

Released under MIT License. 