from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from datetime import datetime
from team.models import Team, TeamMember
from team.serializers import TeamSerializer, TeamMemberSerializer

# دالة مساعدة لتحويل ObjectId إلى نصوص
def convert_object_id_to_string(data):
    """
    تحويل جميع الحقول التي تحتوي على ObjectId إلى نصوص.
    """
    if isinstance(data, list):
        for item in data:
            convert_object_id_to_string(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
            elif isinstance(value, (dict, list)):
                convert_object_id_to_string(value)
    return data



# عرض وإنشاء الفرق
class TeamListCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            team_data = serializer.validated_data
            team_data['created_at'] = datetime.utcnow()
            team_data['updated_at'] = datetime.utcnow()
            created_team = Team.create_team(team_data)
            created_team = convert_object_id_to_string(created_team)  # تحويل ObjectId إلى نصوص
            return Response(created_team, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        teams = Team.collection.find()
        team_list = [convert_object_id_to_string(team) for team in teams]  # تحويل ObjectId إلى نصوص
        return Response(team_list, status=status.HTTP_200_OK)


# عرض وإنشاء أعضاء الفريق
class TeamMemberListCreateView(APIView):
    def post(self, request):
        data = request.data
        serializer = TeamMemberSerializer(data=data)
        if serializer.is_valid():
            member_data = serializer.validated_data
            member_data['created_at'] = datetime.utcnow()
            member_data['updated_at'] = datetime.utcnow()
            created_member = TeamMember.add_team_member(member_data)
            created_member = convert_object_id_to_string(created_member)  # تحويل ObjectId إلى نصوص
            return Response(created_member, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        members = TeamMember.collection.find()
        member_list = [convert_object_id_to_string(member) for member in members]  # تحويل ObjectId إلى نصوص
        return Response(member_list, status=status.HTTP_200_OK)




# تحديث فريق
class TeamUpdateView(APIView):
    def put(self, request, team_id):
        data = request.data
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            updated_data = serializer.validated_data
            updated_data['updated_at'] = datetime.utcnow()
            Team.update_team(ObjectId(team_id), updated_data)  # تحديث الفريق باستخدام ObjectId
            updated_team = Team.get_team(ObjectId(team_id))
            updated_team = convert_object_id_to_string(updated_team)
            return Response(updated_team, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# حذف فريق
class TeamDeleteView(APIView):
    def delete(self, request, team_id):
        team = Team.get_team(ObjectId(team_id))
        if team:
            Team.delete_team(ObjectId(team_id))
            return Response({"message": "Team deleted successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)


# تحديث عضو فريق
class TeamMemberUpdateView(APIView):
    def put(self, request, member_id):
        data = request.data
        serializer = TeamMemberSerializer(data=data)
        if serializer.is_valid():
            updated_data = serializer.validated_data
            updated_data['updated_at'] = datetime.utcnow()
            TeamMember.update_team_member(ObjectId(member_id), updated_data)  # تحديث عضو الفريق باستخدام ObjectId
            updated_member = TeamMember.get_team_member(ObjectId(member_id))
            updated_member = convert_object_id_to_string(updated_member)
            return Response(updated_member, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# حذف عضو فريق
class TeamMemberDeleteView(APIView):
    def delete(self, request, member_id):
        member = TeamMember.get_team_member(ObjectId(member_id))
        if member:
            TeamMember.delete_team_member(ObjectId(member_id))
            return Response({"message": "Team member deleted successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Team member not found."}, status=status.HTTP_404_NOT_FOUND)
