import requests
from base64 import b64encode
import pandas as pd

# Please set actual Personal Autentication Token
pat = "***"

# Please set actual parameters there for Azure Devops
api_version = "api-version=6.0"
organization = "myOrganization"
project = "myProject"
team = "myProjectTeam"

# Class for set Authorization header for requests module
class BasicAuthToken(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token


    def __call__(self, r):
        authstr = 'Basic ' + \
            b64encode(('token:' + self.token).encode('utf-8')).decode('utf-8')
        r.headers['Authorization'] = authstr
        return r

def rest_all_repos2list(organization,project):

    rest_url = f"https://dev.azure.com/{organization}/{project}/_apis/git/repositories?{api_version}"
    response = requests.get(rest_url, auth=BasicAuthToken(pat))
    
    repos_list = []

    #Get repository name fron response
    for response_dict in response.json()["value"]:
     for attribute, value in response_dict.items():
         if attribute == "name":
            repos_list.append(value)
    return repos_list


#For example: print repos list to console output
list = rest_all_repos2list(organization,project)
for item in sorted(list):
    print(item)