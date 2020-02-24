from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('tag/<str:name>', TagDetail.as_view(), name="tag_detail"),
    path('create/tag', TagCreate.as_view(), name="tag_create"),
    path('create/', PostCreate.as_view(), name="post_create"),
    path('edit/<str:slug>', PostEdit.as_view(), name="post_edit"),
    path('delete/<str:slug>', PostDelete.as_view(), name="post_delete"),
    path('<str:slug>', PostDetail.as_view(), name="post_detail"),
]