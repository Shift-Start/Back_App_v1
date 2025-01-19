<<<<<<< HEAD
=======
from django.db import models
from bson import ObjectId
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
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

<<<<<<< HEAD
=======
    @staticmethod
    def delete_members_by_team_id(team_id):
        # حذف جميع الأعضاء المرتبطين بفريق معين.
        result = TeamMember.collection.delete_many({"team_id": str(team_id)})
        print(f"Deleted {result.deleted_count} members for team_id: {team_id}")  # طباعة عدد الأعضاء المحذوفين
        return result.deleted_count


>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
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
<<<<<<< HEAD
        Team.collection.delete_one({"_id": team_id})

# جدول مهام الفريق (TeamTask)
=======
        # حذف الفريق والأعضاء المرتبطين به.
        from .models import TeamMember  # تأكد من استيراد TeamMember إذا لم يكن مستوردًا
        print(f"Attempting to delete team with ID: {team_id}")  # طباعة لتأكيد بدء الحذف

        # حذف الأعضاء المرتبطين بالفريق
        deleted_members = TeamMember.delete_members_by_team_id(team_id)
        print(f"Members deleted: {deleted_members}")  # تأكيد عدد الأعضاء المحذوفين

        # حذف الفريق نفسه
        result = Team.collection.delete_one({"_id": ObjectId(team_id)})
        print(f"Team deleted: {result.deleted_count > 0}")  # تأكيد حذف الفريق

>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
class TeamTask:
    collection = db['team_tasks']

    @staticmethod
<<<<<<< HEAD
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
=======
    def add_team_task(data):
        try:
            return TeamTask.create_task(data)
        except Exception as e:
            raise ValueError(f"Error while adding task: {e}")

    @staticmethod
    def create_task(data):
        if "team_id" not in data:
            raise ValueError("Team ID is required to create a task.")
        data['created_at'] = datetime.utcnow()
        data['updated_at'] = datetime.utcnow()
        try:
            result = TeamTask.collection.insert_one(data)
            data['_id'] = result.inserted_id
            return data
        except Exception as e:
            raise ValueError(f"Error while creating task: {e}")

    @staticmethod
    def get_task_by_id(task_id):
        try:
            task = TeamTask.collection.find_one({"_id": ObjectId(task_id)})
            return dict(task) if task else None
        except Exception as e:
            raise ValueError(f"Invalid Task ID: {e}")

    @staticmethod
    def get_tasks_by_team_id(team_id):
        tasks = TeamTask.collection.find({"team_id": team_id})
        return [dict(task) for task in tasks]
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815

    @staticmethod
    def update_task(task_id, data):
        data['updated_at'] = datetime.utcnow()
<<<<<<< HEAD
        TeamTask.collection.update_one({"_id": task_id}, {"$set": data})

    @staticmethod
    def delete_task(task_id):
        TeamTask.collection.delete_one({"_id": task_id})
=======
        try:
            result = TeamTask.collection.update_one({"_id": ObjectId(task_id)}, {"$set": data})
            return result.modified_count > 0
        except Exception as e:
            raise ValueError(f"Error while updating task: {e}")

    @staticmethod
    def delete_task(task_id):
        try:
            result = TeamTask.collection.delete_one({"_id": ObjectId(task_id)})
            return result.deleted_count > 0
        except Exception as e:
            raise ValueError(f"Error while deleting task: {e}")

    @staticmethod
    def get_all_tasks():
        tasks = TeamTask.collection.find()
        return [dict(task) for task in tasks]
>>>>>>> f70151a67db44782b0182c41b22e35dbcd1ed815
