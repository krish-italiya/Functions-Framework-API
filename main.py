import json
import functions_framework
from flask_cors import cross_origin
import plots
import matplotlib
matplotlib.use("Agg")



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
        return json.dumps({"response": "Invalid Query :(", "plot_detail": img_data}), 200
    except Exception as e:
        return {"error": str(e)}, 500
