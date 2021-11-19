from inmueblesApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        return {
            'id': user.id,
            'username': user.username
        }