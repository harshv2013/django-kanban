
from rest_framework import serializers
from kanbanapp.models import User, Board, Collection, Task


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

    # def create(self, validated_data):
    #     pass



class MyCollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Collection
        # fields = "__all__"
        fields = ['id', 'name', 'created_at', 'updated_at', 'owner', 'board']
        # fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    collection = MyCollectionSerializer()

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['id', 'name', 'created_at', 'updated_at', 'owner', 'collection']

class CollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Collection
        # fields = "__all__"
        fields = ['id', 'name', 'created_at', 'updated_at', 'owner', 'board','tasks']
        read_only_fields = ['tasks']

class NewCollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # tasks = TaskSerializer(many=True)
    tasks = serializers.SerializerMethodField('get_tasks')

    class Meta:
        model = Collection
        # fields = "__all__"
        fields = ['id', 'name', 'created_at', 'updated_at', 'owner', 'board','tasks']
        read_only_fields = ['tasks']

    def get_tasks(self, obj):
        search_text = self.context.get('search_text')
        # tasks = Task.objects.filter(collection=obj)
        # TODO 1. Sorting 2. pagination 3. UnitTest
        tasks = Task.objects.filter(collection=obj).order_by("-created_at")
        if search_text:
            tasks = tasks.filter(name__icontains=search_text)
        # tasks = Task.objects.all()
        serializer = TaskSerializer(instance=tasks, many=True)
        return serializer.data

