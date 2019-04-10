from fragment import getFragments
import sqlite3


def loadSite(db):
    sql="select capacity,fragment_limit from sites"
    db.execute(sql)
    res = db.fetchall()
    result =[]
    for i in range(len(res)):
        temp=[]
        for j in range(len(res[i])):
            temp.append(res[i][j])
        result.append(temp)
    return result


def getAveragecost(db,attribute,mod):
    sql="""select predicate*frequency from arum where mod = "{}" and attribute= "{}" order BY arum_id""".format(mod,attribute)
    db.execute(sql)
    res=db.fetchall()
    return res


def calcuateUC(ucost,index,length):

    max_index=0
    max_total=0
    for i in range(length):
        #print ucost[index][0]+ucost[index+3][0], max_total ,ucost[index][0]+ucost[index+3][0] > max_total
        if ucost[index][0]+ucost[index+3][0] > max_total :
            max_index = i
            max_total=ucost[index][0]+ucost[index+3][0]
        index = index+6

    return max_index+1



def calculateAverage(cost,index):
    total=0
    while index < len(cost):
        #print total ,index,cost[index][0]
        total = total+ cost[index][0]
        index+=3
    return total/len(cost)


def updateSite(site,site_no,frag_id, result):
    for i in range(len(site)):
        if i+1 in site_no and site[i][1]>0:
            print "fragment ",frag_id ,"--> site ",i+1
            result[i].append(frag_id)
            site[i][1] = int(site[i][1])-1
    print ""
    return site,result



def getAllocation(db):
    attribute,f1,f2,f3=getFragments(db)
    rcost=getAveragecost(db,attribute,'rf')
    ucost=getAveragecost(db,attribute,'uf')
    site=loadSite(db)

    result=[]
    for i in range(len(site)):
        result.append([])

    for i in range(3):
        site_no=[]
        if calculateAverage(rcost,i) < calculateAverage(ucost,i):
            site_no.append(calcuateUC(ucost,i,len(site)))
        else:
            for j in range(len(site)):
                site_no.append(j+1)

        #print site_no
        #print site
        site,result=updateSite(site,site_no,i+1,result)

    for i in range(len(result)):
        print "site {} --> fragments {}".format(i+1,result[i])





if __name__ == '__main__':
    db_name = 'data'
    conn = sqlite3.connect('{}.db'.format(db_name))
    db = conn.cursor()
    getAllocation(db)
