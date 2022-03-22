from django.urls import include, path

# from .views import BoardListCreate, BoardRetriveUpdateDestroy
from .views import index,CollectionListCreate, \
    CollectionRetriveUpdateDestroy, \
    BoardCustomView, TaskListCreate

# from .views import UserListCreate, UserCreate, \
#     LoginView, UserList, UserDetail

board_highlight = BoardCustomView.as_view({
    'get': 'customquery'})


from kanbanapp.views import BoardCustomView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'boards', BoardCustomView, basename='boards2')
urlpatterns = router.urls


urlpatterns = [
    path('', index, name='index'),

    # path('user/', UserListCreate.as_view(), name='testuser-list'),
    # path("usercreate/", UserCreate.as_view(), name="user_create"),
    # path("login/", LoginView.as_view(), name="login"),
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>', UserDetail.as_view()),

    # path('boards/', BoardListCreate.as_view()),
    # path('boards/<int:pk>/', BoardRetriveUpdateDestroy.as_view()),

    path('customboards/', board_highlight),
    path('', include(router.urls)),

    path('collections/', CollectionListCreate.as_view()),
    path('collections/<int:pk>/', CollectionRetriveUpdateDestroy.as_view()),

    path('tasks/', TaskListCreate.as_view()),
]