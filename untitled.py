from flask import Flask, jsonify

app = Flask(__name__)


class Lecture_front:
    def __init__(self):
        self.lecture_id = 1
        self.disp_lecture = ""
        self.must = True
        self.week = 1
        self.jigen = 1
        self.teachers = [123, 456]
        self.rooms = [123, 234]
        self.classes = [12, 34]


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
    a = Lecture_front()
    b = Lecture_front()
    # レクチャーフロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = [a, b]
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
    a = Room_front()
    b = Room_front()
    # フロントクラスの配列を作る
    # 配列の1つ目と2つ目にインスタンスを入れる
    ar = [a, b]
    return jsonify(ar)  # 配列をjsonifyの中に入れる


if __name__ == '__main__':
    app.run()
