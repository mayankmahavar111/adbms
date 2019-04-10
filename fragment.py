from aruf import getAttribute
import sqlite3


def executeQuery(db,attribute,predicate,operator):
    sql="""select * from employee where {} {} {} """.format(attribute,operator,predicate)
    print sql
    db.execute(sql)
    res=db.fetchall()
    for x in res:
        print x
    print ""
    return res

def getPredicate(attribute,db):
    sql="""select avg({}) from employee""".format(attribute)
    db.execute(sql)
    average=int(db.fetchone()[0])
    sql ="""select {} from employee""".format(attribute)
    db.execute(sql)
    res=db.fetchall()
    temp=res[0][0]
    for x in res:
        x=x[0]
        if abs(temp-average) > abs(x-average):
            temp=x
    return temp

def getFragments(db):
    attribute=getAttribute(db)
    predicate=getPredicate(attribute,db)
    print "deciding attribute :",attribute
    print "predicate:",predicate
    f1=executeQuery(db,attribute,predicate,'>')
    f2=executeQuery(db,attribute,predicate,'<')
    f3=executeQuery(db,attribute,predicate,'=')



   # print f1,'\n',f2,'\n',f3,'\n'

    """
    print "f1 -> s4"
    print "f2 -> s1,s2,s3,s4"
    print "f3 -> s1,s2,s4"
    """

    return attribute,f1,f2,f3

if __name__ == '__main__':
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    getFragments(db)
