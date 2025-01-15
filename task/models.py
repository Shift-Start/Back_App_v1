from datetime import datetime, date
from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

# الاتصال بقاعدة البيانات
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['Shift-Start-db']

class Task:
    collection = db['tasks']

    @staticmethod
    def add_task(data):
        # تحويل التاريخ إذا كان من نوع date إلى datetime
        for key, value in data.items():
            if isinstance(value, date) and not isinstance(value, datetime):
                data[key] = datetime.combine(value, datetime.min.time())
        current_time = datetime.utcnow()
        data['created_at'] = current_time
        data['updated_at'] = current_time
        try:
            result = Task.collection.insert_one(data)
            data['_id'] = str(result.inserted_id)
            return data
        except PyMongoError as e:
            raise RuntimeError(f"Failed to add task: {e}")

    @staticmethod
    def get_task_by_id(task_id):
#         استرجاع مهمة باستخدام معرف المهمة.
        try:
            if not ObjectId.is_valid(task_id):
                raise ValueError(f"Invalid Task ID: {task_id} is not a valid ObjectId")
            task = Task.collection.find_one({"_id": ObjectId(task_id)})
            if task:
                task["_id"] = str(task["_id"])
                return dict(task)
            else:
                return {"error": "Task not found"}, 404
        except ValueError as ve:
            return {"error": str(ve)}, 400
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}, 500
    @staticmethod
    def get_tasks_by_user_id(user_id):
        try:
            tasks_collection = db['tasks']
            tasks_cursor = tasks_collection.find({"UserID": user_id})
            tasks_list = []
            for task in tasks_cursor:
                task["_id"] = str(task["_id"])
                tasks_list.append(task)

            if not tasks_list:
                return {"error": "No tasks found for this user"}, 404
            return tasks_list, 200
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}, 500

    @staticmethod
    def delete_task(task_id):
        try:
            if not ObjectId.is_valid(task_id):
                return {"error": "Invalid Task ID"}, 400
            result = Task.collection.delete_one({"_id": ObjectId(task_id)})
            if result.deleted_count > 0:
                return {"message": "Task deleted successfully"}, 200
            else:
                return {"error": "Task not found"}, 404
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}, 500

    @staticmethod
    def update_task(task_id, data):
        # تحديث بيانات المهمة باستخدام معرف المهمة
        try:
            if not ObjectId.is_valid(task_id):
                return {"error": "Invalid Task ID"}, 400
            
            data['updated_at'] = datetime.utcnow()
            result = Task.collection.update_one({"_id": ObjectId(task_id)}, {"$set": data})
            
            if result.matched_count == 0:
                return {"error": "Task not found"}, 404
            elif result.modified_count > 0:
                return {"message": "Task updated successfully"}, 200
            else:
                return {"message": "No changes made to the task"}, 304
        
        except Exception as e:
            return {"error": f"Error while updating task: {str(e)}"}, 500

    @staticmethod
    def get_all_tasks():
        try:
            tasks_cursor = Task.collection.find()
            tasks_list = []
            for task in tasks_cursor:
                task["_id"] = str(task["_id"])
                tasks_list.append(task)
            return tasks_list
        except Exception as e:
            raise ValueError(f"Error while retrieving tasks: {e}")
