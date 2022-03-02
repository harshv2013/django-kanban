from django.shortcuts import render
from django.http import HttpResponse
from kanbanapp.models import User, Board, Collection
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import status
# from kanbanapp.serializers import UserSerializer
from kanbanapp.serializers import BoardSerializer, \
    CollectionSerializer
from .collection import creat_collection


def index(request):
    return HttpResponse("Hello, world. You're at the trello home page.")

############################################################
"""
class UserListCreate(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    # parser_classes = (MultiPartParser, FormParser, FileUploadParser)
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.instance)
        # user = serializer.data['username']
        # user = User.objects.get(pk=pk_of_user_without_token)
        # token = Token.objects.create(user=serializer.instance)
        # print(token)
        print('serializer.data in UserCreate in create defn is-', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

"""
################################################################

class BoardListCreate(APIView):
    """
    List all boards, or create a new board.
    """
    def get(self, request, format=None):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            res_obj = serializer.save(owner=self.request.user)
            # print(res.id)
            # print(res.__dict__)
            creat_collection(res_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a board instance.
    """
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        board = self.get_object(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        board = self.get_object(pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ########**********************************##################
class BoardCustomView(viewsets.ViewSet):

        def get_object(self, pk):
            try:
                return Board.objects.get(pk=pk)
            except Board.DoesNotExist:
                raise Http404

        def customquery(self, request, *args, **kwargs):
            boards = Board.objects.all()
            serializer = BoardSerializer(boards, many=True)
            return Response(serializer.data)

        def list(self, request):
            queryset = Board.objects.all()
            serializer = BoardSerializer(queryset, many=True)
            return Response(serializer.data)


        def create(self, request, format=None):
            serializer = BoardSerializer(data=request.data)
            if serializer.is_valid():
                res_obj = serializer.save(owner=self.request.user)
                # print(res.id)
                # print(res.__dict__)
                creat_collection(res_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        def retrieve(self, request, pk=None):
            queryset = Board.objects.all()
            board = get_object_or_404(queryset, pk=pk)
            serializer = BoardSerializer(board)
            return Response(serializer.data)


        def update(self, request, pk, format=None):
            board = self.get_object(pk)
            serializer = BoardSerializer(board, data=request.data)
            if serializer.is_valid():
                serializer.save(owner=self.request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        def partial_update(self, request, pk, format=None):
            board = self.get_object(pk)
            serializer = BoardSerializer(board, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(owner=self.request.user)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # def destroy(self, request, pk=None):
        #     pass

        def destroy(self, request, pk, format=None):
            board = self.get_object(pk)
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


        # @action(detail=False, methods=['get'])
        # def fetch_myboard(self, request, pk=None):
        #     print('at line ===================204')
        #     board = Board.objects.all()
        #     # board = get_object_or_404(queryset, pk=pk)
        #     serializer = BoardSerializer(board, many=True)
        #     return Response(serializer.data)


        @action(detail=False)
        def fetch_board(self, request):
            queryset = Board.objects.all()
            serializer = BoardSerializer(queryset, many=True)
            return Response(serializer.data)
            



#############################################################

class CollectionListCreate(APIView):
    """
    List all collection, or create a new collection.
    """
    def get(self, request, format=None):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionRetriveUpdateDestroy(APIView):
    """
    Retrieve, update or delete a collection instance.
    """
    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






