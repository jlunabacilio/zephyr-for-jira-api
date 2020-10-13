import requests
import json
import yaml
#Hide Zephyr api key and JWT key
conf = yaml.safe_load(open('conf/application.yml'))
Authorization = conf['headers']['Authorization']
Authorization1 = conf['headers']['Authorization1']
zapiAccessKey = conf['headers']['zapiAccessKey']
#New execution endpoint
url_execution = "https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/execution"
#Update execution endpoint
url_update = "https://prod-api.zephyr4jiracloud.com/connect/public/rest/api/1.0/execution/-1"
#Execution headers
headers_execution = {
  'Content-Type': 'application/json',
  'Authorization': Authorization,
  'zapiAccessKey': zapiAccessKey
}
#Execution headers to update
headers_update = {
  'Content-Type': 'application/json',
  'Authorization': Authorization1,
  'zapiAccessKey': zapiAccessKey
}
#Execution body
body_execution = {
    "id": "-1",
    "projectId": 10003,
    "issueId": 10134,
    "cycleId": "-1",
    "versionId": 10003
}
#Execution body to update
body_update = {
    "status": {"id":1},
    "id": "-1",
    "projectId": 10003,
    "issueId": 10134,
    "cycleId": "-1",
    "versionId": 10003
}

response_execution = requests.request(
   "POST",
   url_execution,
   headers=headers_execution
)

response_update = requests.request(
   "PUT",
   url_execution,
   headers=headers_execution
)

r = requests.post(url_execution, headers=headers_execution ,json=body_execution)
print(r)
print("Test Execution Created successfully")
s = requests.put(url_update, headers=headers_update ,json=body_update)
print(s)
print("Test Execution Updated successfully")
