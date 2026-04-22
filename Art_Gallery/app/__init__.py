from flask import Flask, session, request
from flask_babel import Babel

# Create Flask app
app = Flask(__name__)

# Secret key for session handling
app.secret_key = 'a secret key'

# Supported languages (match your base.html)
LANGUAGES = ['en_IE', 'zh_CN', 'ja_JP']


# Locale selector for Babel
def get_locale():
    # If user selected a language, use it
    if 'language' in session:
        return session['language']

    # Otherwise detect from browser
    return request.accept_languages.best_match(LANGUAGES)


# Initialize Babel
babel = Babel()
babel.init_app(app, locale_selector=get_locale)


# Import routes
from . import routes