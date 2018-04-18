#! /usr/bin/python3
import praw
import getpass


def login():
    client_id = input("client_id=")
    client_secret = input("client_secret=")
    password = getpass.getpass()
    username = input("username=")
    return praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=username, username=username)


i = input('''1: Clean old subscriptions
2: Keep old subscriptions\n''')
print('Log into old Reddit Account')
drain = login()
print('Log into new Reddit Account')
source = login()

# Unsubscribing from old subreddits
if i == '1':
    print('Unsubscribing from old subreddits')
    old = drain.user.subreddits()
    olds = [str(o) for o in old]
    drain.subreddit(olds[0]).unsubscribe(other_subreddits=olds)
    for subreddit in olds:
        print('Unsubscribed from {}'.format(subreddit))

# Subscribing to imported subreddts
print('Getting List of subreddits from old Account')
subreddit = source.user.subreddits()
subreddits = [str(s) for s in subreddit]
for subreddit in subreddits:
    print('Subscribed to {}'.format(subreddit))
