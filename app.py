import json
import os

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


def load_blog_posts():
    # Construct the path to the JSON file in the static folder
    json_file_path = os.path.join('static', 'blog_posts.json')
    with open(json_file_path, 'r') as file:
        return json.load(file)


def save_blog_posts(blog_posts):
    json_file_path = os.path.join('static', 'blog_posts.json')
    with open(json_file_path, 'w') as file:
        json.dump(blog_posts, file)


@app.route('/')
def index():
    blog_posts = load_blog_posts()
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        blog_posts = load_blog_posts()
        new_id = max(post['id'] for post in blog_posts) + 1 if blog_posts else 1

        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }

        blog_posts.append(new_post)
        save_blog_posts(blog_posts)

        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    blog_posts = load_blog_posts()
    blog_posts = [post for post in blog_posts if post['id'] != post_id]
    save_blog_posts(blog_posts)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    blog_posts = load_blog_posts()
    post = next((p for p in blog_posts if p['id'] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post details
        post['author'] = request.form['author']
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        save_blog_posts(blog_posts)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    # Initialize the session if it doesn't exist
    if 'liked_posts' not in session:
        session['liked_posts'] = []

    # Check if the post has already been liked
    if post_id in session['liked_posts']:
        return redirect(url_for('index'))  # Prevent adding another like

    blog_posts = load_blog_posts()
    post = next((p for p in blog_posts if p['id'] == post_id), None)

    if post is None:
        return "Post not found", 404

    # Increment the likes count
    post['likes'] += 1
    session['liked_posts'].append(post_id)  # Add to the session
    save_blog_posts(blog_posts)  # Save changes back to JSON file

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
