from instapy import InstaPy

##### TO DO #####
"""
- Integrate session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
- Add prompt for Headless browser session = InstaPy(username='test', password='test', headless_browser=True)
- Set relationshiop bounds session.set_relationship_bounds(enabled=True, max_followers=8500)
- Add prompts for hashtags and amount (or for session quota)
"""

#Asks for username and password
username = input("Username: ")
password = input("Password: ")

#Uses InstaPy to login to Instagram via FireFox
session = InstaPy(username=username, password=password)
session.login()

#### BOT OPTIONS ####

#Sets the tags to like, as well as how many likes.
#Note that it automatically likes the top 9 posts for each hashtag
session.like_by_tags([],amount=0)
#Sets any keywords to avoid liking. These keywords can appear anywhere in the
#post, incl hashtags and descriptions
session.set_dont_like([])
#Sets whether or not to follow users and what percentage of users to follow
session.set_do_follow(False,percentage=0)
#Sets whether or not to comment on posts and what percentage of users to follow
session.set_do_comment(False,percentage=0)
#A list of comments that will be added to posts.
session.set_comments([])

session.end()
