import praw
from OAuth2Util import OAuth2Util

subreddit_name = 'delete_from_here'

r = praw.Reddit("New application for /r/steroids by /u/timlardner - v1.0 alpha")
o = OAuth2Util(r, server_mode=True)
o.refresh()
user = r.get_me()
for submission in user.get_submitted(limit=50):
    if str(submission.subreddit)==subreddit_name:
        print('Deleting '+str(submission))
        submission.delete()
    else:
        print('Other submission: '+str(submission))

