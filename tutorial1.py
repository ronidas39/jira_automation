import requests
import json
url="https://magdeline22.atlassian.net//rest/api/2/issue"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload=json.dumps(
    {
    "fields": {
       "project":
       {
          "key": "TJJ"
       },
       "summary": "creating for test",
       "description": "Created for test11",
       "issuetype": {
          "name": "Task"
       }
   }
}
)
response=requests.post(url,headers=headers,data=payload,
auth=("magdamabusela@gmail.com",
"ATATT3xFfGF0UzMaW1lfogT_YlLrM820oSsukcmfHPwZ0WRsK3wN2OmSed4h9zZv_NITHjePpZ-cm4KUK8n0HdsZCQoIUscYjbNpOwj0Inwh0GOy6tq2y8eReZTvdKxhTgmtUzEaT1PxOHbLI6Cn99qyTg0wkYMDkUMfm2dIfWRMx4ftOZFDFEQ=CA706B00"))
print(response.text)



