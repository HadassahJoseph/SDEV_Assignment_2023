from app import app
from flask import render_template, session, redirect, request, url_for


@app.route('/')
@app.route('/home')
def home():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("korea/index.html", lang_code=session["language"])

@app.route('/')
@app.route('/Khome')
def Khome():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("korea/index.html", lang_code=session["language"])

@app.route('/')
@app.route('/Kaccom')
def Kaccom():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("korea/bookings.html", lang_code=session["language"])

@app.route('/')
@app.route('/Kguides')
def Kguides():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("korea/guides.html", lang_code=session["language"])

@app.route('/')
@app.route('/Kttd')
def Kttd():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("korea/ttd.html", lang_code=session["language"])


@app.route('/')
@app.route('/Nhome')
def Nhome():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("norway/index.html", lang_code=session["language"])

@app.route('/')
@app.route('/Naccom')
def Naccom():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("norway/bookings.html", lang_code=session["language"])

@app.route('/')
@app.route('/Nguides')
def Nguides():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("norway/guides.html", lang_code=session["language"])

@app.route('/')
@app.route('/Nttd')
def Nttd():
    if session.get("language") is None:
        session["language"] = 'en'
    return render_template("norway/ttd.html", lang_code=session["language"])



@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    # Set the session variable lang to whatever code was used in the url
    session["language"] = lang_code
    # refresh the page from which the set language request was made
    return redirect(request.referrer)

