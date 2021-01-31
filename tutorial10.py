import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-4/comment/10009"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}


response=requests.delete(url,headers=headers,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text)





