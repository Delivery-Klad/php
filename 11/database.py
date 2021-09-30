import psycopg2


def db_connect():
    con = psycopg2.connect(
        host="ec2-54-198-252-9.compute-1.amazonaws.com",
        database="d7sjscgk5e4258",
        user="slllyeejcwnmyt",
        port=5432,
        password="76e7f204bbb6559b72bcaef582731d086e7fd40dfca9ad358485ed5ece8c2b0a"
    )
    return con, con.cursor()


def create_tables():
    try:
        connect, cursor = db_connect()
        cursor.execute("CREATE TABLE IF NOT EXISTS enclosure(id BIGSERIAL PRIMARY KEY,"
                       "url TEXT NOT NULL,"
                       "type TEXT NOT NULL,"
                       "length INTEGER NOT NULL)")
        connect.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS item(id BIGSERIAL PRIMARY KEY,"
                       "title TEXT NOT NULL,"
                       "link TEXT NOT NULL,"
                       "pubDate TEXT NOT NULL,"
                       "tags TEXT NOT NULL,"
                       "description TEXT NOT NULL,"
                       "guid_link TEXT NOT NULL,"
                       "enclosure_id BIGINT REFERENCES enclosure (id))")
        cursor.execute("CREATE TABLE IF NOT EXISTS subjects(id BIGSERIAL PRIMARY KEY,"
                       "text TEXT NOT NULL)")
        connect.commit()
        cursor.execute("CREATE TABLE IF NOT EXISTS full_info(item_id BIGINT REFERENCES item (id),"
                       "subject_id BIGINT REFERENCES subjects (id),"
                       "CONSTRAINT full_info_pkey PRIMARY KEY (item_id, subject_id))")
        connect.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        connect.close()


def add_enclosure(url: str, en_type: str, length: str):
    connect, cursor = db_connect()
    cursor.execute(f"INSERT INTO enclosure (url, type, length) VALUES ('{url}', '{en_type}', {length})")
    connect.commit()
    cursor.execute("SELECT MAX(id) FROM enclosure")
    return cursor.fetchall()[0][0]


def add_item(title: str, link: str, pubDate: str, tags: str, description: str, guid_link: str, enclosure_id: int):
    connect, cursor = db_connect()
    cursor.execute(f"INSERT INTO item (title, link, pubDate, tags, description, guid_link, enclosure_id) VALUES "
                   f"('{title}', '{link}', '{pubDate}', '{tags}', '{description}', '{guid_link}', {enclosure_id})")
    connect.commit()
    cursor.execute("SELECT MAX(id) FROM item")
    return cursor.fetchall()[0][0]


def add_subjects(text: str):
    connect, cursor = db_connect()
    cursor.execute(f"INSERT INTO subjects (text) VALUES ('{text}')")
    connect.commit()
    cursor.execute("SELECT MAX(id) FROM subjects")
    return cursor.fetchall()[0][0]


def add_full_info(item_id: int, subject_id: int):
    connect, cursor = db_connect()
    cursor.execute(f"INSERT INTO full_info VALUES ({item_id}, {subject_id})")
    connect.commit()
    return True


def get_subjects(item_id: int):
    connect, cursor = db_connect()
    cursor.execute(f"SELECT text FROM full_info JOIN subjects ON full_info.subject_id = subjects.id WHERE "
                   f"item_id={item_id}")
    subjects = []
    for subject in cursor.fetchall():
        subjects.append(subject[0])
    return subjects


def select_all():
    connect, cursor = db_connect()
    cursor.execute("SELECT DISTINCT item.id,title,link,pubDate,tags,description,guid_link,url,type,length FROM item "
                   "JOIN enclosure ON item.enclosure_id = enclosure.id")
    result = cursor.fetchall()
    returned = []
    for i in result:
        tags = i[4] if i[4] != "" else None
        description = i[5] if i[5] != "" else None
        returned.append({"title": i[1],
                         "link": i[2],
                         "publication_date": i[3],
                         "tags": tags,
                         "description": description,
                         "guid_link": i[6],
                         "enclosure": {"url": i[7], "type": i[8], "length": i[9]},
                         "subjects": get_subjects(i[0])})
    return returned
