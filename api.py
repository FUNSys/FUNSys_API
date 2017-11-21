from flask import Flask, jsonify
from FunsysModel import*

app = Flask(__name__)

@app.route('/')
def index():
    return 'Connection was established'


@app.route('/ping',methods=['POST'])
def ping():
    return 'Pong'


@app.route('/lectures',methods=['POST'])
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


@app.route('/lectures/{id}',methods=['POST'])
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


@app.route('/teachers',methods=['POST'])
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


@app.route('/classes',methods=['POST'])
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


@app.route('/rooms',methods=['POST'])
def rooms():
    ar = []
    for room in Room.select():
        data = {
            'room_id':room.room_id,
            'disp_room':room.disp_room
        }
    ar.append(data)
    return (ar)

if __name__ == '__main__':
    app.run()
