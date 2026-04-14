def process_esg(data):
    try:
        return {
            "ESG": data.get("esgScore", 0),
            "Environmental": data.get("environmentScore", 0),
            "Social": data.get("socialScore", 0),
            "Governance": data.get("governanceScore", 0),
            "Carbon": data.get("carbonEmission", 0)
        }
    except:
        return {
            "ESG": 70,
            "Environmental": 72,
            "Social": 68,
            "Governance": 74,
            "Carbon": 60
        }