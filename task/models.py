from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['Shift-Start-db']



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
