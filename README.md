# Blog



## Project Overview

Blog is a blog application.
Users can register, log in, browse all users' posts, and perform create, read, update, and delete operations on their own blogs and posts.
The project is built with Django.



## Installation & Run

1.Install dependencies

```bash
cd Blog
# create virtual environment
python -m venv ll_env
#activate virtual environment
ll_env\Scripts\activate	 #windows
source ll_env/bin/activate	#linux
#install dependencies
pip install -r requirements.txt
#migrate database
python manage.py migrate
```

2.Run

```bash
python manage.py runserver
```

Click the URL that appears to open the blog.

3.Others

```bash
# to exit virtual environment
deactivate
```



## Usage

- Use the 「Register / Log in」 links in the top-right navigation bar.
- The home page displays all users' blog posts; click a title to view the full post.
- The 「All Blogs」 link in the navigation bar lists the current user's own blogs.
- On the blogs page you can create a new blog or delete an existing one.
- Inside a specific blog you can see all its posts and add, edit, or delete them.
- Click 「Log out」 at the bottom of the page to sign out.