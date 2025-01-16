import boto3
import csv
from functions import outputtable,createcsv
from authentication import session

#Arguments
accesskey=sys.argv[1]
secretaccesskey=sys.argv[2]
bucketname=sys.argv[3]

session=boto3_session(accesskey,secretaccesskey)
s3_client=session.client('s3')

data=s3_client.list_multipart_uploads(Bucket="xxxx")
print (data)

