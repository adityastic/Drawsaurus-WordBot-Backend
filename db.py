import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


# conn = psycopg2.connect(database='test_rent', user='rupal', password='postgres')


def get_con():
    cur = conn.cursor()
    cur.execute('SELECT version()')
    return "Postgres with version " + str(cur.fetchone())


def add_word(word):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO drawsaurus.words VALUES ('{word}') ON CONFLICT DO NOTHING")
    conn.commit()
    return {'msg': 'Success'}
