# My Flask Blog

Welcome to **My Flask Blog**! This is a simple blog application built using Flask. It allows users to view, add, update, delete, and like blog posts.

## Features

- Display a list of blog posts with author, title, content, and like count.
- Add new blog posts through a user-friendly form.
- Update existing blog posts.
- Delete blog posts easily.
- Toggle likes for each blog post.

## Technologies Used

- Python
- Flask
- HTML/CSS
- JSON for data storage

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-flask-blog
2. Install Flask:
    ```bash
   pip install Flask
3. Run the application:
    ```bash
   python app.py
4. Open your browser and visit:
    ```bash
   http://127.0.0.1:5000/
   
### Project structure
/my-flask-blog/
├── app.py                # Main Flask application
├── blog_posts.json       # JSON file for storing blog data
├── /templates/           # Folder for HTML templates
│   ├── index.html        # Main template for displaying posts
│   ├── add.html          # Template for adding a new blog post
│   └── update.html       # Template for updating an existing blog post
└── /static/              # Folder for static files (CSS, JS)
    └── style.css         # Stylesheet for the blog

### Usage

	1.	Home Page: Displays all blog posts with options to add, update, and delete posts.
	2.	Add Post: Navigate to /add to create a new blog post.
	3.	Update Post: Click the “Update” button next to each post to edit its details.
	4.	Delete Post: Click the “Delete” button next to each post to remove it.
	5.	Like Feature: Click the “Like” button to toggle likes on each post.

