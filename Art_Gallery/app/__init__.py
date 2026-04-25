from flask import Flask, session, request
from flask_babel import Babel

# This will set the language variable in session for the Babel app.
# If no language is set in session, return the best browser match.
def get_locale():
    if 'language' in session:
        if session['language'] == 'zh_CN':
            return 'zh_Hans_CN'
        return session['language']
    return request.accept_languages.best_match(['en_IE', 'zh_Hans_CN', 'ja_JP'])


# Create the Flask app
app = Flask(__name__)

# Session language uses secret key
app.secret_key = 'a secret key'


# Hook Babel into the app
babel = Babel(app)

# Initialize Babel locale selector
babel.init_app(app, locale_selector=get_locale)


# Import routes
from . import routes