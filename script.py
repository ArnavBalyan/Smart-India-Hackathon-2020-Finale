from flask import Flask, Response, request
from flask import render_template, make_response
from flask_restful import Resource, Api
import numpy as np
import flask
import pickle
import json
import jsonify
from collections import OrderedDict

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

api = Api(app)
# api2 = Api(app)
def mdl1(txt1):
#     print('rcvtxt',txt1)
    ret = OrderedDict()
    org = txt1.split('$')
    hdr = ['model_id','room_id','no_of_occupants','indoor_temp','outdoor_temp','rel_hght_of_floor','ceiling_height','room_area','roof_material','humidity']
    for i in range(len(hdr)):
        ret[hdr[i]] = org[i]
    ls = txt1.split('$')[1:]
    roomid = ls[1]
    floorid = ls[4]
    ls = ls[1:]
    print(ls)
    to_predict = np.array(ls).reshape(1,8)
    print(to_predict)
    loaded_model = pickle.load(open("model1.pkl","rb"))
    result = loaded_model.predict(to_predict)
    ret['hvac_load'] = result[0]
    print(ret)
    lr = flask.jsonify(ret)
    return lr
#     return lr
    
    
def invalid(txt):
    return 'Bad Request'
class Dash(Resource):
    pass
class Display(Resource):

    def get(self, string1):
        txt = string1
        ids = txt[0]
        if(ids == '1'):
            return mdl1(txt)

        return invalid(txt)
        # headers = {'Content-Type': 'text/html'}
        # return{'text':'test'}
        # return make_response(render_template("result.html",result= "{}".format(string1)))

api.add_resource(Display, '/search/v1/<string:string1>')
api.add_resource(Dash, '/dash/v1/<string:string1>')  
if __name__ == '__main__':
    app.run()
