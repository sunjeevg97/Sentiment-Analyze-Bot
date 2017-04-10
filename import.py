import praw
import requests
import requests.auth
import oauth
from bs4 import BeautifulSoup
import csv
import re

client_id = 'aCOsBF1HMnSKDg'
client_secret = 'tpvzRJM44mwXXy2UsZoVSD54ThM'

reddit = oauth.oauth(client_id, client_secret)
idx = 0

comment_file = open('comments.csv', 'wb')
wr = csv.writer(comment_file, dialect = 'excel')

for comments in reddit.subreddit('all').comments(limit = None):
    idx += 1
    soup = BeautifulSoup(comments.body_html,"lxml")
    if not soup.find('a'):
        for node in soup.findAll('p'):
            wr.writerow([''.join(node.findAll(text = True)).encode('utf-8')])
print idx

'''ids = submission
post = reddit.submission(ids)
post.comment_sort = 'top'
post.comments.replace_more(limit = 1)

comment_file = open('comments.csv', 'wb')
wr = csv.writer(comment_file, dialect = 'excel')

for top_level_comments in list(post.comments):
    soup = BeautifulSoup(top_level_comments.body_html,"lxml")
    if not soup.find('a'):
        for node in soup.findAll('p'):
            wr.writerow([''.join(node.findAll(text = True))])'''
