import psycopg2
import config

# ? To check the function in docker setup


def pgdbins(chatid, prgm):
    conn = psycopg2.connect(database="database", user="postgres",
                            password="postgres", host="db")
    cur = conn.cursor()
    sem = "S"
    cur.execute("INSERT INTO \"btech_demo\" VALUES(%s,%s,%s)",
                (chatid, sem, prgm))
    conn.commit()
    conn.close()

# pgdbins('456765434','B.Des')


def pgdb(list):
    rows2 = []

    conn = psycopg2.connect(database=config.db, user=config.database_usr,
                            password=config.database_pwd, host=config.db_host)
    cur = conn.cursor()
    for i in range(len(list)):
        cur.execute("SELECT cid FROM \"btech_demo\" WHERE \"prgm\"=%s AND \"sem\"=%s;",
                    (list[i]["program"], list[i]["semester"]))
        rows = cur.fetchall()
        for row in rows:
            rows2.append(row[0])
        # print(rows2)
        # rows1.append(rows)

    # print(" /// \n ")
    # print(rows2)
    # print("\n /// \n ")
    # for i in rows2:

    #     print(i)
    # # last = convertTuple(rows2)
    # # print(last)
    # print("\n /// \n ")
    # conn.close()

    return rows2

# pgdb(b)


def pgdbupd(chatid, sem):
    conn = psycopg2.connect(database="database", user="postgres",
                            password="postgres", host="db")
    cur = conn.cursor()
    chidstr = str(chatid)
    cur.execute(
        "UPDATE \"btech_demo\" SET \"sem\"=%s WHERE \"cid\"=%s;", (sem, chidstr))
    conn.commit()
    conn.close()

# pgdbins('456765434','B.Des')
