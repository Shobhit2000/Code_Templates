import MySQLdb as mdb
import MySQLdb.cursors

# Database Settings
DB_ONE = {'DHOST': localhost,
          'DPORT': 8080,
          'USER': "dashboard",
          'PASS': "p*****"}


# General Functions

def connect_to_db(DB_SETTINGS):
    """
    Connect to a database
    Returns a connection object
    """
    DBS = DB_SETTINGS
    con = mdb.connect(user=DBS['USER'], passwd=DBS['PASS'], host=DBS['HOST'],
                      port=DBS['PORT'], cursorclass=MySQLdb.cursors.DictCursor,
                      charset="utf8", use_unicode=True)
    return con


def run_query(query, con):
    '''
    Execute a query
    Returns a results set
    '''
    cur = con.cursor()
    cur.execute(query)
    result_set = cur.fetchall()
    return result_set


def close(con):
    '''
    Close a db connection
    '''
    con.close()
