import requests
import json
url="https://totaltechnology.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload=json.dumps(
    {
    "fields": {
       "project":
       {
          "key": "TTS"
       },
       "summary": "created for test",
       "description": "Created for test11",
       "issuetype": {
          "name": "Task"
       }
   }
}
)
response=requests.post(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
data=response.json()
print(data["id"])



