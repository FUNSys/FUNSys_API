from flask import Flask, jsonify
from FunsysModel import*


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# index
@app.route('/',methods=['GET'])
def index():
    return 'Connection was established\n'


# send all lectures [Error of ManyToMany]
@app.route('/lectures',methods=['GET'])
def lectures():
    ar = []
    try:
        for lecture in Lecture.select():
            data = {
                'lecture_id': lecture.lecture_id,
                'disp_lecture': lecture.disp_lecture,
                'must': lecture.must,
                'week': lecture.week,
                'jigen': lecture.jigen,
                # 'teachers': lecture.teachers,
                # 'rooms': lecture.rooms,
                # 'classes': lecture.classes,
            }
            ar.append(data)
    except Lecture.DoesNotExist:
        return 'DoesNotExist\n'
    return jsonify(ar)


# send single lecture [Error of ManyToMany]
@app.route('/lectures/<id>',methods=['GET'])
def single_lecture(id):
    try:
        lecture = Lecture.get(Lecture.lecture_id==id)
        data = {
            'lecture_id': lecture.lecture_id,
            'disp_lecture': lecture.disp_lecture,
            'must': lecture.must,
            'week': lecture.week,
            'jigen': lecture.jigen,
            # 'teachers': lecture.teachers,
            # 'rooms': lecture.rooms,
            # 'classes': lecture.classes,
        }
        return jsonify(data)
    except Lecture.DoesNotExist:
        return 'DoesNotExist\n'

# send all teacher [OK]
@app.route('/teachers',methods=['GET'])
def teachers():
    ar = []
    try:
        for teacher in Teacher.select():
            data = {
                'teacher_id': teacher.teacher_id,
                'disp_teacher': teacher.disp_teacher,
                'romen_name': teacher.roman_name,
                'position': teacher.position,
                'research_area': teacher.research_area,
                'role': teacher.role
            }
            ar.append(data)
        return jsonify(ar)
    except Teacher.DoesNotExist:
        return 'DoesNotExist\n'

# send single teacher [OK]
@app.route('/teachers/<id>',methods=['GET'])
def single_teacher(id):
    try:
        single_teacher = Teacher.get(Teacher.teacher_id==id)
        data = {
            'teacher_id': single_teacher.teacher_id,
            'disp_teacher': single_teacher.disp_teacher,
            'romen_name': single_teacher.roman_name,
            'position': single_teacher.position,
            'research_area': single_teacher.research_area,
            'role': single_teacher.role
        }
        return jsonify(data)
    except Teacher.DoesNotExist:
        return 'DoesNotExist\n'

# send all classes [OK]
@app.route('/classes',methods=['GET'])
def classes():
    ar = []
    try:
        for single_class in Class.select():
            data = {
                'class_id': single_class.class_id,
                'disp_class': single_class.disp_class,
                'course': single_class.course,
            }
            ar.append(data)
        return jsonify(ar)
    except Class.DoesNotExist:
        return 'DoesNotExist\n'


# send single class [OK]
@app.route('/classes/<id>',methods=['GET'])
def single_class(id):
    try:
        single_class = Class.get(Class.class_id==id)
        data = {
            'class_id': single_class.class_id,
            'disp_class': single_class.disp_class,
            'course': single_class.cource,
            }
        return jsonify(data)
    except Class.DoesNotExist:
        return 'DoesNotExist\n'


# send all rooms [OK]
@app.route('/rooms',methods=['GET'])
def rooms():
    ar = []
    try:
        for room in Room.select():
            data = {
                'room_id':room.room_id,
                'disp_room':room.disp_room
            }
            ar.append(data)
    except Room.DoesNotExist:
        return 'DoesNotExist\n'
    return jsonify(ar)

# send single room [OK]
@app.route('/rooms/<id>',methods=['GET'])
def single_room(id):
    try:
        room = Room.get(Room.room_id==id)
        data = {
            'room_id':room.room_id,
            'disp_room':room.disp_room
            }
        return jsonify(data)
    except Room.DoesNotExist:
        return 'DoesNotExist\n'


if __name__ == '__main__':
    app.run(debug=True)
