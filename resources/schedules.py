from flask_restful import Resource,reqparse
#from werkzeug.security import safe_str_cmp
#from flask_jwt_extended import create_access_token,jwt_required
from db import query

class schedule(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('schedule_id',type=int,required=True,help="Schedule id cannot be left blank!")
        parser.add_argument('sport_id',type=int,required=True,help="Sport id cannot be left blank!")
        parser.add_argument('team1_id',type=int,required=True,help="Team 1 id cannot be left blank!")
        parser.add_argument('team2_id',type=int,required=True,help="Team 2 id cannot be left blank!")
        parser.add_argument('start_timing',type=str,required=True,help="Start time cannot be left blank!")
        parser.add_argument('end_timing',type=str,required=True,help="End time cannot be left blank!")
        parser.add_argument('title',type=str,required=True,help="Team Status cannot be left blank!")
        parser.add_argument('date',type=str,required=True,help="Date cannot be left blank")
        data=parser.parse_args()
        try:
            x=query(f"""SELECT * FROM group10.schedule WHERE schedule_id={data['schedule_id']}""",return_json=False)
            if len(x)>0: return {"message":"A Schedule with that Id already exists."},400
        except:
            return {"message":"There was an error inserting into Schedule table."},500
        if data['schedule_id']!=None:
            try:
                query(f"""INSERT INTO group10.schedule (schedule_id,sport_id,team1_id,team2_id,start_timing,end_timing,Date,title)
                                                VALUES({data['schedule_id']},
                                                    {data['sport_id']},
                                                    {data['team1_id']},
                                                    {data['team2_id']},
                                                    '{data['start_timing']}',
                                                    '{data['end_timing']}',
                                                    '{data['title']}',
                                                    '{data['date']}')""")

            except:
                return {"message":"There was an error inserting into table."},500
            return {"message":"Successfully Inserted."},201
#class adminlogin(Resource):
#    def post(self):
#        parser.add_argument('admin_id',type=int,required=True,help="Admin ID cannot be left blank!")
#        parser.add_argument('password',type=str,required=True,help="Password cannot be left blank!")
#        data=parser.parse_args()
#            access_token=create_access_token(identity=user.admin_id,expires_delta=False)
#            return {'access_token':access_token},200
#        return {"message":"Invalid Credentials!"}, 401
