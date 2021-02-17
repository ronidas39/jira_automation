import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-38/assignee"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload=json.dumps(
    {
    "accountId": "5ff7d2d91051d10075a65acb"
}
)
response=requests.put(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text)



