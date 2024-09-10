import psycopg2

con = psycopg2.connect(host='localhost', database='residents',
user='user', password='user')
    
def select_all():
    cur = con.cursor()
    cur.execute('select * from "Resident" r ')
    recset = cur.fetchall()
    print(recset)
    con.close()

def select_resident_id():
    cur = con.cursor()
    script = 'SELECT id FROM "Resident" r limit 1'
    cur.execute(script)
    recset = cur.fetchone()
    return ''.join(recset)