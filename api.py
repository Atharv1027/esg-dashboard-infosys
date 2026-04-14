import requests

API_KEY = "YOUR_SMP_API_KEY"

BASE_URL = "https://api.marketintelligence.spglobal.com"

def get_esg_data(company="INFY"):
    endpoint = f"/esg/v1/companies/{company}"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(BASE_URL + endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

    except Exception as e:
        return {"error": str(e)}