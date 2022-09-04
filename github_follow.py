from github import Github
import requests

USERNAME = ''
PERSONAL_ACCESS_TOKEN = ''

session = requests.session()
session.auth = (USERNAME, PERSONAL_ACCESS_TOKEN)
following_increased = 0

def follow(username):    
    global following_increased
    session.put(f'https://api.github.com/user/following/{username}')
    following_increased += 1
    print(f"Following {username}\n Following increased by: {following_increased}")

g = Github(PERSONAL_ACCESS_TOKEN)

user = g.get_user(USERNAME)
my_followings = [i.login for i in user.get_following()]

PEOPLE_TO_KEEP_FOLLOWING = []

for i in my_followings:
    following_user = g.get_user(i) 
    for follower in following_user.get_followers():
        if (follower.login not in PEOPLE_TO_KEEP_FOLLOWING) and (follower.login not in my_followings):
            follow(follower.login)       
