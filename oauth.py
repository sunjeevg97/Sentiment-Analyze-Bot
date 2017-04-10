import requests
import requests.auth
import praw

def oauth(cid, secret):
    reddit = praw.Reddit(client_id= cid,
                         client_secret= secret,
                         user_agent='osx:localhost:8080:v.1.0(by /u/sentimentanalyzebot)')
    return reddit
