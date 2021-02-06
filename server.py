import tensorflow as tf
import numpy as np
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/tpdne/classify/')
def ingest_since(unixepoch):
    """Classifies TPDNE images as real or fake
    ---
    tags: [SomeTag]
    consumes: [multipart/form-data]
    parameters:
        - name: file
          in: formData
          required: true
          type: file
          description: The file you want to store
    """

    return jsonify({"test": "success"})

app.run(debug=False)