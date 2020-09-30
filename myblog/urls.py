from django.urls import path
# from . import views
from .views import home_view, post_detail_view, add_post_view, update_post_view,delete_post_view, add_comment_view, delete_comment_view

urlpatterns = [
    # path('', views.home, name="home"),
    path('', home_view.as_view(), name="home"),
    path('post/<int:pk>', post_detail_view.as_view(), name="post-detail"),
    path('add_post/', add_post_view.as_view(), name="add-post"),
    path('post/edit/<int:pk>', update_post_view.as_view(), name="update-post"),
    path('post/delete/<int:pk>', delete_post_view.as_view(), name="delete-post"),
    path('post/<int:pk>/comment', add_comment_view.as_view(), name="add-comment"),
    path('post/<int:pk>/comment/delete', delete_comment_view.as_view(), name="delete-comment"),
]

