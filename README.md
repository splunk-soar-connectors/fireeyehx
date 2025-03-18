# FireEye HX

Publisher: Splunk Community \
Connector Version: 2.3.1 \
Product Vendor: FireEye \
Product Name: FireEye HX \
Minimum Product Version: 5.1.0

FireEye HX Endpoint Security

### Configuration variables

This table lists the configuration variables required to operate FireEye HX. These variables are specified when configuring a FireEye HX asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**hx_hostname** | required | string | HX Appliance URL Eg. https://hx.customer.com |
**hx_port** | required | numeric | HX Port. Eg. 3000 |
**hx_username** | required | string | HX API Username |
**hx_password** | required | password | HX API Password |
**zip_password** | optional | password | ZIP Archive Password |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[get system info](#action-get-system-info) - Get system information for an endpoint \
[quarantine device](#action-quarantine-device) - Request to contain the endpoint \
[get quarantine status](#action-get-quarantine-status) - Get the containment status for an endpoint \
[set quarantine approved](#action-set-quarantine-approved) - Approve containment request for host \
[unquarantine device](#action-unquarantine-device) - Containment cancellation for host \
[get acquisition status](#action-get-acquisition-status) - Get status of file acquisition \
[get triage](#action-get-triage) - Request Endpoint Host Triage Package \
[list device groups](#action-list-device-groups) - Retrieve a list of host sets in HX optionally filtered by name \
[get device group](#action-get-device-group) - List endpoints in a host set \
[list endpoints](#action-list-endpoints) - List and search the endpoints on HX \
[list acquisitions](#action-list-acquisitions) - Retrieve a list of all acquisitions with optional filters \
[start acquisition](#action-start-acquisition) - Request a file to be acquired into FireEye HX \
[get file](#action-get-file) - Pull the acquired file into Phantom Vault \
[get alert](#action-get-alert) - Pull single alert info by ID

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'get system info'

Get system information for an endpoint

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Agent ID to get system info of | string | `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.@created | string | | 2012-01-12T22:36:22Z |
action_result.data.\*.@uid | string | | A390C269-EE66-409E-B262-13F7D577588D |
action_result.data.\*.MAC | string | | a2-ac-75-70-ec-ae |
action_result.data.\*.OS | string | | Windows 7 Enterprise 7601 Service Pack 1 |
action_result.data.\*.OSbitness | string | | 32-bit |
action_result.data.\*.appCreated | string | | 2011-08-08T12:34:56Z |
action_result.data.\*.appVersion | string | | 1.0.1 |
action_result.data.\*.availphysical | string | | 1434546176 |
action_result.data.\*.biosInfo.biosDate | string | | 09/13/2011 |
action_result.data.\*.biosInfo.biosVersion | string | | Xen 4.1.1 |
action_result.data.\*.buildNumber | string | | 7601 |
action_result.data.\*.date | string | | 2014-08-09T06:55:07Z |
action_result.data.\*.directory | string | | C: |
action_result.data.\*.domain | string | `domain` | marketing.abc.com |
action_result.data.\*.gmtoffset | string | | -PT8H |
action_result.data.\*.hostname | string | `host name` | random_565_4 |
action_result.data.\*.installDate | string | | 2011-11-16T17:02:17Z |
action_result.data.\*.machine | string | | CORAL-WIN7SP164 |
action_result.data.\*.networkArray.networkInfo.\*.MAC | string | | a2-ac-75-70-ec-ae |
action_result.data.\*.networkArray.networkInfo.\*.adapter | string | | {C8CD9531-F96E-4B48-995E-9C34552FFDD0} |
action_result.data.\*.networkArray.networkInfo.\*.description | string | | Citrix PV Ethernet Adapter |
action_result.data.\*.networkArray.networkInfo.\*.dhcpLeaseExpires | string | | 2012-01-20T09:02:03Z |
action_result.data.\*.networkArray.networkInfo.\*.dhcpLeaseObtained | string | | 2012-01-12T09:02:03Z |
action_result.data.\*.networkArray.networkInfo.\*.dhcpServerArray.dhcpServer | string | `ip` | 10.6.6.7 |
action_result.data.\*.networkArray.networkInfo.\*.ipArray.ipInfo.ipAddress | string | `ip` | 10.6.6.6 |
action_result.data.\*.networkArray.networkInfo.\*.ipArray.ipInfo.ipv6Address | string | | ::1 |
action_result.data.\*.networkArray.networkInfo.\*.ipArray.ipInfo.ipv6SubnetMask | string | | FFFF:FFFF:FFFF:FC00:0:0:0:0 |
action_result.data.\*.networkArray.networkInfo.\*.ipArray.ipInfo.subnetMask | string | `ip` | 255.255.255.0 |
action_result.data.\*.networkArray.networkInfo.\*.ipGatewayArray.ipGateway | string | `ip` | 10.1.1.1 |
action_result.data.\*.patchLevel | string | | Service Pack 2 |
action_result.data.\*.primaryIpAddress | string | `ip` | 10.1.1.1 |
action_result.data.\*.procType | string | | Multiprocessor Free |
action_result.data.\*.processor | string | | Intel(R) Xeon(R) CPU X5670 @ 2.93GHz |
action_result.data.\*.productID | string | | 55041-050-0818515-86383 |
action_result.data.\*.productName | string | | Windows XP SP3 |
action_result.data.\*.regOrg | string | | FireEye |
action_result.data.\*.regOwner | string | | dgoodman |
action_result.data.\*.timezone | string | | Pacific Standard Time |
action_result.data.\*.timezoneDST | string | | Pacific Daylight Time |
action_result.data.\*.timezoneStandard | string | | Pacific Standard Time |
action_result.data.\*.totalphysical | string | | 2142883840 |
action_result.data.\*.uptime | string | | PT2468377S |
action_result.data.\*.user | string | | SYSTEM |
action_result.status | string | | success failed |
action_result.message | string | | Primary ip: 10.1.1.1, Hostname: random_565_4 |
action_result.summary.hostname | string | `host name` | random_565_4 |
action_result.summary.primary_ip | string | `ip` | 10.1.1.1 |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'quarantine device'

Request to contain the endpoint

Type: **contain** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Endpoint Agent ID you want to contain | string | `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.message | string | | Accepted |
action_result.data.\*.route | string | | /hx/api/v3/hosts/agent_id/containment |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get quarantine status'

Get the containment status for an endpoint

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Endpoint Agent ID you want to check the status | string | `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.\_id | string | | 96D2CB1414691242160B26 |
action_result.data.\*.contained_by_actor.\_id | numeric | | 1007 |
action_result.data.\*.contained_by_actor.username | string | `user name` | api_analyst_contain |
action_result.data.\*.contained_on | string | | 2014-10-30T17:47:22.261Z |
action_result.data.\*.excluded | boolean | | True False |
action_result.data.\*.last_sysinfo | string | | 2013-10-27T11:16:47.000Z |
action_result.data.\*.queued | boolean | | True False |
action_result.data.\*.requested_by_actor.\_id | numeric | | 1007 |
action_result.data.\*.requested_by_actor.username | string | `user name` | api_analyst_contain |
action_result.data.\*.requested_on | string | | 2014-10-30T17:47:22.261Z |
action_result.data.\*.state | string | | contain |
action_result.data.\*.state_update_time | string | | 2014-10-30T17:47:22.261Z |
action_result.data.\*.url | string | | /hx/api/v3/hosts/96D2CB1414691242160B26 |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'set quarantine approved'

Approve containment request for host

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Endpoint Agent ID you want to approve containment | string | `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.message | string | | Created |
action_result.data.\*.route | string | | /hx/api/v3/hosts/agent_id/containment |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'unquarantine device'

Containment cancellation for host

Type: **correct** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Endpoint Agent ID you want to cancel containment | string | `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | |
action_result.data | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get acquisition status'

Get status of file acquisition

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acquisition_id** | required | Acquisition ID from (get file) action to query status | string | `fireeyehx acquisition id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.acquisition_id | string | `fireeyehx acquisition id` | 2494 |
action_result.data.\*.\_id | numeric | | 2494 |
action_result.data.\*.\_revision | string | | 20180523191059963547881830 |
action_result.data.\*.alert | string | | |
action_result.data.\*.comment | string | | |
action_result.data.\*.condition | string | | |
action_result.data.\*.error_message | string | | The acquisition completed with issues. |
action_result.data.\*.external_id | string | | null |
action_result.data.\*.finish_time | string | | 2018-05-23T19:10:59.963Z |
action_result.data.\*.host.\_id | string | | E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.host.url | string | | /hx/api/v3/hosts/E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.indicator | string | | |
action_result.data.\*.md5 | string | `md5` | |
action_result.data.\*.message | string | | OK |
action_result.data.\*.req_filename | string | `file name` | NV4HPControllerSetup.exe |
action_result.data.\*.req_path | string | `file path` | C:\\Users\\aeh11\\AppData\\Local\\Temp\\1\\NVFiles_7e7bc015-0db1-4605-a9cf-9d81754054e9\\ |
action_result.data.\*.req_use_api | boolean | | True False |
action_result.data.\*.request_actor.\_id | numeric | | 1012 |
action_result.data.\*.request_actor.username | string | `user name` | bckapi |
action_result.data.\*.request_time | string | | 2018-05-23T19:10:00.000Z |
action_result.data.\*.route | string | | /hx/api/v3/acqs/files/id |
action_result.data.\*.state | string | | COMPLETE |
action_result.data.\*.url | string | | /hx/api/v3/acqs/files/2494 |
action_result.data.\*.zip_passphrase | string | | unzip-me |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get triage'

Request Endpoint Host Triage Package

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Agent ID to get Triage Package | string | `fireeyehx agentid` |
**req_timestamp** | optional | The triage collection time in ISO-8601_DATE format | string | |
**external_id** | optional | External correlation ID | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.parameter.external_id | string | | |
action_result.parameter.req_timestamp | string | | null |
action_result.data.\*.\_id | numeric | | 5 |
action_result.data.\*.\_revision | string | | 20141030174717969373100031 |
action_result.data.\*.alert.\_id | string | | |
action_result.data.\*.alert.url | string | | |
action_result.data.\*.condition.\_id | string | | |
action_result.data.\*.condition.url | string | | |
action_result.data.\*.error_message | string | | |
action_result.data.\*.external_id | string | | |
action_result.data.\*.finish_time | string | | |
action_result.data.\*.host.\_id | string | | F114BC21414691237913B9 |
action_result.data.\*.host.url | string | | /hx/api/v3/hosts/F114BC21414691237913B9 |
action_result.data.\*.indicator.\_id | string | | |
action_result.data.\*.indicator.url | string | | |
action_result.data.\*.md5 | string | `md5` | |
action_result.data.\*.message | string | | Created |
action_result.data.\*.request_actor.\_id | numeric | | 1002 |
action_result.data.\*.request_actor.username | string | `user name` | api_analyst |
action_result.data.\*.request_time | string | | 2014-10-30T17:47:17.000Z |
action_result.data.\*.request_time | string | | |
action_result.data.\*.route | string | | /hx/api/v3/hosts/agent_id/triages |
action_result.data.\*.state | string | | NEW |
action_result.data.\*.url | string | | /hx/api/v3/acqs/triages/5 |
action_result.status | string | | success failed |
action_result.message | string | | State: NEW, Id: 5 |
action_result.summary.id | numeric | | 5 |
action_result.summary.state | string | | NEW |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'list device groups'

Retrieve a list of host sets in HX optionally filtered by name

Type: **investigate** \
Read only: **True**

This action can retrieve a maximum of 100 host sets.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**name** | optional | Host set name for filtering | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.name | string | | |
action_result.data.\*.\_id | numeric | `fireeye hostsetid` | 1069 |
action_result.data.\*.\_revision | string | | |
action_result.data.\*.name | string | | |
action_result.data.\*.type | string | | venn static |
action_result.data.\*.url | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get device group'

List endpoints in a host set

Type: **investigate** \
Read only: **True**

This action can retrieve a maximum of 10000 endpoints in a host set.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host_set_id** | required | ID of the Host Set | string | `fireeyehx hostsetid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.host_set_id | string | `fireeyehx hostsetid` | |
action_result.data.\*.\_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.agent_version | string | | 1.0.1 |
action_result.data.\*.containment_missing_software | boolean | | True False |
action_result.data.\*.containment_queued | boolean | | True False |
action_result.data.\*.containment_state | string | | normal |
action_result.data.\*.domain | string | `domain` | hr.fireeye.com |
action_result.data.\*.excluded_from_containment | boolean | | True False |
action_result.data.\*.gmt_offset_seconds | numeric | | -28800 |
action_result.data.\*.hostname | string | `host name` | random_164_1 |
action_result.data.\*.last \_exploit_block | string | | |
action_result.data.\*.last_alert | string | | |
action_result.data.\*.last_alert_timestamp | string | | |
action_result.data.\*.last_audit_timestamp | string | | 2015-07-30T04:12:23.000Z |
action_result.data.\*.last_exploit_block_timestamp | string | | |
action_result.data.\*.last_poll_ip | string | | |
action_result.data.\*.last_poll_timestamp | string | | |
action_result.data.\*.message | string | | OK |
action_result.data.\*.os.bitness | string | | 32-bit |
action_result.data.\*.os.patch_level | string | | Service Pack 3 |
action_result.data.\*.os.product_name | string | | Windows XP SP1 |
action_result.data.\*.primary_ip_address | string | `ip` | 10.1.1.1 |
action_result.data.\*.primary_mac | string | | a2-ac-75-70-ec-ae |
action_result.data.\*.reported_clone | boolean | | True False |
action_result.data.\*.stats.acqs | numeric | | 0 |
action_result.data.\*.stats.alerting_conditions | numeric | | 0 |
action_result.data.\*.stats.alerts | numeric | | 0 |
action_result.data.\*.stats.exploit_alerts | numeric | | 0 |
action_result.data.\*.stats.exploit_blocks | numeric | | 0 |
action_result.data.\*.sysinfo.url | string | | /hx/api/v3/hosts/3805951439869103977B58/sysinfo |
action_result.data.\*.timezone | string | | Pacific Standard Time |
action_result.data.\*.url | string | | /hx/api/v3/hosts/3805951439869103977B58 |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'list endpoints'

List and search the endpoints on HX

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** | optional | Limit the number of hosts returned. (HX Defaults to 50) | numeric | |
**search** | optional | Search all hosts connected to the HX appliance. Search for hostname, IP address or Agent ID | string | `host name` `ip` `fireeyehx agentid` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.limit | numeric | | 50 |
action_result.parameter.search | string | `host name` `ip` `fireeyehx agentid` | |
action_result.data.\*.data.entries.\*.\_id | string | `fireeyehx agentid` | 3805951439869103977B58 |
action_result.data.\*.data.entries.\*.agent_version | string | | 1.0.1 |
action_result.data.\*.data.entries.\*.containment_missing_software | boolean | | True False |
action_result.data.\*.data.entries.\*.containment_queued | boolean | | True False |
action_result.data.\*.data.entries.\*.containment_state | string | | normal |
action_result.data.\*.data.entries.\*.domain | string | `domain` | hr.fireeye.com |
action_result.data.\*.data.entries.\*.excluded_from_containment | boolean | | True False |
action_result.data.\*.data.entries.\*.gmt_offset_seconds | numeric | | -28800 |
action_result.data.\*.data.entries.\*.hostname | string | `host name` | random_164_1 |
action_result.data.\*.data.entries.\*.last_alert | string | | |
action_result.data.\*.data.entries.\*.last_alert_timestamp | string | | |
action_result.data.\*.data.entries.\*.last_audit_timestamp | string | | 2015-07-30T04:12:23.000Z |
action_result.data.\*.data.entries.\*.last_exploit_block | string | | |
action_result.data.\*.data.entries.\*.last_exploit_block_timestamp | string | | |
action_result.data.\*.data.entries.\*.last_poll_ip | string | | |
action_result.data.\*.data.entries.\*.last_poll_timestamp | string | | |
action_result.data.\*.data.entries.\*.os.bitness | string | | 32-bit |
action_result.data.\*.data.entries.\*.os.patch_level | string | | Service Pack 3 |
action_result.data.\*.data.entries.\*.os.product_name | string | | Windows XP SP1 |
action_result.data.\*.data.entries.\*.primary_ip_address | string | `ip` | 10.1.1.1 |
action_result.data.\*.data.entries.\*.primary_mac | string | | a2-ac-75-70-ec-ae |
action_result.data.\*.data.entries.\*.reported_clone | boolean | | True False |
action_result.data.\*.data.entries.\*.stats.acqs | numeric | | 0 |
action_result.data.\*.data.entries.\*.stats.alerting_conditions | numeric | | 0 |
action_result.data.\*.data.entries.\*.stats.alerts | numeric | | 0 |
action_result.data.\*.data.entries.\*.stats.exploit_blocks | numeric | | 0 |
action_result.data.\*.data.entries.\*.sysinfo.url | string | | /hx/api/v3/hosts/3805951439869103977B58/sysinfo |
action_result.data.\*.data.entries.\*.timezone | string | | Pacific Standard Time |
action_result.data.\*.data.entries.\*.url | string | | /hx/api/v3/hosts/3805951439869103977B58 |
action_result.data.\*.data.limit | numeric | | 50 |
action_result.data.\*.data.message | string | | OK |
action_result.data.\*.data.offset | numeric | | 0 |
action_result.data.\*.data.route | string | | /hx/api/v3/hosts |
action_result.data.\*.data.total | numeric | | 5 |
action_result.data.\*.entries.\*.stats.exploit_alerts | numeric | | 0 |
action_result.status | string | | success failed |
action_result.message | string | | Matched endpoints: 1 |
action_result.summary.matched_endpoints | numeric | | 1 |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'list acquisitions'

Retrieve a list of all acquisitions with optional filters

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | optional | HX Agent ID for the host | string | `fireeyehx agentid` |
**req_filename** | optional | Name of the file acquired | string | `file name` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | E8kw2d9uRcjgkfDjWKQqnv |
action_result.parameter.req_filename | string | `file name` | NV4HPControllerSetup.exe |
action_result.data.\*.\_id | numeric | | 2494 |
action_result.data.\*.\_revision | string | | 20180523191000077103881827 |
action_result.data.\*.alert | string | | |
action_result.data.\*.comment | string | | |
action_result.data.\*.condition | string | | |
action_result.data.\*.error_message | string | | |
action_result.data.\*.external_id | string | | null |
action_result.data.\*.finish_time | string | | |
action_result.data.\*.host.\_id | string | | E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.host.url | string | | /hx/api/v3/hosts/E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.indicator | string | | |
action_result.data.\*.md5 | string | `md5` | |
action_result.data.\*.message | string | | Created |
action_result.data.\*.req_filename | string | `file name` | NV4HPControllerSetup.exe |
action_result.data.\*.req_path | string | `file path` | C:\\Users\\aeh11\\AppData\\Local\\Temp\\1\\NVFiles_7e7bc015-0db1-4605-a9cf-9d81754054e9\\ |
action_result.data.\*.req_use_api | boolean | | True False |
action_result.data.\*.request_actor.\_id | numeric | | 1012 |
action_result.data.\*.request_actor.username | string | `user name` | bckapi |
action_result.data.\*.request_time | string | | 2018-05-23T19:10:00.000Z |
action_result.data.\*.route | string | | /hx/api/v3/hosts/agent_id/files |
action_result.data.\*.state | string | | NEW COMPLETE |
action_result.data.\*.url | string | | /hx/api/v3/acqs/files/2494 |
action_result.data.\*.zip_passphrase | string | | unzip-me |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'start acquisition'

Request a file to be acquired into FireEye HX

Type: **generic** \
Read only: **False**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent_id** | required | HX Agent ID for the host | string | `fireeyehx agentid` |
**req_path** | required | Path of the file that you want to acquire | string | `file path` |
**req_filename** | required | Name of the file you want to acquire | string | `file name` |
**req_use_api** | optional | Whether to use RAW or API mode | boolean | |
**comment** | optional | General Comment | string | |
**external_id** | optional | External correlation ID from a SIEM solution | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.agent_id | string | `fireeyehx agentid` | E8kw2d9uRcjgkfDjWKQqnv |
action_result.parameter.comment | string | | null |
action_result.parameter.external_id | string | | null |
action_result.parameter.req_filename | string | `file name` | NV4HPControllerSetup.exe |
action_result.parameter.req_path | string | `file path` | C:\\Users\\aeh11\\AppData\\Local\\Temp\\1\\NVFiles_7e7bc015-0db1-4605-a9cf-9d81754054e9\\ |
action_result.parameter.req_use_api | boolean | | False True |
action_result.data.\*.\_id | numeric | | 2494 |
action_result.data.\*.\_revision | string | | 20180523191000077103881827 |
action_result.data.\*.alert | string | | |
action_result.data.\*.comment | string | | |
action_result.data.\*.condition | string | | |
action_result.data.\*.error_message | string | | |
action_result.data.\*.external_id | string | | null |
action_result.data.\*.finish_time | string | | |
action_result.data.\*.host.\_id | string | | E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.host.url | string | | /hx/api/v3/hosts/E8kw2d9uRcjgkfDjWKQqnv |
action_result.data.\*.indicator | string | | |
action_result.data.\*.md5 | string | `md5` | |
action_result.data.\*.message | string | | Created |
action_result.data.\*.req_filename | string | `file name` | NV4HPControllerSetup.exe |
action_result.data.\*.req_path | string | `file path` | C:\\Users\\aeh11\\AppData\\Local\\Temp\\1\\NVFiles_7e7bc015-0db1-4605-a9cf-9d81754054e9\\ |
action_result.data.\*.req_use_api | boolean | | True False |
action_result.data.\*.request_actor.\_id | numeric | | 1012 |
action_result.data.\*.request_actor.username | string | `user name` | bckapi |
action_result.data.\*.request_time | string | | 2018-05-23T19:10:00.000Z |
action_result.data.\*.route | string | | /hx/api/v3/hosts/agent_id/files |
action_result.data.\*.state | string | | NEW |
action_result.data.\*.url | string | | /hx/api/v3/acqs/files/2494 |
action_result.data.\*.zip_passphrase | string | | unzip-me |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get file'

Pull the acquired file into Phantom Vault

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acquisition_id** | required | HX Acquisition ID for the acquired file | string | `fireeyehx acquisition id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.acquisition_id | string | `fireeyehx acquisition id` | 2496 |
action_result.data.\*.container | numeric | | 544 |
action_result.data.\*.hash | string | `hash` | 0f3c4ff28f354aede202d54e9d1c5529a3bf87d8 |
action_result.data.\*.id | numeric | | 2 |
action_result.data.\*.message | string | | success failed |
action_result.data.\*.size | numeric | | 345088 |
action_result.data.\*.succeeded | boolean | | True False |
action_result.data.\*.vault_id | string | `vault id` | 0f3c4ff28f354aede202d54e9d1c5529a3bf87d8 |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'get alert'

Pull single alert info by ID

Type: **investigate** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**alert_id** | required | The ID of the alert to fetch data from | string | `fireeyehx alert id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.alert_id | string | `fireeyehx alert id` | 1110 |
action_result.data.\*.condition | string | | |
action_result.data.\*.condition.\_id | string | | |
action_result.data.\*.condition.url | string | `url` | |
action_result.data.\*.event_id | string | | |
action_result.data.\*.event_type | string | | fileWriteEvent |
action_result.data.\*.event_values | string | | |
action_result.data.\*.indicator | string | | |
action_result.data.\*.indicator.\_id | string | | |
action_result.data.\*.indicator.url | string | `url` | |
action_result.data.\*.md5values | string | `md5` | |
action_result.data.\*.source | string | | |
action_result.status | string | | success failed |
action_result.message | string | | |
action_result.summary | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
