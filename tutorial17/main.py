import requests,json

base_url="https://ttyoutube.atlassian.net/rest/api/3/search"
user="thetotaltechnology@gmail.com"
pwd="ATATT3xFfGF04Xs9SBXzMwS3WBBmZXp1mHD0-RCspB2J9uhHTiZMycFek-TmVqpmfEmSmqg4vRApC8CUSQTDVGce6cvifCvaGWv_Y4PDzLY_rm0m5AwxNiAhAorIg_fYkYDfg3cveORMIDkSXEp9kS7fdfjtCTlV-wP8E-MmoV2BTlGk_xYoBZg=EA27AA78"
headers={
    "Accept":"application/json",
    "Content":"application/json",
}
api_url=f"{base_url}?jql=assignee='RONI DAS'"
response=requests.get(api_url,headers=headers,auth=(user,pwd))
issues=response.json()["issues"]
for issue in issues:
    print(issue["key"],issue["fields"]["summary"])