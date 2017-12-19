from flask import Flask, jsonify
from FunsysModel import *
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, '')
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False


# send all lectures
@app.route('/lectures', methods=['GET'])
def get_all_lectures():
    query = Lecture.select()
    lecture_dict_list = list(
        map(lambda x: {
            'lecture_id': x.lecture_id,
            'disp_lecture': x.disp_lecture,
            'must': x.must,
            'week': x.week,
            'jigen': x.jigen,
            'teachers': list(map(lambda y: y.teacher_id, x.teachers)),
            'rooms': list(map(lambda y: y.room_id, x.rooms)),
            'classes': list(map(lambda y: y.class_id, x.classes)),
        }, query))
    return jsonify(lecture_dict_list)


# send single lecture
@app.route('/lectures/<id>', methods=['GET'])
def get_single_lecture(id):
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
def get_all_teachers():
    query = Teacher.select()
    teacherlist = list(
        map(lambda x: {
            'teacher_id': x.teacher_id,
            'disp_teacher': x.disp_teacher,
            'romen_name': x.roman_name,
            'position': x.position,
            'research_area': x.research_area,
            'role': x.role
        }, query)
    )
    return jsonify(teacherlist)


# send single teacher
@app.route('/teachers/<id>', methods=['GET'])
def get_single_teacher(id):
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
def get_all_classes():
    query = Class.select()
    class_dict_list = list(
        map(lambda x: {
            'class_id': x.class_id,
            'disp_class': x.disp_class,
            'course': x.course,
        }, query)
    )
    return jsonify(class_dict_list)


# send single class
@app.route('/classes/<id>', methods=['GET'])
def get_single_class(id):
    query = Class.get(Class.class_id == id)
    data = {
        'class_id': query.class_id,
        'disp_class': query.disp_class,
        'course': query.course,
    }
    return jsonify(data)


# send all rooms
@app.route('/rooms', methods=['GET'])
def get_all_rooms():
    query = Room.select()
    room_dict_list = list(
        map(lambda x: {'room_id': x.room_id, 'disp_room': x.disp_room}, query))
    return jsonify(room_dict_list)


# send single room
@app.route('/rooms/<id>', methods=['GET'])
def get_single_room(id):
    room = Room.get(Room.room_id == id)
    data = {
        'room_id': room.room_id,
        'disp_room': room.disp_room
    }
    return jsonify(data)


@app.route('/musts')
def get_all_musts():
    lines = []
    with open(os.path.join(APP_STATIC, 'must_data.txt')) as f:
        for line in f:
            x = line.split(',')
            must_list = {
                    'must_id': x[0],
                    'ict': x[1],
                    'system': x[2],
                    'design': x[3],
                    'complex': x[4],
                    'intelligent': x[5],
                    'unassign': x[6]
            }
            lines.append(must_list)
    return jsonify(lines)


@app.route('/musts/<id>')
def get_single_must(id):
    with open(os.path.join(APP_STATIC, 'must_data.txt')) as f:
        for line in f:
            x = line.split(',')
            if x[0] in str(id):
                must_list = {
                        'must_id': x[0],
                        'ict': x[1],
                        'system': x[2],
                        'design': x[3],
                        'complex': x[4],
                        'intelligent': x[5],
                        'unassign': x[6]
                }
                return jsonify(must_list)


if __name__ == '__main__':
    app.run()
