import requests
import json
url="https://totaltechnology.atlassian.net/rest/api/2/users/search"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ronidas071@gmail.com","fdaLj3RlE9jhDVdaPwOzD4E6"))
data=response.json()
print(len(data))
for users in data:
    print(users["displayName"])
    



