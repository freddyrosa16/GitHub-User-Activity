# GitHub User Activity

## What it does

Enter a GitHub username and it shows some of that user's recent public activity: pushes grouped by repo, branches created or deleted, and repos forked. It counts pushes, not commits, and it doesn't show the user's full history.

## How to run it

You'll need Python 3 and Git. Clone the repo, make a virtual environment, and install `requests`:

```sh
git clone https://github.com/freddyrosa16/GitHub-User-Activity.git
cd GitHub-User-Activity
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
python main.py
```

Enter a username when it asks. Here's an example of what the output can look like:

```text
Enter your Github username: example
Output:
Created branch fix-readme in example/my-project

Pushed 2 times to example/my-project
```

## What I learned

One thing I had to figure out was how to tell the difference between a user with no recent activity and a request that failed. An empty list means the request worked, just with nothing to show. I also learned to clean up the username before making the request and use a dictionary to count pushes for each repo.
