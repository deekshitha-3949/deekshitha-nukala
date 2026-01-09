from flask import Flask,request,jsonify

app = Flask(__name__)

students = []
next_user_id=1

if __name__ =='__main__':
    app.run(debug = True)
    @app.route('/register_student', methods=['POST'])
    def register_student():
        username=request.json['username']
        password=request.json['password']
        email=request.json['email']
        global next_user_id
        student ={
            'user_id':next_user_id,
            'username':username,
            'password':password,
            'email':email
        }
        students.append(student)
        next_user_id +=1
        return jsonify({"message":"student register successfull"}),200
