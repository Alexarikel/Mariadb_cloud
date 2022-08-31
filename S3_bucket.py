from asyncio.log import logger
import boto3
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="db_script.log", level=logging.INFO, format="%(asctime)s:%(name)s:%(funcName)s:%(message)s")

class S3_bucket:
    def __init__(self, bucket, accessid, accesskey):
        self.bucket = bucket
        self.accesskey = accesskey
        self.accessid = accessid
        self.s3_client = self.session()
       
    def session(self):
        try:
            s3_client = boto3.client('s3', aws_access_key_id=self.accessid, aws_secret_access_key=self.accesskey)
        except:
            logger.exception("Connection failed.")
        else:
            logger.info("Connected to s3 bucket.")
            return s3_client

    def list_bucket(self):
        objects = self.s3_client.list_objects_v2(Bucket=self.bucket)
        list_bucket = []
        for obj in objects['Contents']:
            obj = obj['Key']
            list_bucket.append(obj)
        return list_bucket
           
    def download (self, file_name, file_to_save):
        try:
            self.s3_client.download_file(self.bucket, file_name, file_to_save)
        except:
            logger.exception("An error occured while downloading files.")
            return False
        else:
            logger.info("Downloaded successfully.")

