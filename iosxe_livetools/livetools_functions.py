import requests
import urllib3

urllib3.disable_warnings()

HEADERS = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
}

def ping_action(host:str, username:str, password:str, target_ip:str)->int:

    base_url = f"https://{host}:443/restconf"
    action_url = f"{base_url}/operations/Cisco-IOS-XE-livetools-actions-rpc:ip-ping-action"
    body = {
        "count": 3,
        "host-ip":target_ip
    }
    auth = (username, password)
    response = requests.post(action_url, headers=HEADERS, json=body, auth=auth, verify=False)
    print(f"Request status code: {response.status_code}")
    
    if response.ok:
        return response.json()["Cisco-IOS-XE-livetools-actions-rpc:output"]["job-id"]
    else:
        return None

def traceroute_action(host:str, username:str, password:str, target_ip:str="10.128.128.5")->int:
    base_url = f"https://{host}:443/restconf"
    action_url = f"{base_url}/operations/Cisco-IOS-XE-livetools-actions-rpc:ip-tracert-action"
    body = {
        "host-ip":target_ip
    }
    auth = (username, password)

    response = requests.post(action_url, headers=HEADERS, json=body, auth=auth, verify=False)
    print(f"Request status code: {response.status_code}")

    if response.ok:
        return response.json()["Cisco-IOS-XE-livetools-actions-rpc:output"]["job-id"]
    else:
        return None

def traceroute_results(host:str, username:str, password:str, job_id:int=None):

    base_url = f"https://{host}:443/restconf"
    result_url = f"{base_url}/data/Cisco-IOS-XE-livetools-oper:livetools-oper-data/tracert-result"
    auth = (username, password)

    response = requests.get(f"{result_url}{f'={job_id}' if job_id else ''}", headers=HEADERS, auth=auth, verify=False)
    if response.ok:
        return response.json().get("Cisco-IOS-XE-livetools-oper:tracert-result")
    else:
        return None

def ping_results(host:str, username:str, password:str, job_id:int=None)->list:

    base_url = f"https://{host}:443/restconf"
    result_url = f"{base_url}/data/Cisco-IOS-XE-livetools-oper:livetools-oper-data/ip-ping-result"
    auth = (username, password)

    response = requests.get(f"{result_url}{f'={job_id}' if job_id else ''}", headers=HEADERS, auth=auth, verify=False)
    if response.ok:
        return response.json().get("Cisco-IOS-XE-livetools-oper:ip-ping-result")
    else:
        return None