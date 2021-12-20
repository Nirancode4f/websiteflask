from flask import Blueprint , render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404