import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warning": True
}

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        database = "movies",
        user = "movies_user",
        password = "popcorn"
    )

    #print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")

    else:
        print(err)


cursor = mydb.cursor()

def show_films(cursor, title):
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as `Studio Name` FROM film JOIN studio ON film.studio_id = studio.studio_id JOIN genre ON film.genre_id = genre.genre_id")

    film = cursor.fetchall()

    print(f"\n -- {title} --".format(title))
    stu = 'Studio Name'

    for Name, Director, Genre, stu in film:
        print(f"Film Name: {Name}\nDirector: {Director}\nGenre Name ID: {Genre}\nStudio Name: {stu}\n".format(film))

title = "DISPLAYING FILMS"
show_films(cursor, title)

#insert
insert_sql = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('Star Wars', '1977', 121, 'George Lucas', 1, 2)"
cursor.execute(insert_sql)
title = "DISPLAYING FILMS AFTER INSERT"
show_films(cursor, title)

#update
update_sql ="UPDATE film SET genre_id = 1 WHERE film_id = 2"
cursor.execute(update_sql)
title = "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror"
show_films(cursor, title)

#delete
delete_sql ="DELETE FROM film WHERE film_name = 'Gladiator'"
cursor.execute(delete_sql)
title = "DISPLAYING FILMS AFTER DELETE"
show_films(cursor, title)