import boto3
import csv
from tabulate import tabulate
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
s3=session.client('s3')

#Getting Bucket 
data=s3_client.list_multipart_uploads(Bucket="xxxx")
print (data)

s3multipartdata=[]
while True:
    paginator=s3.get_paginator('list_multipart_uploads')
    responses=paginator.paginate(Bucket,MaxUploads=pagesize,KeyMarker=NextKeyMarker)
    
    #Iterting through each response and the Uploads
    #NextKeyMarker from the response should be passed to get the next list of MultiPart Uploads


    for response in responses:
        try:
            incompleteuploads=response['Uploads']
            NextKeyMarker=response['NextKeyMarker']
            i=i+1
            if i<=pages:
                for row in incompleteuploads:
                    #There are also other fiels that can be returned in responses
                    initator=incompleteuploads['Initiator']['ID']
                    partname=incompleteuploads['Key']
                    date=incompleteuploads['Initiated']
                    s3multipartdata.append([initator,partname,date])
            else:
                headers=['Initiator','PartName','Date']

                #Writing to CSV
                with open(csvname,'w',newline='') as csvfile:
                filewriter=csv.writer(csvfile,delimiter=',')
                
                #Getting the list of MultiPart Uploads
                rowcount=len(s3multipartdata)
                filewriter.writerow(headers)

              
                for x in range(0,rowcount):
                    filewriter.writerow(data[i])

        except Exception as error:
            headers=['Initiator','PartName','Date']

            #Writing to CSV
            with open(csvname,'w',newline='') as csvfile:
                filewriter=csv.writer(csvfile,delimiter=',')
                
               
                rowcount=len(s3multipartdata)
                filewriter.writerow(headers)

              
                for x in range(0,rowcount):
                    filewriter.writerow(data[i])