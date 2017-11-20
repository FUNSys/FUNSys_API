from flask import Flask, jsonify

app = Flask(__name__)


class Lecture_front:
    def __init__(self,lecture_id,disp_lecture,must,week,jigen,teachers,rooms,classes):
        self.lecture_id = lecture_id
        self.disp_lecture = disp_lecture
        self.must = must
        self.week = week
        self.jigen = jigen
        self.teachers = teachers
        self.rooms = rooms # [123, 234]
        self.classes = classes # [12, 34]

    def return_json(self):
        data = {
            'lecture_id':self.lecture_id,
            'disp_lecture':self.disp_lecture,
            'must':self.must,
            'week':self.week,
            'jigen': self.jigen,
            'teachers': self.teachers,
            'rooms': self.rooms,
            'classes': self.classes,

        }
        return data

class Teacher_front:
    def __init__(self):
        self.teachers_id = 1
        self.disp_teacher = ""
        self.research_area = ""
        self.course = 1


class Room_front:
    def __init__(self):
        self.room_id = 1
        self.disp_room = ""


class Class_front:
    def __init__(self):
        self.class_id = 1
        self.year = 1
        self.kumi = "A"
        self.course = 1


@app.route('/ping')
def ping():
    return 'Pong'


@app.route('/lectures')
def lectures():
    # レクチャーフロントクラスのインスタンスを二つ作る
    # 引数は講義ID,講義名,必修/選択,週,時限,先生s,部屋s,クラス
    lecture_id = 0
    disp_lecture = '線型代数学'
    must = True
    week = '月'
    jigen = '1'
    teachers = ['由良','香取']
    rooms  = ['123', '234','R791']
    classes = ['A', 'B', 'C', 'D']
    a = Lecture_front(lecture_id,disp_lecture,must,week,jigen,teachers,rooms,classes)
    # レクチャーフロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = []
    ar.append(a.return_json())
    return jsonify(ar)
    # 配列をjsonifyの中に入れる


@app.route('/lectures/{id}')
def lecturesaa(id):
    # レクチャーフロントクラスのインスタンスを作る
    a = Lecture_front()
    return jsonify(a)  # 配列をjsonifyの中に入れる


@app.route('/teachers')
def teachers():
    # フロントクラスのインスタンスを二つ作る
    a = Teacher_front()
    b = Teacher_front()
    # フロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = [a, b]
    return jsonify(ar)  # 配列をjsonifyの中に入れる


@app.route('/classes')
def classes():
    # フロントクラスのインスタンスを二つ作る
    a = Class_front()
    b = Class_front()
    # フロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = [a, b]
    return jsonify(ar)  # 配列をjsonifyの中に入れる


@app.route('/rooms')
def rooms():
    # フロントクラスのインスタンスを二つ作る
    # 引数は講義ID,講義名,必修/選択,週,時限,先生s,部屋s,クラス
    a = Room_front()
    b = Room_front()
    # フロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = [a, b]
    return jsonify(ar)  # 配列をjsonifyの中に入れる


if __name__ == '__main__':
    app.run()
