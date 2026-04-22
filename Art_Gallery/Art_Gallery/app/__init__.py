from datetime import timedelta
from flask import Flask, session, request
from flask_babel import Babel

# Create Flask app
app = Flask(__name__)

# Secret key for session handling
app.secret_key = 'a secret key'

# Session settings — keep cookie alive and compatible with redirects
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Supported languages (match your base.html)
LANGUAGES = ['en_IE', 'zh_CN', 'ja_JP']


# Map session language codes to Babel locale identifiers
LOCALE_MAP = {
    'en_IE': 'en_IE',
    'zh_CN': 'zh_Hans_CN',  # Babel normalizes zh_CN to zh_Hans_CN
    'ja_JP': 'ja_JP',
}


# Locale selector for Babel
def get_locale():
    # If user selected a language, use it
    if 'language' in session:
        return LOCALE_MAP.get(session['language'], session['language'])

    # Otherwise detect from browser
    return request.accept_languages.best_match(LANGUAGES)


# Initialize Babel
babel = Babel()
babel.init_app(app, locale_selector=get_locale)


# Import routes
from . import routes