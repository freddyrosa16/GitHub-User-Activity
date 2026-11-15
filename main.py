import requests
import json

def main():
    pushEvent = {}
    username = input('Enter your Github username: ')
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        print('Output:')
        for event in response.json():
            if event['type'] == 'PushEvent':
                repo_name = event['repo']['name']
                if not repo_name in pushEvent:
                    pushEvent[repo_name] = 1
                else:
                    pushEvent[repo_name] += 1
            elif event['type'] == 'CreateEvent':
                repo_name = event['repo']['name']
                if event['payload']['ref_type'] == 'branch':
                    print(f"Created {event['payload']['ref_type']} {event['payload']['ref']} in {repo_name}", '\n')
            elif event['type'] == 'DeleteEvent':
                repo_name = event['repo']['name']
                if event['payload']['ref_type'] == 'branch':
                    print(f"Deleted {event['payload']['ref_type']} {event['payload']['ref']} from {repo_name}", '\n')
            elif event['type'] == 'ForkEvent':
                repo_name = event['repo']['name']
                print(f"Forked {repo_name} to {event['payload']['forkee']['full_name']}", '\n')
    for key, value in pushEvent.items():
        print(f'Pushed {value} pushes to {key}', '\n')

main()
