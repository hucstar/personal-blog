from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Route for creating posts
@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Logic for creating a post
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html')

# Route for viewing posts
@app.route('/posts')
def view_posts():
    # Logic to retrieve posts
    return render_template('view_posts.html')

# User authentication route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic for user authentication
        flash('Logged in successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Logic for logging out
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

# Search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Logic for searching posts
    return render_template('search_results.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
