import boto3
import ConfigParser

C = ConfigParser.RawConfigParser()
C.read('config.cfg')
filter_by_tag = C.get('aws', 'tags').split(',')


def init_session(profile, region):
    ses = boto3.session.Session(profile_name=profile,region_name=region)
    return ses.resource('ec2')

def list_instances(profile, region):
    ec2 = init_session(profile, region)
    list_of_instances = []

    for inst in ec2.instances.all():
        for tag in inst.tags:
            try:
                ec2Info = {}
                if tag['Key'] == 'Sistema':
                    for search_tag in filter_by_tag:
                        if tag['Value'] == search_tag:
                            for tag in inst.tags:
                                if tag['Key'] == 'Name':
                                    ec2Info['instName'] = tag['Value']
                                    ec2Info['instId'] = inst.id
                                    ec2Info['instType'] = inst.instance_type
                                    ec2Info['instState'] = inst.state['Name']
                                    ec2Info['instPrivIp'] = inst.private_ip_address
                                    ec2Info['Sistema'] = search_tag
                                    list_of_instances.append(ec2Info)
            except:
                continue
    return list_of_instances
