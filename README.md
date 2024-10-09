# Unfollowers Script

This Python script identifies Instagram users who you follow but who do not follow you back. It compares two JSON files: `followers_1.json` and [`following.json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A34%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition"), and outputs the usernames and profile links of users who don't follow you back.

## Prerequisites

- Python 3.x
- JSON files: `followers_1.json` and [`following.json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A34%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition")

## JSON File Structure

### followers_1.json

```json
[
  {
    "title": "",
    "media_list_data": [],
    "string_list_data": [
      {
        "href": "https://www.instagram.com/username1",
        "value": "username1",
        "timestamp": 1726971682
      }
    ]
  },
  ...
]
```

### following.json

```json
{
  "relationships_following": [
    {
      "title": "",
      "media_list_data": [],
      "string_list_data": [
        {
          "href": "https://www.instagram.com/username2",
          "value": "username2",
          "timestamp": 1726549200
        }
      ]
    },
    ...
  ]
}
```

## How to Use

1. **Clone the repository or download the script.**

2. **Ensure you have the required JSON files (`followers_1.json` and [`following.json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A34%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition")) in the same directory as the script.**

3. **Run the script:**

   ```sh
   python unfollowers.py
   ```

4. **The script will output the usernames and profile links of users who don't follow you back.**

## Script Explanation

### Functions

- **load_json(filename)**: Reads a JSON file and returns its content.
- **extract_usernames(data)**: Extracts usernames and their profile links from the [`string_list_data`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A42%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition") array.
- **find_non_followers(followers, following)**: Compares the usernames from the followers and following lists and identifies those who don't follow back.

### Main Workflow

1. **Load JSON Data**: The script loads the contents of `followers_1.json` and [`following.json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A34%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition").
2. **Extract Usernames**: It extracts the usernames and profile links from the [`string_list_data`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A42%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition") arrays in both files.
3. **Compare Usernames**: It identifies usernames in [`following.json`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fag%2FDocuments%2Fig%20data%2Funfollowers%2Funfollowers.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A14%2C%22character%22%3A34%7D%7D%5D%2C%223a3ca622-e203-4545-82f7-9c6f3a8acdc2%22%5D "Go to definition") that are not in `followers_1.json`.
4. **Output Results**: It prints the usernames and profile links of users who don't follow you back.

## Example Output

```sh
Username: username2, Href: https://www.instagram.com/username2
Username: username3, Href: https://www.instagram.com/username3
...
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
