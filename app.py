import os
from flask import Flask, render_template, request, jsonify
from serpapi import GoogleSearch

app = Flask(__name__)

TIER_3_CITIES = [
    "Udaipur", "Jhansi", "Madurai", "Aligarh", "Guntur",
    "Warangal", "Tirunelveli", "Nellore", "Rajahmundry", "Kurnool", "Darbhanga", "Madhubani",
    "Bikaner", "Amravati"
]

def construct_query(platform, city, keywords="admissions"):
    base_query = '("Principal" OR "Director") "{}" "{}"'.format(city, keywords)
    if platform == "LinkedIn":
        return f'site:linkedin.com/in {base_query}'
    elif platform == "Facebook":
        return f'site:facebook.com {base_query}'
    elif platform == "Instagram":
        return f'site:instagram.com {base_query}'
    return base_query

def fetch_results(query, num_results=100):
    results_data = []
    api_key = os.environ.get('SERPAPI_KEY')

    if not api_key:
        return {"error": "SERPAPI_KEY not found in environment variables."}

    params = {
        "q": query,
        "engine": "google",
        "api_key": api_key,
        "num": num_results # SerpApi allows up to 100 per credit
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        if "error" in results:
             return {"error": f"SerpApi Error: {results['error']}"}

        for result in results.get("organic_results", []):
            results_data.append({
                "Title": result.get("title"),
                "URL": result.get("link"),
                "Description": result.get("snippet")
            })
    except Exception as e:
        return {"error": str(e)}

    return results_data

@app.route('/')
def index():
    return render_template('index.html', cities=TIER_3_CITIES)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    platform = data.get('platform')
    city = data.get('city')
    keywords = data.get('keywords', 'admissions')
    # Capture num_results from the frontend, default to 100
    num_results = int(data.get('num_results', 100))

    if not platform or not city:
        return jsonify({"error": "Platform and City are required."}), 400

    query = construct_query(platform, city, keywords)
    results = fetch_results(query, num_results)

    if isinstance(results, dict) and "error" in results:
        return jsonify(results), 500

    return jsonify({"results": results})
