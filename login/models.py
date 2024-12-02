import bcrypt
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['Shift-Start-db']

class User:
    collection = db['users']

    @staticmethod
    def create_user(data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        User.collection.insert_one(data)  # إضافة المستخدم إلى collection
        return data  # هنا نقوم بإرجاع البيانات المُدخلة

    @staticmethod
    def get_user_by_email(email):
        return User.collection.find_one({"email": email})

    @staticmethod
    def get_user_by_username(username):
        return User.collection.find_one({"username": username})

    @staticmethod
    def check_password(hashed_password, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))

class Task:
    collection = db['tasks']

    @staticmethod
    def create_task(data):
        """إضافة مهمة جديدة إلى الـ MongoDB مع التأكد من تحويل ObjectId إلى str"""
        # إضافة الوقت الحالي لتاريخ الإنشاء والتحديث
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()

        # إدخال المهمة في الـ collection
        result = Task.collection.insert_one(data)  # إضافة المهمة إلى collection
        
        # البحث عن المهمة باستخدام _id بعد الإدخال
        task = Task.collection.find_one({"_id": result.inserted_id})
        
        # تحويل _id إلى task_id (تحويل ObjectId إلى str)
        task['task_id'] = str(task['_id'])  # تحويل ObjectId إلى str

        # إعادة المهمة مع task_id كـ str
        return task

    @staticmethod
    def get_task_by_id(task_id):
        """الحصول على مهمة باستخدام task_id"""
        return Task.collection.find_one({"task_id": task_id})

    @staticmethod
    def get_tasks_by_user_id(user_id):
        """الحصول على كل المهام باستخدام user_id"""
        return Task.collection.find({"user_id": user_id})

    @staticmethod
    def update_task(task_id, data):
        """تحديث مهمة باستخدام task_id"""
        # إضافة التحديث على تاريخ التعديل
        data['updated_at'] = datetime.utcnow()
        
        # تحديث المهمة في الـ MongoDB
        Task.collection.update_one({"task_id": task_id}, {"$set": data})

        # إرجاع المهمة المحدّثة
        return Task.get_task_by_id(task_id)

    @staticmethod
    def delete_task(task_id):
        """حذف مهمة باستخدام task_id"""
        Task.collection.delete_one({"task_id": task_id})


class Habit:
    collection = db['habits']

    @staticmethod
    def create_habit(data):
        # تحويل start_date و end_date إلى datetime
        if 'start_date' in data:
            data['start_date'] = datetime.combine(data['start_date'], datetime.min.time())
        if 'end_date' in data:
            data['end_date'] = datetime.combine(data['end_date'], datetime.min.time())
        
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        Habit.collection.insert_one(data)
        return data

    @staticmethod
    def get_habit_by_id(habit_id):
        return Habit.collection.find_one({"_id": habit_id})

    @staticmethod
    def update_habit(habit_id, data):
        data['updated_at'] = datetime.utcnow()
        Habit.collection.update_one({"_id": habit_id}, {"$set": data})

    @staticmethod
    def delete_habit(habit_id):
        Habit.collection.delete_one({"_id": habit_id})

# جدول أعضاء الفريق (TeamMembers)
class TeamMember:
    collection = db['team_members']

    @staticmethod
    def add_team_member(data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        TeamMember.collection.insert_one(data)
        return data

    @staticmethod
    def get_team_member(team_member_id):
        return TeamMember.collection.find_one({"_id": team_member_id})

    @staticmethod
    def update_team_member(team_member_id, data):
        data['updated_at'] = datetime.utcnow()
        TeamMember.collection.update_one({"_id": team_member_id}, {"$set": data})

    @staticmethod
    def delete_team_member(team_member_id):
        TeamMember.collection.delete_one({"_id": team_member_id})

# جدول الفريق (Team)
class Team:
    collection = db['teams']

    @staticmethod
    def create_team(data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        Team.collection.insert_one(data)
        return data

    @staticmethod
    def get_team(team_id):
        return Team.collection.find_one({"_id": team_id})

    @staticmethod
    def update_team(team_id, data):
        data['updated_at'] = datetime.utcnow()
        Team.collection.update_one({"_id": team_id}, {"$set": data})

    @staticmethod
    def delete_team(team_id):
        Team.collection.delete_one({"_id": team_id})

# جدول مهام الفريق (TeamTask)
class TeamTask:
    collection = db['team_tasks']

    @staticmethod
    def create_task(data):
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        TeamTask.collection.insert_one(data)
        return data

    @staticmethod
    def get_task_by_id(task_id):
        return TeamTask.collection.find_one({"_id": task_id})

    @staticmethod
    def get_tasks_by_team_id(team_id):
        return TeamTask.collection.find({"team_id": team_id})

    @staticmethod
    def update_task(task_id, data):
        data['updated_at'] = datetime.utcnow()
        TeamTask.collection.update_one({"_id": task_id}, {"$set": data})

    @staticmethod
    def delete_task(task_id):
        TeamTask.collection.delete_one({"_id": task_id})
