import json
import boto3
import time

"""
The Sample data stored in variable api-data is pushed every 5 sec interval to Firehose using the boto3 lib
The data is converted to bytes and pushed to firehose stream
The firehose sream name is to be provied at DeliveryStreamName 
"""
n = 0
while True:
    # sample data
    apidata = str(n) + """2|8777702034351210208495|best_recs|42545|Mobile is designed to save you money|1"""

    # creating a firehose client naming it as KF
    kf = boto3.client("firehose",region_name='us-east-1')
    # converting data to bytes before pushing to firehose stream
    print("converting data to bytes")
    enc = str.encode(apidata)
    try:
        response = kf.put_record(
                DeliveryStreamName='FireHose-API',
                Record={
                    'Data': enc
                }
        )
        print(response)
    except:
         print("cannot push data to kinesis")
    n = n + 1
    time.sleep(5)
