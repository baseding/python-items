#!/usr/bin/env python

import json
import ruamel.yaml as yaml
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest, DescribeDomainRecordInfoRequest, AddDomainRecordRequest, DescribeDomainsRequest

#from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
#from aliyunsdkecs.request.v20140526 import StopInstanceRequest

# 1. Create AcsClient Instantance
client = AcsClient(
    "LTAIp8HQFmAC0FIo", 
    "PwrU39MPMiO6NE4PaznxQ4Zi6CC6E2",
    "cn-shanghai",
);

# 2. Create request, with params 
## DescribeDomainRecords
#request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
#request.set_DomainName("azza.com.cn")
#request.set_accept_format('json')

request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
request.set_RR('test1')
request.set_Type('A')
request.set_Value('9.9.9.9')
request.set_RecordId('3427090946544640')
request.set_TTL('600')
request.set_accept_format('json')



# 3. Send API request,and print response 
#response = client.do_action_with_exception(request)
#response = json.loads(client.do_action_with_exception(request)).get('Domains').get('DomainId')
response = yaml.safe_load(client.do_action_with_exception(request))

print(response)

