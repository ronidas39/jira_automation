import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/user"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
with io.open("userlist.csv","r",encoding="utf-8")as f1:
    user_data=f1.read()
    f1.close()
user_data=user_data.split("\n")[1:]
for users in user_data:
    displayname=users.split(",")[0]
    pwd=users.split(",")[1]
    email=users.split(",")[2]
    name=users.split(",")[2]
    payload=json.dumps(
    {
    "password": pwd,
  "emailAddress": email,
  "displayName": displayname,
  "name": name
   }
   )
    response=requests.post(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
    print(response.text) 



''' payload=json.dumps(
    {
    "password": "test@1234",
  "emailAddress": "tesuser1@atlassian.com",
  "displayName": "test1 user1",
  "name": "test1user1"
}
)
response=requests.post(url,headers=headers,data=payload,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
print(response.text) '''



