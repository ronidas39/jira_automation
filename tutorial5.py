import requests
import json
import io
url="https://totaltechnology.atlassian.net/rest/api/3/issue/TTS-4/comment"
headers={
  "Accept": "application/json",
    "Content-Type": "application/json"
}
response=requests.get(url,headers=headers,auth=("ronidas071@gmail.com","wg5OpdxcSbGvlykzUhm5C939"))
data=response.json()
#gives the comment counts
print(data["total"])
with io.open("comments.csv","w",encoding="utf-8") as f1:
 f1.write("comment id"+","+"comment text"+"\n")
 for comments in data["comments"]:
    f1.write(comments["id"]+","+comments["body"]["content"][0]["content"][0]["text"]+"\n")
 f1.close()
