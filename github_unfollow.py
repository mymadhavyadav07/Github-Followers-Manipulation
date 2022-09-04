from github import Github
import requests


USERNAME = ''
PERSONAL_ACCESS_TOKEN = ''
session = requests.session()
session.auth = (USERNAME, PERSONAL_ACCESS_TOKEN)

def un_follow(username):    
    session.delete(f'https://api.github.com/user/following/{username}')
    print(f"Unfollowed {username}")

g = Github(PERSONAL_ACCESS_TOKEN)

user = g.get_user(USERNAME)

followers = []
PEOPLE_TO_KEEP_FOLLOWING = []

for i in user.get_followers():
    followers.append(i.login)

for i in user.get_following():
    if (i.login not in followers) and (i.login not in PEOPLE_TO_KEEP_FOLLOWING):
        un_follow(i.login)

 




