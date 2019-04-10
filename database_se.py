import sqlite3

def readSql(name):
    f=open('{}.sql'.format(name),'r')
    temp=f.read()
    query=[]
    for x in temp.split(";"):
        query.append(x)
    return query

if __name__ == '__main__':
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    query=readSql('data')
    for sql in query:
        db.execute(sql)
    query = readSql('insertData')
    for sql in query:
        try:
            db.execute(sql)
        except Exception as e:
            print sql
            continue
    conn.commit()
    db.close()
    conn.close()
