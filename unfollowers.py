import json

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def extract_usernames(data):
    usernames = {}
    for entry in data:
        if isinstance(entry, dict):
            for string_data in entry.get('string_list_data', []):
                usernames[string_data['value']] = string_data['href']
    return usernames

def find_non_followers(followers, following):
    non_followers = {}
    for username, href in following.items():
        if username not in followers:
            non_followers[username] = href
    return non_followers

def main():
    followers_data = load_json('followers_1.json')
    following_data = load_json('following.json')

    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data['relationships_following'])

    non_followers = find_non_followers(followers, following)

    for username, href in non_followers.items():
        print(f"Username: {username}, Href: {href}")

if __name__ == "__main__":
    main()