[comment]: # "Auto-generated SOAR connector documentation"
# FireEye HX

Publisher: Splunk Community  
Connector Version: 2\.1\.1  
Product Vendor: FireEye  
Product Name: FireEye HX  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.10\.0\.40961  

FireEye HX Endpoint Security

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a FireEye HX asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**hx\_hostname** |  required  | string | HX Appliance URL Eg\. https\://hx\.customer\.com
**hx\_port** |  required  | numeric | HX Port\. Eg\. 3000
**hx\_username** |  required  | string | HX API Username
**hx\_password** |  required  | password | HX API Password
**zip\_password** |  optional  | password | ZIP Archive Password

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[get system info](#action-get-system-info) - Get system information for an endpoint  
[quarantine device](#action-quarantine-device) - Request to contain the endpoint  
[get quarantine status](#action-get-quarantine-status) - Get the containment status for an endpoint  
[set quarantine approved](#action-set-quarantine-approved) - Approve containment request for host  
[unquarantine device](#action-unquarantine-device) - Containment cancellation for host  
[get acquisition status](#action-get-acquisition-status) - Get status of file acquisition  
[get triage](#action-get-triage) - Request Endpoint Host Triage Package  
[list device groups](#action-list-device-groups) - Retrieve a list of host sets in HX optionally filtered by name  
[get device group](#action-get-device-group) - List endpoints in a host set  
[list endpoints](#action-list-endpoints) - List and search the endpoints on HX  
[list acquisitions](#action-list-acquisitions) - Retrieve a list of all acquisitions with optional filters  
[start acquisition](#action-start-acquisition) - Request a file to be acquired into FireEye HX  
[get file](#action-get-file) - Pull the acquired file into Phantom Vault  
[get alert](#action-get-alert) - Pull single alert info by ID  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'get system info'
Get system information for an endpoint

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Agent ID to get system info of | string |  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.\@created | string | 
action\_result\.data\.\*\.\@uid | string | 
action\_result\.data\.\*\.MAC | string | 
action\_result\.data\.\*\.OS | string | 
action\_result\.data\.\*\.OSbitness | string | 
action\_result\.data\.\*\.appCreated | string | 
action\_result\.data\.\*\.appVersion | string | 
action\_result\.data\.\*\.availphysical | string | 
action\_result\.data\.\*\.biosInfo\.biosDate | string | 
action\_result\.data\.\*\.biosInfo\.biosVersion | string | 
action\_result\.data\.\*\.buildNumber | string | 
action\_result\.data\.\*\.date | string | 
action\_result\.data\.\*\.directory | string | 
action\_result\.data\.\*\.domain | string |  `domain` 
action\_result\.data\.\*\.gmtoffset | string | 
action\_result\.data\.\*\.hostname | string |  `host name` 
action\_result\.data\.\*\.installDate | string | 
action\_result\.data\.\*\.machine | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.MAC | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.adapter | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.description | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.dhcpLeaseExpires | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.dhcpLeaseObtained | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.dhcpServerArray\.dhcpServer | string |  `ip` 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.ipArray\.ipInfo\.ipAddress | string |  `ip` 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.ipArray\.ipInfo\.ipv6Address | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.ipArray\.ipInfo\.ipv6SubnetMask | string | 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.ipArray\.ipInfo\.subnetMask | string |  `ip` 
action\_result\.data\.\*\.networkArray\.networkInfo\.\*\.ipGatewayArray\.ipGateway | string |  `ip` 
action\_result\.data\.\*\.patchLevel | string | 
action\_result\.data\.\*\.primaryIpAddress | string |  `ip` 
action\_result\.data\.\*\.procType | string | 
action\_result\.data\.\*\.processor | string | 
action\_result\.data\.\*\.productID | string | 
action\_result\.data\.\*\.productName | string | 
action\_result\.data\.\*\.regOrg | string | 
action\_result\.data\.\*\.regOwner | string | 
action\_result\.data\.\*\.timezone | string | 
action\_result\.data\.\*\.timezoneDST | string | 
action\_result\.data\.\*\.timezoneStandard | string | 
action\_result\.data\.\*\.totalphysical | string | 
action\_result\.data\.\*\.uptime | string | 
action\_result\.data\.\*\.user | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.hostname | string |  `host name` 
action\_result\.summary\.primary\_ip | string |  `ip` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'quarantine device'
Request to contain the endpoint

Type: **contain**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Endpoint Agent ID you want to contain | string |  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get quarantine status'
Get the containment status for an endpoint

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Endpoint Agent ID you want to check the status | string |  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.\_id | string | 
action\_result\.data\.\*\.contained\_by\_actor\.\_id | numeric | 
action\_result\.data\.\*\.contained\_by\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.contained\_on | string | 
action\_result\.data\.\*\.excluded | boolean | 
action\_result\.data\.\*\.last\_sysinfo | string | 
action\_result\.data\.\*\.queued | boolean | 
action\_result\.data\.\*\.requested\_by\_actor\.\_id | numeric | 
action\_result\.data\.\*\.requested\_by\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.requested\_on | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.state\_update\_time | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'set quarantine approved'
Approve containment request for host

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Endpoint Agent ID you want to approve containment | string |  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'unquarantine device'
Containment cancellation for host

Type: **correct**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Endpoint Agent ID you want to cancel containment | string |  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.data | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get acquisition status'
Get status of file acquisition

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acquisition\_id** |  required  | Acquisition ID from \(get file\) action to query status | string |  `fireeyehx acquisition id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.acquisition\_id | string |  `fireeyehx acquisition id` 
action\_result\.data\.\*\.\_id | numeric | 
action\_result\.data\.\*\.\_revision | string | 
action\_result\.data\.\*\.alert | string | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.condition | string | 
action\_result\.data\.\*\.error\_message | string | 
action\_result\.data\.\*\.external\_id | string | 
action\_result\.data\.\*\.finish\_time | string | 
action\_result\.data\.\*\.host\.\_id | string | 
action\_result\.data\.\*\.host\.url | string | 
action\_result\.data\.\*\.indicator | string | 
action\_result\.data\.\*\.md5 | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.req\_filename | string |  `file name` 
action\_result\.data\.\*\.req\_path | string |  `file path` 
action\_result\.data\.\*\.req\_use\_api | boolean | 
action\_result\.data\.\*\.request\_actor\.\_id | numeric | 
action\_result\.data\.\*\.request\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.request\_time | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.data\.\*\.zip\_passphrase | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get triage'
Request Endpoint Host Triage Package

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Agent ID to get Triage Package | string |  `fireeyehx agentid` 
**req\_timestamp** |  optional  | The triage collection time in ISO\-8601\_DATE format | string | 
**external\_id** |  optional  | External correlation ID | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.parameter\.external\_id | string | 
action\_result\.parameter\.req\_timestamp | string | 
action\_result\.data\.\*\.\_id | numeric | 
action\_result\.data\.\*\.\_revision | string | 
action\_result\.data\.\*\.alert\.\_id | string | 
action\_result\.data\.\*\.alert\.url | string | 
action\_result\.data\.\*\.condition\.\_id | string | 
action\_result\.data\.\*\.condition\.url | string | 
action\_result\.data\.\*\.error\_message | string | 
action\_result\.data\.\*\.external\_id | string | 
action\_result\.data\.\*\.finish\_time | string | 
action\_result\.data\.\*\.host\.\_id | string | 
action\_result\.data\.\*\.host\.url | string | 
action\_result\.data\.\*\.indicator\.\_id | string | 
action\_result\.data\.\*\.indicator\.url | string | 
action\_result\.data\.\*\.md5 | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.request\_actor\.\_id | numeric | 
action\_result\.data\.\*\.request\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.request\_time | string | 
action\_result\.data\.\*\.request\_time | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.id | numeric | 
action\_result\.summary\.state | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list device groups'
Retrieve a list of host sets in HX optionally filtered by name

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**name** |  optional  | Host set name for filtering | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.name | string | 
action\_result\.data\.\*\.\_id | numeric |  `fireeye hostsetid` 
action\_result\.data\.\*\.\_revision | string | 
action\_result\.data\.\*\.name | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get device group'
List endpoints in a host set

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host\_set\_id** |  required  | ID of the Host Set | string |  `fireeyehx hostsetid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.host\_set\_id | string |  `fireeyehx hostsetid` 
action\_result\.data\.\*\.\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.agent\_version | string | 
action\_result\.data\.\*\.containment\_missing\_software | boolean | 
action\_result\.data\.\*\.containment\_queued | boolean | 
action\_result\.data\.\*\.containment\_state | string | 
action\_result\.data\.\*\.domain | string |  `domain` 
action\_result\.data\.\*\.excluded\_from\_containment | boolean | 
action\_result\.data\.\*\.gmt\_offset\_seconds | numeric | 
action\_result\.data\.\*\.hostname | string |  `host name` 
action\_result\.data\.\*\.last \_exploit\_block | string | 
action\_result\.data\.\*\.last\_alert | string | 
action\_result\.data\.\*\.last\_alert\_timestamp | string | 
action\_result\.data\.\*\.last\_audit\_timestamp | string | 
action\_result\.data\.\*\.last\_exploit\_block\_timestamp | string | 
action\_result\.data\.\*\.last\_poll\_ip | string | 
action\_result\.data\.\*\.last\_poll\_timestamp | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.os\.bitness | string | 
action\_result\.data\.\*\.os\.patch\_level | string | 
action\_result\.data\.\*\.os\.product\_name | string | 
action\_result\.data\.\*\.primary\_ip\_address | string |  `ip` 
action\_result\.data\.\*\.primary\_mac | string | 
action\_result\.data\.\*\.reported\_clone | boolean | 
action\_result\.data\.\*\.stats\.acqs | numeric | 
action\_result\.data\.\*\.stats\.alerting\_conditions | numeric | 
action\_result\.data\.\*\.stats\.alerts | numeric | 
action\_result\.data\.\*\.stats\.exploit\_alerts | numeric | 
action\_result\.data\.\*\.stats\.exploit\_blocks | numeric | 
action\_result\.data\.\*\.sysinfo\.url | string | 
action\_result\.data\.\*\.timezone | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list endpoints'
List and search the endpoints on HX

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**limit** |  optional  | Limit the number of hosts returned\. \(HX Defaults to 50\) | numeric | 
**search** |  optional  | Search all hosts connected to the HX appliance\. Search for hostname, IP address or Agent ID | string |  `host name`  `ip`  `fireeyehx agentid` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.limit | numeric | 
action\_result\.parameter\.search | string |  `host name`  `ip`  `fireeyehx agentid` 
action\_result\.data\.\*\.data\.entries\.\*\.\_id | string |  `fireeyehx agentid` 
action\_result\.data\.\*\.data\.entries\.\*\.agent\_version | string | 
action\_result\.data\.\*\.data\.entries\.\*\.containment\_missing\_software | boolean | 
action\_result\.data\.\*\.data\.entries\.\*\.containment\_queued | boolean | 
action\_result\.data\.\*\.data\.entries\.\*\.containment\_state | string | 
action\_result\.data\.\*\.data\.entries\.\*\.domain | string |  `domain` 
action\_result\.data\.\*\.data\.entries\.\*\.excluded\_from\_containment | boolean | 
action\_result\.data\.\*\.data\.entries\.\*\.gmt\_offset\_seconds | numeric | 
action\_result\.data\.\*\.data\.entries\.\*\.hostname | string |  `host name` 
action\_result\.data\.\*\.data\.entries\.\*\.last\_alert | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_alert\_timestamp | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_audit\_timestamp | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_exploit\_block | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_exploit\_block\_timestamp | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_poll\_ip | string | 
action\_result\.data\.\*\.data\.entries\.\*\.last\_poll\_timestamp | string | 
action\_result\.data\.\*\.data\.entries\.\*\.os\.bitness | string | 
action\_result\.data\.\*\.data\.entries\.\*\.os\.patch\_level | string | 
action\_result\.data\.\*\.data\.entries\.\*\.os\.product\_name | string | 
action\_result\.data\.\*\.data\.entries\.\*\.primary\_ip\_address | string |  `ip` 
action\_result\.data\.\*\.data\.entries\.\*\.primary\_mac | string | 
action\_result\.data\.\*\.data\.entries\.\*\.reported\_clone | boolean | 
action\_result\.data\.\*\.data\.entries\.\*\.stats\.acqs | numeric | 
action\_result\.data\.\*\.data\.entries\.\*\.stats\.alerting\_conditions | numeric | 
action\_result\.data\.\*\.data\.entries\.\*\.stats\.alerts | numeric | 
action\_result\.data\.\*\.data\.entries\.\*\.stats\.exploit\_blocks | numeric | 
action\_result\.data\.\*\.data\.entries\.\*\.sysinfo\.url | string | 
action\_result\.data\.\*\.data\.entries\.\*\.timezone | string | 
action\_result\.data\.\*\.data\.entries\.\*\.url | string | 
action\_result\.data\.\*\.data\.limit | numeric | 
action\_result\.data\.\*\.data\.message | string | 
action\_result\.data\.\*\.data\.offset | numeric | 
action\_result\.data\.\*\.data\.route | string | 
action\_result\.data\.\*\.data\.total | numeric | 
action\_result\.data\.\*\.entries\.\*\.stats\.exploit\_alerts | numeric | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary\.matched\_endpoints | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'list acquisitions'
Retrieve a list of all acquisitions with optional filters

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  optional  | HX Agent ID for the host | string |  `fireeyehx agentid` 
**req\_filename** |  optional  | Name of the file acquired | string |  `file name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.parameter\.req\_filename | string |  `file name` 
action\_result\.data\.\*\.\_id | numeric | 
action\_result\.data\.\*\.\_revision | string | 
action\_result\.data\.\*\.alert | string | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.condition | string | 
action\_result\.data\.\*\.error\_message | string | 
action\_result\.data\.\*\.external\_id | string | 
action\_result\.data\.\*\.finish\_time | string | 
action\_result\.data\.\*\.host\.\_id | string | 
action\_result\.data\.\*\.host\.url | string | 
action\_result\.data\.\*\.indicator | string | 
action\_result\.data\.\*\.md5 | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.req\_filename | string |  `file name` 
action\_result\.data\.\*\.req\_path | string |  `file path` 
action\_result\.data\.\*\.req\_use\_api | boolean | 
action\_result\.data\.\*\.request\_actor\.\_id | numeric | 
action\_result\.data\.\*\.request\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.request\_time | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.data\.\*\.zip\_passphrase | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'start acquisition'
Request a file to be acquired into FireEye HX

Type: **generic**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**agent\_id** |  required  | HX Agent ID for the host | string |  `fireeyehx agentid` 
**req\_path** |  required  | Path of the file that you want to acquire | string |  `file path` 
**req\_filename** |  required  | Name of the file you want to acquire | string |  `file name` 
**req\_use\_api** |  optional  | Whether to use RAW or API mode | boolean | 
**comment** |  optional  | General Comment | string | 
**external\_id** |  optional  | External correlation ID from a SIEM solution | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.agent\_id | string |  `fireeyehx agentid` 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.external\_id | string | 
action\_result\.parameter\.req\_filename | string |  `file name` 
action\_result\.parameter\.req\_path | string |  `file path` 
action\_result\.parameter\.req\_use\_api | boolean | 
action\_result\.data\.\*\.\_id | numeric | 
action\_result\.data\.\*\.\_revision | string | 
action\_result\.data\.\*\.alert | string | 
action\_result\.data\.\*\.comment | string | 
action\_result\.data\.\*\.condition | string | 
action\_result\.data\.\*\.error\_message | string | 
action\_result\.data\.\*\.external\_id | string | 
action\_result\.data\.\*\.finish\_time | string | 
action\_result\.data\.\*\.host\.\_id | string | 
action\_result\.data\.\*\.host\.url | string | 
action\_result\.data\.\*\.indicator | string | 
action\_result\.data\.\*\.md5 | string | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.req\_filename | string |  `file name` 
action\_result\.data\.\*\.req\_path | string |  `file path` 
action\_result\.data\.\*\.req\_use\_api | boolean | 
action\_result\.data\.\*\.request\_actor\.\_id | numeric | 
action\_result\.data\.\*\.request\_actor\.username | string |  `user name` 
action\_result\.data\.\*\.request\_time | string | 
action\_result\.data\.\*\.route | string | 
action\_result\.data\.\*\.state | string | 
action\_result\.data\.\*\.url | string | 
action\_result\.data\.\*\.zip\_passphrase | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get file'
Pull the acquired file into Phantom Vault

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acquisition\_id** |  required  | HX Acquisition ID for the acquired file | string |  `fireeyehx acquisition id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.acquisition\_id | string |  `fireeyehx acquisition id` 
action\_result\.data\.\*\.container | numeric | 
action\_result\.data\.\*\.hash | string |  `hash` 
action\_result\.data\.\*\.id | numeric | 
action\_result\.data\.\*\.message | string | 
action\_result\.data\.\*\.size | numeric | 
action\_result\.data\.\*\.succeeded | boolean | 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get alert'
Pull single alert info by ID

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**alert\_id** |  required  | The ID of the alert to fetch data from | string |  `fireeyehx alert id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.alert\_id | string |  `fireeyehx alert id` 
action\_result\.data\.\*\.condition | string | 
action\_result\.data\.\*\.condition\.\_id | string | 
action\_result\.data\.\*\.condition\.url | string |  `url` 
action\_result\.data\.\*\.event\_id | string | 
action\_result\.data\.\*\.event\_type | string | 
action\_result\.data\.\*\.event\_values | string | 
action\_result\.data\.\*\.indicator | string | 
action\_result\.data\.\*\.indicator\.\_id | string | 
action\_result\.data\.\*\.indicator\.url | string |  `url` 
action\_result\.data\.\*\.md5values | string | 
action\_result\.data\.\*\.source | string | 
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.summary | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 