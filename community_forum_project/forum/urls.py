from django.urls import path
from .views import register, login, logout, ProfileView, CategoryListCreateView, CategoryRetrieveUpdateDestroyView, ThreadListCreateView, ThreadRetrieveUpdateDestroyView, PostListCreateView, PostRetrieveUpdateDestroyView,LikeCreateView, LikeDestroyView, UserFollowListCreate, UserFollowDestroy, NotificationList, NotificationMarkRead

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('threads/', ThreadListCreateView.as_view(), name='thread-list-create'),
    path('threads/<int:pk>/', ThreadRetrieveUpdateDestroyView.as_view(), name='thread-retrieve-update-destroy'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', LikeDestroyView.as_view(), name='like-destroy'),
    path('follows/', UserFollowListCreate.as_view(), name='user-follow-list-create'),
    path('follows/<int:pk>/', UserFollowDestroy.as_view(), name='user-follow-destroy'),
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/mark-read/', NotificationMarkRead.as_view(), name='notification-mark-read'),
]