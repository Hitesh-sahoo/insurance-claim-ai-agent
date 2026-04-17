from utils import extract_text, extract_fields, check_missing, route_claim, generate_reasoning
import json

def run_pipeline(file):
    text = extract_text(file)

    data = extract_fields(text)
    missing = check_missing(data)

    route = route_claim(data, missing, text)
    reason = generate_reasoning(route, missing, data)

    result = {
        "extractedFields": data,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

    with open("result.json", "w") as f:
        json.dump(result, f, indent=4)

    return result


if __name__ == "__main__":
    output = run_pipeline("sample.pdf")
    print(output)