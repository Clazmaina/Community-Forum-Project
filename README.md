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

Week 3
 User Authentication:
    Registration, login, and logout functionality.
 User Profiles:
    User profile management.
 Categories, Threads, and Posts:
    Create, read, update, and delete categories, threads, and posts.
 Likes:
    Users can like posts.
 User Following (Subscriptions):
    Users can follow other users, categories, or threads.
 Notifications:
    Users receive notifications for relevant activities.


1. Clone the repository:
    bash
    git clone [repository URL]
    
2. Create a virtual environment:
    bash
    python -m venv venv
    
3. Activate the virtual environment:
    On Windows: venv\Scripts\activate
4. Install dependencies:
    bash
    pip install -r requirements.txt
    
5. Run migrations:
    bash
    python manage.py makemigrations
    python manage.py migrate
    
6. Run the development server:
    bash
    python manage.py runserver
    
API Endpoints
7. User Follows:
   GET/api/follows/: List all follows of the current user.
   POST/api/follows/: Create a new follow.
   DELETE/api/follows/{follow_id}/: Delete a follow.

8. Notifications:
   GET/api/notifications/: List notifications for the current user.
   PUT/api/notifications/{notification_id}/mark-read/: Mark a notification as read.