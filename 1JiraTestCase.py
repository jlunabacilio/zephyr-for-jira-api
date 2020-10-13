from jira import JIRA
import yaml
import requests
import json

conf = yaml.safe_load(open('conf/application.yml'))
user = conf['user']['username']
passwd = conf['user']['password']

options = {'server': 'https://pruebajira10.atlassian.net/'}
jira = JIRA(options, basic_auth=(user, passwd))

#Creating new issue
issue_dict = {
    'project': {'id': 10003},
    'summary': 'Test Case from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Test'},
}
new_issue = jira.create_issue(fields=issue_dict)
print('Issue created successfully')

#issue = jira.issue('ACM-1')
#nombre = issue.fields.summary
