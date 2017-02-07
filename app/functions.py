import boto3

def init_session(profile, region):
    ses = boto3.session.Session(profile_name=profile,region_name=region)
    return ses.resource('ec2')

def listInstances(profile, region):
    ec2 = init_session(profile, region)
    arrInstances = []
    for inst in ec2.instances.all():
        try:
            if inst.tags is None:
                continue
            for tag in inst.tags:
                if tag['Key'] == 'Name':
                    ec2Info = {}
                    ec2Info['instName'] = tag['Value']
                    ec2Info['instId'] = (inst.id)
                    ec2Info['instType'] = inst.instance_type
                    ec2Info['instState'] = inst.state['Name']
                    ec2Info['instPrivIp'] = inst.private_ip_address
                    arrInstances.append(ec2Info)
        except:
            continue
    return arrInstances
