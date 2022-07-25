# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_plays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS song_plays (songplay_id SERIAL PRIMARY KEY, start_time time NOT NULL, user_id int NOT NULL, level varchar, 
song_id varchar, artist_id varchar NOT NULL, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration numeric);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar, location varchar, latitude varchar, longitude varchar);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS times (time_id SERIAL PRIMARY KEY, start_time time, hour int, day int, week int, month int, year int, weekday int);
""")

foreign_key_constraints_create = """
alter table song_plays
add constraint fk_users
foreign key (user_id)
REFERENCES users (user_id);

alter table song_plays
add constraint fk_artists
foreign key (artist_id)
REFERENCES artists (artist_id);

alter table song_plays
add constraint fk_songs
foreign key (song_id)
REFERENCES songs (song_id);

alter table songs
add constraint fk_artists
foreign key (artist_id)
REFERENCES artists (artist_id);
"""


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO song_plays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) 
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
                 VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                 VALUES (%s, %s, %s, %s, %s)
                 ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO times (start_time, hour, day, week, month, year, weekday) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)
                 ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id FROM songs INNER JOIN artists ON songs.artist_id = artists.artist_id 
WHERE songs.title = %s and artists.name = %s and songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create, foreign_key_constraints_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]