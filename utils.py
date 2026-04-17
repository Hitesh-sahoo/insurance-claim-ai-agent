import pdfplumber
import re

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_fields(text):
    data = {}

    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)

    
    policy_matches = re.findall(r'POLICY NUMBER[:\s]*([A-Z0-9-]{6,})', text, re.IGNORECASE)
    for p in policy_matches:
        if p not in ["CONTACT", "AGENCY", "INSURED"]:
            data["policy_number"] = p
            break

    
    date = re.search(r'DATE OF LOSS.*?(\d{2}/\d{2}/\d{4})', text, re.IGNORECASE)
    if date:
        data["date_of_loss"] = date.group(1)

    time = re.search(r'TIME.*?(\d{1,2}:\d{2}\s*(AM|PM))', text, re.IGNORECASE)
    if time:
        data["time"] = time.group(1)

    location = re.search(r'CITY[, ]+STATE[, ]+ZIP[:\s]*([A-Z\s]{5,})', text, re.IGNORECASE)
    if location:
        loc=location.group(1).strip()
        if "REPORT" not in loc and "COUNTRY" not in loc:
            data["location"]=loc

    desc = re.search(r'DESCRIPTION OF ACCIDENT[:\s]+(.+?)(?:VEH|DRIVER|OWNER)', text, re.IGNORECASE)
    if desc:
        clean_desc = desc.group(1).strip()
        if "ACORD 101" not in clean_desc:
            data["description"] = clean_desc


    if any(word in text.lower() for word in ["injury", "hospital", "medical"]):
        data["claim_type"] = "injury"
    else:
        data["claim_type"] = "damage"


    damage = re.search(r'ESTIMATE(?: AMOUNT)?[:\s]*\$?(\d+)', text, re.IGNORECASE)
    if damage:
        data["estimated_damage"] = float(damage.group(1))

    if "DRIVER" in text:
        data["involved_party"] = "Driver mentioned"
    
    if "description" not in data:
        data["description"] = "Not clearly mentioned in document"
    return data

def check_missing(data):
    required = [
        "policy_number",
        "claim_type",
        "estimated_damage",
        "date_of_loss",
        "description"
    ]
    return [f for f in required if f not in data]

def route_claim(data, missing, text):
    text_lower = text.lower()

    if missing:
        return "Manual Review"

    if any(word in text_lower for word in ["fraud", "staged", "inconsistent"]):
        return "Investigation"

    if data.get("claim_type") == "injury":
        return "Specialist Queue"

    if data.get("estimated_damage", 0) < 25000:
        return "Fast-track"

    return "Normal Processing"

def generate_reasoning(route, missing, data):
    if route == "Manual Review":
        return f"Missing required fields: {missing}"

    if route == "Investigation":
        return "Fraud-related keywords detected in description"

    if route == "Specialist Queue":
        return "Claim type is injury"

    if route == "Fast-track":
        return f"Estimated damage {data.get('estimated_damage')} is below threshold"

    return "Standard processing"