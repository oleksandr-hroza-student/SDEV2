from app import app
from flask import render_template, session, redirect, request


# -------------------------------
# Language Selection Route
# -------------------------------
@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    # Ensure only supported languages are set
    if lang_code in ['en_IE', 'zh_CN', 'ja_JP']:
        session['language'] = lang_code

    # Redirect back to previous page
    return redirect(request.referrer or '/')


# -------------------------------
# Default Language Setup
# -------------------------------
@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en_IE'  # Default: English (Ireland)


# -------------------------------
# Main Routes
# -------------------------------
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/gallery')
@app.route('/art')
def gallery():
    return render_template("art.html")


@app.route('/artists')
def artists():
    return render_template("artists.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/submit')
def submit():
    return render_template("submit.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")
