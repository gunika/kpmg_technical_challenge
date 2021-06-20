import boto3
		
def ec2InstanceDetails(accessKey, secretAccessKey, instanceId):
    session = boto3.Session(accessKey, secretAccessKey)
    service = session.client('ec2')
    response = service.describe_instances(InstanceIds=[instanceId])
	return response
	
