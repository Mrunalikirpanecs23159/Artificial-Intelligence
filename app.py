from flask import Flask, render_template
from resources import create_resource_graph
from allocator import heuristic_allocate

app = Flask(__name__)

@app.route("/")
def home():

    graph = create_resource_graph()
    allocations = heuristic_allocate(graph)

    return render_template("index.html", allocations=allocations)

if __name__ == "__main__":
    app.run(debug=True)