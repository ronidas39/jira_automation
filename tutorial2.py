import requests
import json
url="https://totaltechnology.atlassian.net/rest/api/2/users/search"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
data=response.json()
print(len(data))
print(data)
for users in data:
    print(users["displayName"])
    



