#!/usr/bin/env python

import json
import ruamel.yaml as yaml
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest, DescribeDomainRecordInfoRequest, AddDomainRecordRequest, DescribeDomainsRequest

# 1. Create AcsClient Instantance
client = AcsClient(
    "LTAIp8HQFmAC0FIo", 
    "PwrU39MPMiO6NE4PaznxQ4Zi6CC6E2",
    "cn-shanghai",
);

# 2. Create request, with params 
request = DescribeDomainsRequest.DescribeDomainsRequest()
request.set_accept_format('json')
print request


# 3. Send API request,and print response 
#response = client.do_action_with_exception(request)
#response = json.loads(client.do_action_with_exception(request)).get('Domains').get('DomainId')
response = yaml.safe_load(client.do_action_with_exception(request)).get('Domains')

print response
print response["Domain"][0]
print response["Domain"][0]["DomainName"]
