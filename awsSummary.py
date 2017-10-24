import json
import boto3

#instantiate
ec2 = boto3.client('ec2')

def getRegions():
    #get all regions from AWS
    regions = ec2.describe_regions()
    regions = regions["Regions"]
    #send through each region to getInstances
    for region in regions:
        getInstances(region)

def getInstances(region):
    #format region to only contain the region name, nothing else
    region = region['RegionName']
    #switch regions and get instances
    ec2Region = boto3.client('ec2', region_name=region)
    instances = ec2Region.describe_instances()
    #create file with the name of the region, write the instance details, then close
    newJson = open(region+".json","w+")
    newJson.write(str(instances))
    newJson.close()
    return None

def main():
    getRegions()

#lazy way to start program
main()
