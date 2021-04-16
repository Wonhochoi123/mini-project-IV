# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle
import numpy as np
app = Flask(__name__)
api = Api(app)


model = pickle.load( open( "RF_model3.sav", "rb" ) )
class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict(np.array([list(json_data.values())]))
        # we cannot send numpt array as a result
        return res.tolist() 
# assign endpoint
api.add_resource(Scoring, '/scoring')
if __name__ == '__main__':
    app.run(debug=True)