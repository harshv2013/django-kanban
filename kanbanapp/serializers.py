
from rest_framework import serializers
from kanbanapp.models import User, Board, Collection


#################################################################
"""
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'password', 'is_superuser', 'is_staff', 'email')
        fields = ('username', 'password', 'email')

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            # is_staff=validated_data['is_staff'],
            email=validated_data['email']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
"""
###################################################################

class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Board
        # fields = "__all__"
        fields = ['id', 'title','description', 'created_at', 'updated_at', 'owner']


class CollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Collection
        # fields = "__all__"
        fields = ['id', 'name','description', 'created_at', 'updated_at', 'owner', 'board']