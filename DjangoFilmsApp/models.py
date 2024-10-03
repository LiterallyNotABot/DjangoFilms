# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actors(models.Model):
    actor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    picture_url = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'actors'


class Actorsandawards(models.Model):
    actor_award_id = models.AutoField(primary_key=True)
    actor = models.ForeignKey(Actors, models.DO_NOTHING)
    award = models.ForeignKey('Awards', models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'actorsandawards'
        unique_together = (('actor', 'award'),)


class Awardcategories(models.Model):
    award_category_id = models.AutoField(primary_key=True)
    award_category_name = models.CharField(max_length=100)
    active = models.BooleanField()
    deleted = models.BooleanField()
    award_cat_type = models.ForeignKey('Awardcategorytypes', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'awardcategories'


class Awardcategorytypes(models.Model):
    award_cat_type_id = models.AutoField(primary_key=True)
    award_cat_type = models.CharField(max_length=50)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'awardcategorytypes'


class Awardnames(models.Model):
    award_name_id = models.AutoField(primary_key=True)
    award_name = models.CharField(max_length=50)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'awardnames'


class Awards(models.Model):
    award_id = models.AutoField(primary_key=True)
    film = models.ForeignKey('Films', models.DO_NOTHING)
    award_and_cat = models.ForeignKey('Awardsandcategories', models.DO_NOTHING)
    year_won = models.IntegerField(blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'awards'
        unique_together = (('award_and_cat', 'year_won'), ('award_and_cat', 'film'),)


class Awardsandcategories(models.Model):
    award_and_cat_id = models.AutoField(primary_key=True)
    award_name = models.ForeignKey(Awardnames, models.DO_NOTHING)
    award_category = models.ForeignKey(Awardcategories, models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'awardsandcategories'
        unique_together = (('award_name', 'award_category'),)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    parent_comment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    creation_date = models.DateTimeField()
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'comments'


class Directors(models.Model):
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    picture_url = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'directors'


class Directorsandawards(models.Model):
    director_award_id = models.AutoField(primary_key=True)
    director = models.ForeignKey(Directors, models.DO_NOTHING)
    award = models.ForeignKey(Awards, models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'directorsandawards'
        unique_together = (('director', 'award'),)

class Films(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_year = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    picture_url = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'films'


class Filmsandactors(models.Model):
    film_actor_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Films, models.DO_NOTHING)
    actor = models.ForeignKey(Actors, models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'filmsandactors'


class Filmsandcomments(models.Model):
    film_comment_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Films, models.DO_NOTHING)
    comment = models.ForeignKey(Comments, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'filmsandcomments'


class Filmsanddirectors(models.Model):
    film_director_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Films, models.DO_NOTHING)
    director = models.ForeignKey(Directors, models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'filmsanddirectors'


class Filmsandgenres(models.Model):
    film_genre_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Films, models.DO_NOTHING)
    genre = models.ForeignKey('Genres', models.DO_NOTHING)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'filmsandgenres'


class Filmsandlists(models.Model):
    film_list_id = models.AutoField(primary_key=True)
    list = models.ForeignKey('Userfilmlists', models.DO_NOTHING)
    film = models.ForeignKey(Films, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'filmsandlists'
        unique_together = (('list', 'film'),)


class Filmsandratingbyusers(models.Model):
    film_rating_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Films, models.DO_NOTHING)
    rating = models.ForeignKey('Ratings', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'filmsandratingbyusers'
        unique_together = (('film', 'user'),)


class Genres(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=80)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'genres'


class Privatemessages(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('Users', models.DO_NOTHING)
    receiver = models.ForeignKey('Users', models.DO_NOTHING, related_name='privatemessages_receiver_set')
    date_sent = models.DateTimeField()
    content = models.TextField()
    read_status = models.BooleanField()
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'privatemessages'


class Ratings(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_value = models.DecimalField(max_digits=2, decimal_places=1)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'ratings'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=50)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'roles'


class Userfilmlists(models.Model):
    list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    list_name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'userfilmlists'
        unique_together = (('user', 'list_name'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    date_of_birth = models.DateField(blank=True, null=True)
    registration_date = models.DateTimeField()
    picture_url = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'users'
