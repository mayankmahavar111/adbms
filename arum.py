import sqlite3


def getSwat(db):
    sql="select max(site_id) from sites"
    db.execute(sql)
    site=db.fetchone()[0]
    attibutes=['birthdate','salary','location']
    mod=['rf','uf']

    swat=[]
    for i in range(site):
        temp=[]
        for attibute in attibutes:
            sql ="""select sum(predicate*frequency) from arum where site_id ={} and mod="{}" and attribute ="{}" """.format(i+1,mod[0],attibute)
            db.execute(sql)
            rf=db.fetchone()[0]
            sql = """select sum(predicate*frequency) from arum where site_id ={} and mod="{}" and attribute ="{}" """.format(i+1,mod[1],attibute)
            db.execute(sql)
            uf = db.fetchone()[0]
            temp.append(uf+rf)
        swat.append(temp)
    #print swat
    return swat,attibutes


if __name__ == '__main__':
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    getSwat(db)

