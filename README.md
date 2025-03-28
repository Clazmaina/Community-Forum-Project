# Community-Forum-Project
Community forum application

  IDEA
It is an online application that serves as a platform for users to create and participate in discussions.

Thursday
I added several features including:
1. User registration - this will allow users to create new accounts
2. User login - this will allow users to access a session
3. User logout - it enables users to end a session
4. User profile - it allows users to view and update their profiles

I started by cloning my github repository and creating a virtual environment(better than installing globally)

After all these, I ran the migrations(python manage.py migrate)

Then I started the development server(python manage.py runserver)

In this first week, I added a few API Endpoints which are:
1. POST/forum/register
2. POST/forum/login
3. POST/forum/logout
4. GET/PUT/forum/profile/<int:pk>/ ,

Week 2
Started by reinitializing my git reposritory
I figured how to check if my virtual environment has django installed
Activated my virtual environment venv\Scripts\activate
Added more API endpoints
1. Categories:
     GET/api/categories/
     POST/api/categories/
     GET/api/categories/{id}/
     PUT/api/categories/{id}/
     DELETE/api/categories/{id}/

2. Threads:
     GET/api/threads/
     POST/api/threads/
     GET/api/threads/{id}/
     PUT/api/threads/{id}/
     DELETE/api/threads/{id}/

3. Posts:
     GET/api/posts/
     POST/api/posts/
     GET/api/posts/{id}/
     PUT/api/posts/{id}/
     DELETE/api/posts/{id}/

4. Likes:
     POST/api/likes/
     DELETE/api/likes/{id}/

