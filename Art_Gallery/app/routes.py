from . import app
from flask import render_template, session, redirect, request, flash


# -------------------------------
# Language Selection Route
# -------------------------------
@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    # Ensure only supported languages are set
    if lang_code in ['en_IE', 'zh_CN', 'ja_JP']:
        session['language'] = lang_code
        session.modified = True   # force Flask to save the updated session
        session.permanent = True  # keep the cookie alive across the redirect

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
def gallery():
    return render_template("gallery.html")


@app.route('/artists')
def artists():
    return render_template("artists.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Collect form data for future processing/storage.
        name = request.form.get('name')
        email = request.form.get('email')
        purpose = request.form.get('purpose')
        other_purpose = request.form.get('other_purpose')
        message = request.form.get('message')
        return redirect('/contact/thank-you')
    return render_template("contact.html")


@app.route('/contact/thank-you')
def contact_thank_you():
    return render_template("thank_you.html")


@app.route('/faq')
def faq():
    return render_template("faq.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/art')
def art():
    return render_template("art.html")


# -------------------------------
# Artwork Submission Route
# -------------------------------
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Collect form data (to be processed/stored in future)
        artist_name = request.form.get('artist_name')
        email = request.form.get('email')
        artwork_title = request.form.get('artwork_title')
        medium = request.form.get('medium')
        year = request.form.get('year')
        description = request.form.get('description')
        statement = request.form.get('statement')
        portfolio = request.form.get('portfolio')
        flash('submission_success')
        return redirect('/submit')
    return render_template("submit.html")
