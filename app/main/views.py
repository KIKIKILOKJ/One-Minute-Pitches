from flask import render_template
from app import app
from .models import comments
from .forms import CommentForm
Comment = comments.Comment

@app.route('/')
def index():
    title = 'LIFE CHANGING PITCHES'
    return render_template('index.html',title = title)

@app.route('/pitches/')
def pitches():
    return render_template('pitches.html')

@app.route('/pitches/comment/new', methods=['GET','POST'])
def new_comment():
    form = CommentForm()
    
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(title,comment)
        new_comment.save_comments()
        
    return render_template('new_comment.html',comments_form = form)