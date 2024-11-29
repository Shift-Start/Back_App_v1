from project.settings import db

class UserService:
    collection = db["users"]  # اسم المجموعة

    @staticmethod
    def get_all_users():
        return list(UserService.collection.find({}))

    @staticmethod
    def create_user(data):
        return UserService.collection.insert_one(data)

    @staticmethod
    def get_user_by_id(user_id):
        from bson.objectid import ObjectId
        return UserService.collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def delete_user(user_id):
        from bson.objectid import ObjectId
        return UserService.collection.delete_one({"_id": ObjectId(user_id)})
