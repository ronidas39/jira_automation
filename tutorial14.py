import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-38/assignee"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
with io.open("issue_user.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
data=data.split("\n")
for row in data:
 issue_id=row.split(",")[0]
 user_id=row.split(",")[1]
    
 url="https://totaltechnology.atlassian.net/rest/api/3/issue/"+issue_id+"/assignee"
 payload=json.dumps(
    {
     "accountId": user_id
   }
 )
 response=requests.put(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
 print(response.text)