import ibm_db
from dotenv import load_dotenv
import os


load_dotenv()


conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bts01747;PWD=qA8l4hO4SAWfUHfV",'','')


def check_the_acc_info(user_email):
    sql = "SELECT * FROM donors WHERE user_email=?"
    stmt = ibm_db.prepare(conn,sql)
    ibm_db.bind_param(stmt,1,user_email)
    ibm_db.execute(stmt)
    donor_acc = ibm_db.fetch_assoc(stmt)

    user_sql = "SELECT * FROM users WHERE email=?"
    user_stmt = ibm_db.prepare(conn,user_sql)
    ibm_db.bind_param(user_stmt,1,user_email)
    ibm_db.execute(user_stmt)
    user_acc = ibm_db.fetch_assoc(user_stmt)

    result = ""
    if donor_acc and user_acc:
        result = 'donor-user-account'
    elif donor_acc:
        result = 'donor-account'
    elif user_acc:
        result = 'user-account'
    else:
        return False
    
    return result

