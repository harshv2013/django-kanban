from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from todo import views

router = DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')
urlpatterns = router.urls


urlpatterns = [

    path('', include(router.urls)),
    re_path(r'^students/$', views.students_list),
    re_path(r'^students/([0-9])$', views.students_detail),

]