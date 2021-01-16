import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-2/attachments"
headers={
    "X-Atlassian-Token": "no-check"
}
files={
    "file":("userlist.csv",open("userlist.csv","rb"))
}

response=requests.post(url,headers=headers,files=files,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text) 