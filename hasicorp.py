import requests
import os

ORGANIZATION_ID = os.environ.get("ORGANIZATION_ID")
PROJECT_ID = os.environ.get('PROJECT_ID')
 
def get_hcp_token():
    HCP_CLIENT_ID = os.environ.get("HCP_CLIENT_ID")
    HCP_CLIENT_SECRET = os.environ.get("HCP_CLIENT_SECRET")


    # Obtain an access token
    url = "https://auth.idp.hashicorp.com/oauth2/token"
    payload = {
        'client_id': HCP_CLIENT_ID,
        'client_secret': HCP_CLIENT_SECRET,
        'grant_type': 'client_credentials',
        'audience': 'https://api.hashicorp.cloud'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)

    HCP_API_TOKEN = response.json().get('access_token')
    return HCP_API_TOKEN

def app_vault_creation(key_valut_name):
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps"
    payload = {'name': key_valut_name}
    bearer_token = get_hcp_token()
    
    headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'  
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return "App valut created successfully"
    else:
        return response.text    

def secret_creation(key_valut_name,secret_name,secret_value):
    
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps/{key_valut_name}/kv"
    payload = {'name': secret_name, 'value': secret_value}
    print(url)
    bearer_token = get_hcp_token()
    
    headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'  # Assuming you're sending JSON data
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return f"secret sucessfully created in {key_valut_name} app"
    else:
        return response.text
    
def get_secret_value(key_vault_name,secret_name):
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps/{key_vault_name}/open/{secret_name}"
    bearer_token = get_hcp_token()
    
    headers = {
    'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.get(url, headers=headers)
    print(response.json())
    print(response.json().get('secret', {}).get('version', {}).get('value', None))
    return response.json().get('secret', {}).get('version', {}).get('value', None)
    
def delete_keyvalut_app(key_vault_name):
    urllist = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps/{key_vault_name}/secrets"
    bearer_token = get_hcp_token()
    headers = {
    'Authorization': f'Bearer {bearer_token}'
    }
    respose=requests.get(urllist,headers=headers)
    respose=respose.json()
    for res in respose['secrets']:
        delete_keyvalut_secret(key_vault_name,res.get('name'))
        print(res.get('name'))
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps/{key_vault_name}"
    bearer_token = get_hcp_token()
    
    headers = {
    'Authorization': f'Bearer {bearer_token}'
    }
    requests.delete(url,headers=headers)


def delete_keyvalut_secret(key_vault_name,secret_name):
    
    url = f"https://api.cloud.hashicorp.com/secrets/2023-06-13/organizations/{ORGANIZATION_ID}/projects/{PROJECT_ID}/apps/{key_vault_name}/secrets/{secret_name}"

    bearer_token = get_hcp_token()
    
    headers = {
    'Authorization': f'Bearer {bearer_token}'
    }
    requests.delete(url, headers=headers)
