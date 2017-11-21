# -*- coding: utf-8 -*-
"""
モデルとは、サイトを構成するデータの、唯一絶対的なデータソースを指します。
モデルには、保存したいデータを表すデータフィールドと、データのビヘイビアを 定義します。
通常、一つのモデルは一つのデータベーステーブルに対応しています。
ORM(Object Relational Mapping オブジェクト関係マッピング)
利点:DBアクセスのためにSQLを1行も書かないこともできる。 
"""

from peewee import *
from playhouse.fields import ManyToManyField
from playhouse.db_url import connect
import os
# 環境変数の値を取得
url = os.getenv("FUNSYSDBURL", "mysql://user:user@localhost:3306/db")
# DBに接続
db = connect(url)

# データベース指定のための設定を格納したベースモデル
class BaseModel(Model):
    class Meta:
        database = db


class Teacher(BaseModel):
    # teacher_id,disp_teacher,roman_name,position,research_area,roleのカラムを持つ
    # データベースの指定は BaseModel を継承する形で行う
    teacher_id = PrimaryKeyField()
    disp_teacher = TextField()
    roman_name = TextField()
    position = TextField()
    research_area = TextField()
    role = TextField()

    def __repr__(self):
        return '<Teacher_Model id={0}, disp={1}, roman={2}, potision={3}, area={4}, role={5}>'.format(
            self.teacher_id, self.disp_teacher, self.roman_name, self.position, self.research_area, self.role)


class Room(BaseModel):
    room_id = PrimaryKeyField()
    disp_room = TextField()

    def __repr__(self):
        return '<Room_Model id={0}, disp={1}>'.format(
            self.room_id, self.disp_room)


class Class(BaseModel):
    class_id = IntegerField(primary_key=True)
    disp_class = TextField()
    course = IntegerField()

    def __repr__(self):
        return '<Class_Model id={0}, disp_class={1}, course={2}>'.format(
            self.class_id, self.disp_class, self.course)


class Lecture(BaseModel):
    lecture_id = PrimaryKeyField()
    disp_lecture = TextField()
    must = BooleanField()
    week = IntegerField()
    jigen = IntegerField()

    teachers = ManyToManyField(Teacher, related_name="lectures")
    rooms = ManyToManyField(Room, related_name="lectures")
    classes = ManyToManyField(Class, related_name="lectures")

    def __repr__(self):
        return '<Lecture_Model id={0}, disp={1}, must={2}, week={3}, jigen={4}, teachers={5}, rooms={6}, classes={7}>'.format(
            self.room_id, self.year, self.kumi, self.course, self.teachers, self.rooms, self.classes)


LectureTeacher = Lecture.teachers.get_through_model()
LectureRoom = Lecture.rooms.get_through_model()
LectureClass = Lecture.classes.get_through_model()


def InitializeDatabase():
    db.drop_tables([Teacher, Room, Class, Lecture,
                    LectureTeacher, LectureRoom, LectureClass], safe=True)
    db.create_tables([Teacher, Room, Class, Lecture,
                      LectureTeacher, LectureRoom, LectureClass], safe=True)
    db.commit()


if __name__ == '__main__':
    InitializeDatabase()
