from flask import Flask
from flask_restful import Api
from resources.schedules import schedule

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['PREFERRED_URL_SCHEME']='http'
api=Api(app)

api.add_resource(schedule,'/sch')

if __name__ == "__main__":
    app.run(port="8055",debug=True)
