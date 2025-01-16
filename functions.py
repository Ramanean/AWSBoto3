import boto3
from tabulate import tabulate
import sys
import csv


def outputtable(data,headers):
    
    rowheaders=[]
    for header in headers:
        header=header.replace(" ","\n")
        tableheaders.append(header)

    table=tabulate(
        headers=rowheaders,
        tablefmt="psql",
        floatfmt=".1f"
        numalign="center"
        stralign="center"

    )

###########################################################
# Creates a CSV by passing output                          
# Rows and rowheaders should be passed as a list
###########################################################
def createcsv(outputcsv,data,rowheaders):
    with open(csvfile,'w',newline='') as csvfile:
        filewriter=csv.writer(csvfile,delimiter=',')
        
        #Getting ReportData
        rowcount=len(data)
        filewriter.writerow(rowheaders)

        #Writing the data to a CSV file
        for x in range(0,rowcount):
            filewriter.writerow(data[i])