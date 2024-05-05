import json
import functions_framework
import os
import google.generativeai as genai
from dotenv import load_dotenv
from flask_cors import cross_origin
import plots
import matplotlib
matplotlib.use("Agg")

load_dotenv()
GOOGLE_API_KEY = os.getenv("API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")


@cross_origin(allow_methods=["POST"])
@functions_framework.http
def get_query_response(request):
    try:
        data = request.get_json()
        user_query = data["query"]
        features, relations = plots.parseQuery(user_query)
        print(features, relations)
        img_data = plots.getPlot(features, relations)
        print(img_data)
        response = model.generate_content(user_query)
        return json.dumps({"response": response.text, "plot_detail": img_data}), 200
    except Exception as e:
        return {"error": str(e)}, 500
