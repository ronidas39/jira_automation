import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-37/transitions"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload=json.dumps(
   {
    "transition": {
        "id": "31"
    }
}
 )
response=requests.post(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text)