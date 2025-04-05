from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Category, Thread, Post, Like, UserFollow, Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user)

            return user
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'location', 'birth_date', 'profile_picture']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ThreadSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Thread
        fields = ['id', 'title', 'category', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = '__all__'

class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'
        read_only_fields = ('follower',)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ('recipient',)