#import tensorflow as tf
#import numpy as np
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/tpdne/classify', methods=["POST"])
def tpdne(file):
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
    responses:
      200:
        description: Samples were ingested successfully
        schema:
          $ref: '#/definitions/classify_result'
        examples:
          rgb: ['red', 'green', 'blue']
    """

    #return jsonify({: "success"})
    #print(file)
    return "success"

app.run(debug=True, host = '0.0.0.0')
