from flask import Flask, jsonify
from FunsysModel import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

# index


@app.route('/', methods=['GET'])
def index():
    return 'Connection was established'


# response
@app.route('/ping', methods=['GET'])
def ping():
    return 'Pong'


# send all lectures
@app.route('/lectures', methods=['GET'])
def lectures():
    query = Lecture.select()
    lectureshashed = []
    for lecture in query:
        data = {
            'lecture_id': lecture.lecture_id,
            'disp_lecture': lecture.disp_lecture,
            'must': lecture.must,
            'week': lecture.week,
            'jigen': lecture.jigen,
            'teachers': list(map(lambda y: y.teacher_id, lecture.teachers)),
            'rooms': list(map(lambda y: y.room_id, lecture.rooms)),
            'classes': list(map(lambda y: y.class_id, lecture.classes))
        }
        lectureshashed.append(data)
    return jsonify(lectureshashed)


# send single lecture
@app.route('/lectures/<id>', methods=['GET'])
def single_lecture(id):
    query = Lecture.get(Lecture.lecture_id == id)
    data = {
        'lecture_id': query.lecture_id,
        'disp_lecture': query.disp_lecture,
        'must': query.must,
        'week': query.week,
        'jigen': query.jigen,
        'teachers': list(map(lambda y: y.teacher_id, query.teachers)),
        'rooms': list(map(lambda y: y.room_id, query.rooms)),
        'classes': list(map(lambda y: y.class_id, query.classes)),
    }
    return jsonify(data)


# send all teacher
@app.route('/teachers', methods=['GET'])
def teachers():
    query = Teacher.select()
    teacherlist = []
    for teacher in query:
        data ={
            'teacher_id': teacher.teacher_id,
            'disp_teacher': teacher.disp_teacher,
            'romen_name': teacher.roman_name,
            'position': teacher.position,
            'research_area': teacher.research_area,
            'role': teacher.role
        }
        teacherlist.append(data)
    return jsonify(teacherlist)


# send single teacher
@app.route('/teachers/<id>', methods=['GET'])
def single_teacher(id):
    single_teacher = Teacher.get(Teacher.teacher_id == id)
    data = {
        'teacher_id': single_teacher.teacher_id,
        'disp_teacher': single_teacher.disp_teacher,
        'romen_name': single_teacher.roman_name,
        'position': single_teacher.position,
        'research_area': single_teacher.research_area,
        'role': single_teacher.role
    }
    return jsonify(data)


# send all classes
@app.route('/classes', methods=['GET'])
def classes():
    query = Class.select()
    classlist = []
    for singleclass in query:
        data = {
            'class_id': singleclass.class_id,
            'disp_class': singleclass.disp_class,
            'course': singleclass.course
        }
        classlist.append(data)
    return jsonify(classlist)

# send single class


@app.route('/classes/<id>', methods=['GET'])
def single_class(id):
    query = Class.get(Class.class_id == id)
    data = {
        'class_id': query.class_id,
        'disp_class': query.disp_class,
        'course': query.course
    }
    return jsonify(data)

# send all rooms


@app.route('/rooms', methods=['GET'])
def rooms():
    query = Room.select()
    roomslist = []
    for room in query:
        data = {
            'room_id': room.room_id, 
            'disp_room': room.disp_room
        }
        roomslist.append(data)
    return jsonify(roomslist)

# send single room


@app.route('/rooms/<id>', methods=['GET'])
def single_room(id):
    room = Room.get(Room.room_id == id)
    data = {
        'room_id': room.room_id,
        'disp_room': room.disp_room
    }
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run()
