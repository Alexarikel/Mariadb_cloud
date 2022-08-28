import os
import os.path
import sys
from S3_bucket import S3_bucket
from Db_operations import Db_operations


ACCESSID = sys.argv[1]
ACCESSKEY = sys.argv[2]
USER = sys.argv[3]
PASSWORD = sys.argv[4]
HOST = sys.argv[5]
PORT = sys.argv[6]
DATABASE = sys.argv[7]
TABLE = sys.argv[8]
UPDATED = sys.argv[9]
BUCKET = sys.argv[10]

READ_AND_APPEND = "a+"

def duplicated_files(list_bucket, client_bucket, conf):
    for obj in list_bucket:
        with open(UPDATED, mode=READ_AND_APPEND) as updated:
            updated.seek(os.SEEK_SET)
            lines = [line.strip() for line in updated.readlines()]
            if not obj in lines:
                updated.write(f"{obj}\n")
                client_bucket.download(obj, obj)
                conf.insert(TABLE, obj)
                os.remove(obj)

     
if __name__ == "__main__":
    client_bucket = S3_bucket(BUCKET, ACCESSID, ACCESSKEY)
    conf = Db_operations(USER, PASSWORD, HOST, PORT, DATABASE)
    list_bucket = client_bucket.list_bucket()
    duplicated_files(list_bucket, client_bucket, conf)
    conf.conn.close()
