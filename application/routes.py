from application import app
from application import db
from application.models import Songs
from flask import render_template, request
from application.forms import SongForm

#check VM is connected to browser
@app.route('/browser')
def browsercon():
    todo = 'Connected'
    return todo

@app.route('/viewdbsongs')
def viewdbsongs():
    all_songs = Songs.query.all()
    return render_template('songs.html', songslist=all_songs)   

#add song to the db
@app.route('/addsong', methods=['GET', 'POST'])
def addsong():
    message = ""
    form = SongForm()

    if request.method == 'POST':
        ntitle = form.ntitle.data
        nartist = form.nartist.data
        nfeature = form.nfeature.data
        ncategory = form.ncategory.data
        nreldate = form.nreldate.data
        nlength = form.nlength.data
        message = ntitle + ' has been added'

        if form.validate_on_submit():
            new_song = Songs(title=ntitle, artist=nartist, feature=nfeature, category=ncategory, reldate=nreldate, length=nlength)
            db.session.add(new_song)
            db.session.commit()  

    return render_template('addsong.html', form=form, message=message)