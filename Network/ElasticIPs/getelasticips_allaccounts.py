import boto3
import csv

#To get the list of all the accounts 
#1. This script goes through each account and gets the list of Elastic IPs
#2. This script can be also modified to get Elastic IPs for a certain account


# Configuration
ROLE_NAME = "YourAssumedRoleName"
TARGET_REGION = "us-east-1"
OUTPUT_FILE = "organization_eips.csv"

# Initialize the Organizations client
org_client = boto3.client('organizations')
sts_client = boto3.client('sts')

# Prepare the CSV file and header
csv_file = open(OUTPUT_FILE, mode='w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Account ID', 'Account Name', 'Public IP', 'Allocation ID', 'Instance ID'])

# List all active accounts in the organization
paginator = org_client.get_paginator('list_accounts')
for page in paginator.paginate():
    for account in page['Accounts']:
        if account['Status'] == 'ACTIVE':
            account_id = account['Id']
            account_name = account['Name']
            role_arn = f"arn:aws:iam::{account_id}:role/{ROLE_NAME}"
            
            try:
                # Assume the role in the target account
                assumed_role = sts_client.assume_role(
                    RoleArn=role_arn,
                    RoleSessionName="EIPScannerSession"
                )
                
                # Extract temporary credentials
                creds = assumed_role['Credentials']
                
                # Create EC2 client for the specific account
                ec2 = boto3.client(
                    'ec2',
                    region_name=TARGET_REGION,
                    aws_access_key_id=creds['AccessKeyId'],
                    aws_secret_access_key=creds['SecretAccessKey'],
                    aws_session_token=creds['SessionToken']
                )
                
                # Get EIPs
                addresses = ec2.describe_addresses()['Addresses']
                
                for addr in addresses:
                    public_ip = addr.get('PublicIp')
                    allocation_id = addr.get('AllocationId')
                    instance_id = addr.get('InstanceId', 'N/A')
                    
                    # Write row to CSV
                    csv_writer.writerow([account_id, account_name, public_ip, allocation_id, instance_id])
                
            except Exception as e:
                print(f"Error accessing account {account_id}: {e}")

# Clean up
csv_file.close()
print(f"Report generated successfully: {OUTPUT_FILE}")