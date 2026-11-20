import requests

def main():
    pushEvent = {}
    username = input('Enter your Github username: ').strip()
    if not username:
        print('Enter a GitHub username.')
        return
    url = f"https://api.github.com/users/{username}/events"
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            events = response.json()
            if not events:
                print('No recent activity found')
                return
            print('Output: ')
            for event in events:
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
            print(f'Pushed {value} times to {key}', '\n')
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f'Github user {username} not found.')
        else:
            print(f'Github request failed: {e.response.status_code}.')
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
main()
