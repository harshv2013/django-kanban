from django.urls import path

from .views import index, UserListCreate, UserCreate, \
    LoginView, UserList, UserDetail, \
    BoardListCreate, BoardRetriveUpdateDestroy, \
    CollectionListCreate, CollectionRetriveUpdateDestroy


urlpatterns = [
    path('', index, name='index'),
    path('user/', UserListCreate.as_view(), name='testuser-list'),

    path("usercreate/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),

    path('boards/', BoardListCreate.as_view()),
    path('boards/<int:pk>/', BoardRetriveUpdateDestroy.as_view()),

    path('collections/', CollectionListCreate.as_view()),
    path('collections/<int:pk>/', CollectionRetriveUpdateDestroy.as_view()),
]