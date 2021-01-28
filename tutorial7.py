import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-4/comment/10013"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

data=json.dumps({

  "body": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "text": "comment1 updated by python",
            "type": "text"
          }
        ]
      }
    ]
  }
})

response=requests.put(url,headers=headers,data=data,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text)

