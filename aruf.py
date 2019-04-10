import sqlite3
from arum import getSwat
import numpy as np


def findMaxPosition(aruf):
    temp=aruf[0][0]
    index=0

    for i in range(len(aruf)):
        for j in range(len(aruf[0])):
            if temp <aruf[i][j]:
                temp= aruf[i][j]
                index=j
    return index

def getAttribute(db):
    swat, attributes = getSwat(db)
    # print attributes
    """
    for x in swat:
        print x
    """
    sql = """select body from dcm"""

    db.execute(sql)
    res = db.fetchall()

    temp = []
    for x in res:
        x = x[0]
        x = x.split(",")
        for i in range(len(x)):
            x[i] = int(x[i])
        temp.append(x)
    # print temp

    swat = np.array(swat)
    dcm = np.array(temp)
    print "swat"
    print swat

    print ""

    print "Distance cost matrix"
    print dcm
    print " "
    aruf = np.zeros(shape=(4, 3))
    for i in range(len(dcm)):
        for j in range(len(swat[0])):
            #print dcm[i], swat[:, j]
            aruf[i][j] = int(sum(dcm[i] * swat[:, j]))

    print "Aruf matrix"
    print aruf
    print " "
    index = findMaxPosition(aruf)
    #print attributes[index]
    return attributes[index]


if __name__ == '__main__':
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    print getAttribute(db)
