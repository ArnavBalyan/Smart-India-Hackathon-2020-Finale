from flask import Flask, Response, request
from flask import render_template, make_response
from flask_restful import Resource, Api
import numpy as np
import flask
import pickle

app = Flask(__name__)
api = Api(app)
# api2 = Api(app)
def mdl1(txt1):
#     print('rcvtxt',txt1)
    ls = txt1.split('$')[1:]
    roomid = ls[1]
    floorid = ls[4]
    ls = ls[1:]
    print(ls)
    to_predict = np.array(ls).reshape(1,8)
    print(to_predict)
    loaded_model = pickle.load(open("model1.pkl","rb"))
    result = loaded_model.predict(to_predict)
    print(result)
    return result[0]
    
    
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
