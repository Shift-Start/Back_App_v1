from rest_framework import serializers

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    admin_id = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    goal = serializers.CharField(max_length=200, allow_blank=True, required=False)
    setting_team = serializers.JSONField(required=False)

class TeamMemberSerializer(serializers.Serializer):
    team_id = serializers.CharField(max_length=50)
    user_id = serializers.CharField(max_length=50)
    permissions = serializers.JSONField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
