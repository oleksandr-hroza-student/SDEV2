from . import app
from flask import render_template, session, redirect, request, flash
from .artistdata import artists, paintings


# -------------------------------
# Language Selection Route
# -------------------------------
@app.route('/set_language/<lang_code>')
def set_language(lang_code):
    if lang_code in ['en_IE', 'zh_CN', 'ja_JP']:
        session['language'] = lang_code
        session.modified = True
        session.permanent = True

    return redirect(request.referrer or '/')


# -------------------------------
# Default Language Setup
# -------------------------------
@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en_IE'


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
def artists_page():
    return render_template("artists.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
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
        flash('submission_success')
        return redirect('/submit')
    return render_template("submit.html")


# -------------------------------
# Artist Detail Page
# -------------------------------
@app.route('/artist/<artist_id>')
def artist_detail(artist_id):
    artist = artists.get(artist_id)
    if not artist:
        return redirect('/catalog')

    works = [
        paintings[w]
        for w in artist.get('works', [])
        if w in paintings
    ]

    return render_template(
        'artist.html',
        artist=artist,
        works=works
    )
    return render_template('artist.html')
