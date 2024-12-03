from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['Shift-Start-db']


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
