import requests,json,io

base_url="https://ttyoutube.atlassian.net/rest/api/3/search"
user="thetotaltechnology@gmail.com"
pwd="ATATT3xFfGF0Wx1IssttLkQNWzoERUoiw2B8dr_R_pOgsTUCxRjGkC6LjJWndJkzTcadg_AxHzPP11pKpK2uv8toFgCKIMIyD90R_0k16J-8y_fOCQn7HZnMaBZuMVaSlahB5rjBxuMv__9zmTZN1rtMT8migMPgX8y8KTJOF37JKKDL8F_laAM=910E3098"
project_key="AUT"
headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}

api_url=f"{base_url}?jql=project={project_key}"
#to get the total number of issues

response=requests.get(api_url,auth=(user,pwd))
data=response.json()
total=data["total"]

#setup the pagionation
batch_size=100
nor=(total+batch_size-1)//batch_size
print(nor)

#looping
all=[]
for n in range(nor):
    s=n*batch_size
    query={
        "jql":"project=AUT",
        "startAt":s,
        "maxResults":batch_size
    }
    response=requests.get(base_url,headers=headers,params=query,auth=(user,pwd))
    data=response.json()
    issues=data.get("issues",[])
    all.extend(issues)
with io.open("results.csv","w",encoding="utf-8")as f1:
    for one in all:
        f1.write(one["id"]+","+one["key"]+"\n")
    f1.close()
