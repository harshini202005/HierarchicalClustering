import os
from flask import Flask, render_template, request
from hierarchical import generate_cluster_plots

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    clusters = int(request.form['clusters'])
    generate_cluster_plots(clusters)
    return render_template('result.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
