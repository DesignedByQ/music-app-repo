from application import db
from application.models import Songs

db.drop_all()
db.create_all()

sample_song = Songs(title = "Billie Jean", artist = "Micheal Jackson", feature = "Tito", category = "Pop", reldate = '2021-08-09', length = 3.54)

sample_song1 = Songs(title = "Thriller", artist = "Micheal Jackson", category = "Pop", reldate = '2021-08-09', length = 5.35)

db.session.add(sample_song)
db.session.add(sample_song1)
db.session.commit()
