from flask import Flask, jsonify, request
from flask_cors import CORS
import threading
from src.TreeGeneration.treegen import build_reg_tree, explore_new_node
from src.Models.articlenode import ArticleNode

app = Flask("Causalitree")
CORS(app)  # Allow requests from the frontend

roots = []

@app.after_request
def add_csp_header(response):
    response.headers['Content-Security-Policy'] = "script-src 'self' 'nonce-diddy'"
    return response

@app.route('/api/prevents', methods=['GET'])
def get_prevents():
    query = request.args.get('q')
    predecessors = roots[-1].find_predecessors_2(query)
    combined = {"nodes": []}
    for node in predecessors:
        combined["nodes"].append(node.to_client())
        thread = threading.Thread(target=node.get_new_preds())
        thread.start()

    return jsonify(combined), 200


@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    if len(roots) == 0:
        return jsonify({"error": "No JSON received"}), 400
    
    if len(roots) > 0:
        print("woowwowowo:", roots[0].title)
    if roots[0].title is None and len(roots[0].predecessors) > 0:
        print("Root is None")
        newRoot = roots[0].predecessors[0]
        newRoot.sucessors = []
        roots[0] = newRoot
    
    combined = {"nodes": []}
    
    queue = [roots[-1]]

    while len(queue) > 0:
        node = queue.pop()
        combined["nodes"].append(node.to_client())
        queue += node.predecessors

    return jsonify(combined), 200


@app.route('/api/nodes', methods=['POST'])
def explore_url():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400
    
    url_from_request = data.get('url')

    print("URL FROM REQUEST: ", url_from_request)

    explore_new_node(url_from_request, roots)

    return jsonify({"message": "Data received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)