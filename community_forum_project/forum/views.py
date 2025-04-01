from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import UserSerializer, ProfileSerializer, CategorySerializer, ThreadSerializer, PostSerializer, LikeSerializer, UserFollowSerializer, NotificationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Profile, Category, Thread, Post, Like, UserFollow, Notification
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'})

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ThreadListCreateView(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ThreadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception:
            raise ValidationError("You have already liked this post.")

class LikeDestroyView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)
    
class UserFollowListCreate(generics.ListCreateAPIView):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    permission_class = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        follower = self.request.user
        following_user_id = self.request.data.get('following_user')
        following_category_id = self.request.data.get('following_category')
        following_thread_id = self.request.data.get('following_thread')

        if not (following_user_id or following_category_id or following_thread_id):
            raise ValidationError("You must specify either a user, category, or thread to follow.")
        
        if following_user_id:
            if UserFollow.objects.filter(follower=follower, following_user=following_user_id).exists():
                raise ValidationError("You are already following this user.")
            elif following_category_id:
                if UserFollow.objects.filter(follower=follower, following_category=following_category_id).exists():
                    raise ValidationError("You are already following this category.")
                if UserFollow.objects.filter(follower=follower, following_thread=following_thread_id).exists():
                    raise ValidationError("You are already following this thread.")
                
                serializer.save(follower=follower)

class UserFollowDestroy(generics.DestroyAPIView):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserFollow.objects.filter(follower=self.request.user)
    
class NotificationList(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')
    
class NotificationMarkRead(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def perform_update(self,serializer):
        serializer.save(is_read=True)