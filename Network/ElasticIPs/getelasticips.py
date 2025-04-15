############################################################
##         Created by @RamaneanAWS/@RamaneanTech                                 
##
#############################################################

import boto3
import csv
import tabulate
import sys
import csv

""" 
Step1: Getting the Arguments like AccessKey, SecretKey, S3 BucketName and CSV FileName
Step2: Authentication to AWS
Step3: Getting Multipart Uploads
Step4: Iterating through Multipart Uploads using Paginator
Step5: Writing to CSV if  the list

 """


#Arguments using Access and Secret Key
#PageSize refers to maxResults returned in each pagination 
#Pages refer to no of the pagination requests 

accesskey=sys.argv[1]
secretaccesskey=sys.argv[2]
bucketname=sys.argv[3]
csvname=sys.argv[4]
pagesize=1000
pages=100 

#Authentication
session=boto3.session(aws_access_key_id=AccessKeyId,aws_secret_access_key=SecretAccessKey)

#Creating session for ElasticIPs