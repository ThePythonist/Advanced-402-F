import json
from pprint import pprint

data = {
    "url": "https://www.youtube.com/watch?v=UmljXZIypDc",
    "title": "django tutorial part 1",
    "date": "2017",
    "comments": True,
    "list_of_comments": [
        {
            "john": "awesome!",
            "likes": 0,
        },
        {
            "david": "keep it up",
            "likes": 43,
        }
    ],
    "suggestions": ["flask tutorial", "fastapi tutrial"],
    "likes": None,
}

# Serialize

json_data = json.dumps(data)
pprint(json_data)

# file = open("data.json", "w")
# json.dump(data, file, indent=4)
