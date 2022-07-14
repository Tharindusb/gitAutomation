import os
import warnings
from pprint import pprint
import requests
from dotenv import load_dotenv

load_dotenv()

warnings.filterwarnings("ignore")
filename = input("Enter the project name: ")
github_token = os.getenv("github_token")
api_url = 'https://api.github.com/'
projecrDir = os.getenv("projecrDir")
acount_url = os.getenv("acount_url")


def createDir(filename):
    
    lines = ['#ReadMe','##Test']

    payload = '{ "name":"%s"}'%filename
    header = {'Authorization': 'token '+ github_token ,'Accept': 'application/vnd.github+json'}

    r = requests.post(api_url+'user/repos',data=payload,headers=header)
    if not os.path.exists(f'{projecrDir}'):
        os.makedirs(f'{projecrDir}')


    init_commit = 'Initial commit'
    ssh_url = acount_url + '%s.git'%filename
    
    
    os.system(f"cd '{projecrDir}' && git clone '{ssh_url}' && cd '{filename}' && touch ReadMe.md && git add . && git commit -m '{init_commit}' && git push -u origin main")

    print("Directory '%s' created" % filename)

class gitAutomation:

    def __init__(self,create):
        self.create = create

creategit = gitAutomation(create = createDir)        
creategit.create(filename)


