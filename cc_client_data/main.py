from flask import Flask, render_template
from dotenv import dotenv_values
import requests
import urllib3

urllib3.disable_warnings()

env = dotenv_values(".env")
CC_ADDRESS = env["CC_ADDRESS"]
CC_USERNAME = env["CC_USERNAME"]
CC_PASSWORD = env["CC_PASSWORD"]

app = Flask(__name__)

@app.route("/")
def client_dashboard():
    token = get_cc_token(CC_ADDRESS, CC_USERNAME, CC_PASSWORD)
    client_data = get_clients(token, CC_ADDRESS)
    return render_template("index.html", client_data=client_data)

def get_cc_token(cc_address:str, username:str, password:str):
    token = ""
    url = f"https://{cc_address}/dna/system/api/v1/auth/token"
    response = requests.post(url, auth=(username, password), verify=False)
    print("Token status: ", response.status_code)
    
    if response.ok:
        response_json=response.json()
        token = response_json["Token"]
        print("Token generated")
    
    return token

def get_clients(token:str, cc_address:str):
    clients = []
    url = f"https://{cc_address}/dna/data/api/v1/clients"

    header = {
        "content-type": "application/json",
        "x-auth-token": token
    }

    response= requests.get(url, headers=header, verify=False)
    print("Client retrieval status: ", response.status_code)
    
    if response.ok:
        response_json=response.json()
        clients = response_json["response"]
        print("clients retrieved")
    return clients
