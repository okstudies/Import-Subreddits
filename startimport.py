#! /usr/bin/python3
import praw
import getpass


def login():
    username = input("username=")
    password = getpass.getpass()
    client_id = input("client_id=")
    client_secret = input("client_secret=")
    return praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=username, username=username)


i = input('''1: Clean old subscriptions
2: Keep old subscriptions\n''')

c = input('''1: Check the type of subreddits before subscribing (slower))
2: Dont check for subreddit type (faster, but might cause errors)''')

print('Log into old Reddit Account')
source = login()
print('Log into new Reddit Account')
drain = login()

accepted_subreddit_types = ['public', 'restricted']
failed_subscriptions = []

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
subreddit = source.user.subreddits(limit=None)
subreddits = [str(s) for s in subreddit]

if c == '1':
    for subreddit in subreddits:
        print('Checking type of {}'.format(subreddit))
        if source.subreddit(subreddit).subreddit_type not in accepted_subreddit_types:
            print('{} is not in accepted subreddit types ({}).'.format(subreddit, source.subreddit(subreddit).subreddit_type))
            subreddits.remove(subreddit)
            failed_subscriptions.append(subreddit)

drain.subreddit(subreddits[0]).subscribe(other_subreddits=subreddits)
for subreddit in subreddits:
    print('Subscribed to {}'.format(subreddit))
for subreddit in failed_subscriptions:
    print('You need to manually subscribe to {}'.format(subreddit))
