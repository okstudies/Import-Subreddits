# Import-Subreddits
Import subreddit subscriptions from your old Reddit account

# Installation
1. Install pip3

`sudo apt-get install python3-pip`

2. Install praw

`sudo -H pip3 install praw`

# Usage
Create Reddit application
1. Open your Reddit application preferences by clicking [here](https://www.reddit.com/prefs/apps/).
2. Add a new application. It doesn't matter what it's named, but calling it "Import-Subreddits" makes it easier to remember.
3. Select "script".
4. Redirect URL does not matter for script applications, so enter something like http://127.0.0.1:8080
5. Once created, you should see your application under developed applications

    14 Charater string under `personal use script` is `client_id`
    27 Charater string next to `secret` is `client_secret`

    Username and password are simply your Reddit login credentials for the account that will be used.

6. Open terminal in the repository folder and run `startimport.py` by using following command
`python3 startimport.py`
