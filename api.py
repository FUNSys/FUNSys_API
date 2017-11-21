from flask import Flask, jsonify
from FunsysModel import*

app = Flask(__name__)
# index
@app.route('/',methods=['GET'])
def index():
    return 'Connection was established'

# response
@app.route('/ping',methods=['GET'])
def ping():
    return 'Pong'

# send all lectures
@app.route('/lectures',methods=['GET'])
def lectures():
    ar = []
    for lecture in Lecture.select():
        data = {
            'lecture_id': lecture.lecture_id,
            'disp_lecture': lecture.disp_lecture,
            'must': lecture.must,
            'week': lecture.week,
            'jigen': lecture.jigen,
            'teachers': lecture.teachers,
            'rooms': lecture.rooms,
            'classes': lecture.classes,
        }
        ar.append(data)
    return jsonify(ar)

# send single lecture
@app.route('/lectures/{id}',methods=['GET'])
def single_lecture(id):
    lecture = Lecture.select().where(lecture_id=id)
    data = {
        'lecture_id': lecture.lecture_id,
        'disp_lecture': lecture.disp_lecture,
        'must': lecture.must,
        'week': lecture.week,
        'jigen': lecture.jigen,
        'teachers': lecture.teachers,
        'rooms': lecture.rooms,
        'classes': lecture.classes,
    }
    return jsonify(data)

# send all teacher
@app.route('/teachers',methods=['GET'])
def teachers():
    ar = []
    for teacher in Teacher.select():
        data = {
                'teacher_id': teacher.teacher_id,
                'disp_teacher': teacher.disp_teacher,
                'romen_name': teacher.roman_name,
                'position': teacher.position,
                'research_area': teacher.research_area,
                'role': teacher.role
        }
        ar.appeend(data)
    return jsonify(ar)

# send all classes
@app.route('/classes',methods=['GET'])
def classes():
    ar = []
    for single_class in Class.select():
        data = {
            'class_id': single_class.class_id,
            'disp_class': single_class.disp_class,
            'course': single_class.cource,
        }
    ar.append(data)
    return(ar)

# send single class
@app.route('/classes/{id}',methods=['GET'])
def single_class(id):
    single_class = Class.select().where(class_id=id)
    data = {
        'class_id': single_class.class_id,
        'disp_class': single_class.disp_class,
        'course': single_class.cource,
        }
    return jsonify(data)

# send all rooms
@app.route('/rooms',methods=['GET'])
def rooms():
    ar = []
    for room in Room.select():
        data = {
            'room_id':room.room_id,
            'disp_room':room.disp_room
        }
    ar.append(data)
    return (ar)

# send single room
@app.route('/rooms/{id}',methods=['GET'])
def single_room(id):
    room = Room.select().where(room_id=id)
    data = {
        'room_id':room.room_id,
        'disp_room':room.disp_room
        }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
