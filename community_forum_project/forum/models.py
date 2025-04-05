from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"Liked by {self.user.username} on {self.post}"
    
class UserFollow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE, null=True, blank=True)
    following_category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    following_thread = models.ForeignKey('Thread', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following_user', 'following_category', 'following_thread')
        def __str__(self):
            if self.following_user:
                return f"{self.follower.username} follows {self.following_user.username}"
            elif self.following_category:
                return f"{self.follower.username} follows {self.following_category.name}"
            elif self.following_thread:
                return f"{self.follower.username} follows {self.following_thread.title}"
            else:
                return f"{self.follower.username} follows something" 
            
class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}:{self.message}"
    
