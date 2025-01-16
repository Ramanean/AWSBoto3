import boto3

#Creating AWS Session by using Keys
def createsession_keys(AccessKeyId,SecretAccessKey):
    boto3_session=boto3.session(aws_access_key_id=AccessKeyId,aws_secret_access_key=SecretAccessKey)
    return boto3_session