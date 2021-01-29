import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/search"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}

query = {
   'jql': 'project = TTS'
}

response=requests.get(url,headers=headers,params=query,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
data=response.json()
issues=data["issues"]
for issue in issues:
    print(issue["key"])

