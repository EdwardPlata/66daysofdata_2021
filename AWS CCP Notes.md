---
favorited: true
tags: [Notebooks]
title: AWS CCP Notes
created: '2020-10-13T00:38:14.111Z'
modified: '2021-02-24T02:11:36.752Z'
---

# AWS CCP Notes

### Billing and Pricing
#### Marketplace subscriotion

* There are several vendors, pricing plans and methods
* Most popular will be in Popular Category on hime page
* Followallong shows machine learning categories

--
- [ ] 
- AWS market place has plenty of services that can be puchase like deep learning modified EC2 instances.
### AWS Trusted Advisor
- Advises you on secrutiy, saving money, performance, service limits and fault tolerance

* you'll get free trusted advisor checks

##### 5 categoies
1. Cost optimization (Idle load balancers, unassociated Elastic IP addresses (EIP))
2. Performance(High ultilization EC2 instances)
3. Security (Including IAM access key rotation, MFA - on root account) 
4. Fault Tolerance (Amazon RDS Backups )
5. Service Limits. (VPC)

#### AWS trust advisor
* How does trusted advisor make recomendations to you?

#### Consolidated BIlling
* Turned off by default when you have multiple member accounts
* Cost explorer is very good in getting an overview
* Reports: AWS gives you a bunch by default.
* Completely able to filter and keep certain reports for later.

#### AWS Budgets
# Each cost 2c per day. 
# Cost usage and reservation: USage unit or EC2 running horus. We can track budget on monthly quarterly or yearly levels.
# If it's per year it may alert you at the end of the year.
# Alerts support EC2, RDS, Redshift, ElastiCache.
# API is included for progmantic notafication
# Can also be sent via chatbot: Integration with messaging apps is doable due to API


#### TCO Calculator: Total cost of ownership
* how much can we save
* Good for executive reporting
* Reduces the need to check large capital expenditure.
* Pursuasion tool to use at the executive level
* you can get a 3 year summary of cost 

#### Physical survers / pro machines. 
* Web application 

#### AWS landing Zone
* Help enterprises quickly set up a secure, AWS Multi-account -- Very expensive upfront cost
* Provides a baseline environment ot get started with a multi-account architecture
* AWS account vending Machine (AVM)
* Automatically provisions and ocnfiugre newa accounts via service catalog templates
* Landing zone is givin gyou a baseline environment that will be secured with best practices

##### Resource groups and tagging
* Tags are wrods or phrases that act as metadata for organizeing you AWS resources
* Resource groups are a collection of resources that share one or more tags

* Help syou organize and consolidate information based on your project and the resources that you use.
* Resource groups can display details about a group of resource based on metriucs alamrs and configuration settings
#### AWS Quick Start
* Prebuilt templates by AWS and AWS partnership to help you deploy populat stacks on aWS reducing hundreds of manual procedures into just a few steps
1. A reference arhcitecture for the deployment 
2. AWS cloud formation templates that automate and ocnfigure the deployment
3. A deployment guide explaining the architecture

#### AWS cost and usage report
1. We have a big button with a spread sheet showing a detailed break down
- places the report into s3
- use athena to turn the reprot into queries

#### AWS Cost and usage rpeort
- cost and usage can be integrated with othe raWS services

#### Organization and accounts
1. Organizeation allow you to centrally manage billing, constrol access, compliance , security, and share resources across your AWS accoutns.
2. Root account user is a single sign-in identity

* You want to naem accounts by their function
* Organization is good for policy  management 
* Policy will be applied immediatly.
* we can suspend accounts.

* It'll show as suspended

#### AWS Networking
1. REgion: Geographical
2. AZL Data ceneter 
3. VPC: Logically isolated section of the aws cloud wher eyou can launch aws resources
4. Internet Gateway: Enable access tothe internet
5. Route Tabel: Determine where network traffic from your subnets are directed
6. NACLs: Acts as a firewall at the subnet level
7. Security Groups: Acts as a firewall at the instance level.
8. SubnetsL a logical partition of an IP network into multiple, smaller network segments.

#### Database Services
1. Dynamo DB - NoSQL key/value database ( Cassandra like)
2. DocumentDB - NoSQL document database that is mongodb compatible
3. RDS - relation database service that supports multiple engines
  - Eninges: MySql, postges, Maria DB, oracle, MSSQL Aurora
  - Aurora - MySql (5x faster) and PSQL (3x faster) DB fully managed
  - Auroa Serverless - only runs when you need it, like AWS Lambda ( Best for developmnet or serverless architecture)
4. Neptune: Managed Graph Database
5. Redshift - columnar database petabyte warehouse 
6. ElastiCache- Redis or Memcached database.


#### Provisioning Services
- What is provisioning? An easy way tos et up a bucnh of resources / servers in an automated way via code or GUI

Services:
1. Elastic Beanstalk: Deploying webapps without thinking of underlying infrastructure -- With containeres and language of choice. --> Heroku for AWS
2. Opsworks - Configuration management service that provides managed instances of Chef or poppet 
* 2 different tools to progmatically set up a server
* Chef uses Ruby and set up is call Recepie
* If you have to pull dependencies or pull the code you can do so .
3. CloudFormation - infrastructure as code, JSON or YAML
- Define all AWS resources that you want to provision and exactly how to configure. So you submit a template all in 1 go.
- Compared to OpsWorks - It has some limiteations but cloud formation can do anything. Most complex but most flexible
4. AWS quickstart- pre-made packages liek lightsailm to launch and configure AWS compute, network,sstorage, etc.
- IF you want to get started with ML there are already provisions availbale.
5. AWS market place - Digital catalouge of thousands of software listings from indipendant software vendors.

Computing services
1. EC2- Elastic compute cloud, everything runs on EC2 instances.
2. ECS- Elastic container service Docker as a service , highly scalable, high -performance container, orchestration service that supports docker containers, pay for EC2 instances.Defined with something called a task or service
3.  Fargate -- like ECS but better. Microservices where you don't think about infrastrucure. Pay per task
- You aren't paying for EC2 just the run time. (Like lambda)
4. EKS - Kuberneties as a service. easy to deploy, manage and scale containerized applications using Kubernetes. Just for microservices
5. Lambda- serverless functions - code runs without provisioning or managing service. You just pay for the compute time depending on how long it runs.
6. Elastic Beanstalk orchestrates various AWS services, including EC2, S3, SNS, Cloud watch, autoscaling, and ELB
- Good for setting up developer environments.
- Upload code and it'll take care of the rest.
- Just using EC2 instances just without htinking about it
7. AWS batch - plans, schedules, and executes your batch computing workloads across the full range of AWS compute services and features, such as AWS EC2 and spot instances 
- USes spot pricing

#### Storage services
1. S3 - simple storage service - Object storage
- think as a harddrive in the cloud with unlimited space
2. S3 Glacier - low cost storagefor achiving and long-term backup 7-10 years. Cost for retrival 
- good for retrival 
3. Storage Gateway- A  hybrid cloud storage with local caching
- An extension of onprem storage on cloud
- A good backup
4. EBS - a virtual harddrive in the cloud that we can attach to EC2 instances (Singular)
- Solution SSD, IOPS SSH, throughput HDD, cold HDD
5. EFS-  Elastic file storage - file storage mountable to multiple EC2 instances at the same time (Multi solution)
6. Snowball - Physically migrated lots of data via computer suitcases 50-80tb -- Basically a computer in a suitcase with a lot of hard drives in it. 
- Quickly upload that data onto AWS and upload to AWS 
7. Snowball EDGE - a better version of snowball -100 TB and capability of processing data as it's being inserted 
8. Snowmobile - Move petabytes of data via cargo on a semi trailer truck. 
- AWS will trive it towards you and you can a move all your data on to there.

#### Business Centric Services
1. Amazon Connect - CAll Center - Cloud based call center service you can set up in a few clicks-  based on the same proven system used by amazon customer service teams
- Able to make inbout calls and dial outbound.
- store in S3 as logs and run through analysis via AWS comprehend
- If you want to route calls you can do that too
2. Workspaces - Virtual REmote Desktops - Sercure manged service for provisioning either Windows or Linus desktops in just a few minutes which quickly scales up to 1000s of desktops
3. WorkDocs - A content creation and collaboration service - easily create, edit and share content saved certrally in AWS (AWS sharepoint basically)
4. Chime - AWS platform for online meetings, video conferencing, and business calls whcih elastically scales to mee tyour capacity needs 
- Basically like slack or zoom for amazon
5. WorkMail - (GmAil for AWS) - MAnaged business email, contacts, and calender service with support for existing desktops and mobile email client applications. (IAMP)
6. Pinpoint- marketing campaign management system you can use for sending targeted email, sms, push notaficationsm and voice mail
- AB testing on emails 
7. SES - simple eamil service - A cloud based email sending service designed for marketers and application developers to send marketing notafications and emails
- Like pinpoint but we want to send emails via the application. As Pinpoint is more personal emailing service.
- Has HTML componenet
8. Quick Sigt - A business intelligence (BI service). Connect multiple datasource and quickly visualize data in form of graphs with little to no programing knowledge
- many services in it. and can share visualizations via dashboard.

#### Enterprise Integration
* Going Hybrid
1. Direct Connect- dedicated Gigabit network connecting from prem to aWS (imaging having a fiberoptic connection)
2. VPN - 
- site 2 site VPN - connection your on-prem to aws networks
client vpn - connecting a client ( a laptop) to your aws network
3. Storage Gateway - a hybrid storage service that enables your on-prem applications to use AWS cloud storage. You can use this for backup and archiving, disaster recover,cloud data processing, storage tiering , and migration.
4. Active Diractory - The AWS Diractory Service for Microsoft Active Directory also known as AWS managed microsoft AD - enables your directory-aware workloads and aws resources to manage active directory in the aws cloud.
 - AWS workloads can use this in AWS cloud.
 - Active directory has many integration

 #### Logging Services
 1. CloudTrail - logs all API calls (SDK or CLI) between AWS Services (Who can we blame)
- who created bucket
- who spun expesnive EC2
- who launched sagemaker
* Detect developer misconfiguration
* Detect malicious actors
* Automate responses 
- We can celate triggers
2. CloudWatch - collection fo multiple services
- CloudWatch Logs - Performance data on aWs service eg. CPU utilization, Memory, Network in application logs eg Rails NGinx
Lambda logs - Applicaiton calls for lmabdas
* CloudWatch Metrics  - Represent a time-ordered set of data points, A variable to monitor 
* CloudWatch Events -Trigger an event based on condition eg. Ever hour take snapshots of server
* Cloudwatch Alarms -Tiggers ntoafications based on metrics
* cloudwatch dashboard -create visualization absed on metrics.

# KNow your initalisms 
* Understand all initials.
1. IAM - Identity and ACcess management
2. S3 - Simple storage scaling
3. SWF Simple Workflow service
4. SNS - Simple notafication service
5. SQS simple queue service
6. SES - Simple Email SErvice
7. SSM - Simple system manager
8. RDS Relational database service
9. VPC - virtual private cloud
10. VPN - Virtual private network
11. CFN - cloud formation
12. WAF - Web Application Firewall
13. MQ Amazon Active MQ
14. ASG Auto Scaling group
15. TAM - Technical Account manager
16. ELB - Elastic load balancer
17. ALB Application Load balancer
18. NLB Network Load Balancer
19. EC2 Elastic Cloud computer
20. ECS - Elastic Container SErvice
21. ECR - Elastic container REpo
22. EBS - Elastic Block Storage
23. EFS - Elastic File storage
24. EMR - Elastic Map Reduce
25. EB - Elastic Beanstalk
26. ES - Elastic Search
27. EKS - Elastic Kubernetes SErvice
28. MKS managed Kafka Service
29. IoT - Internet of thinks
30. RI  - Reserved Instance 

#### Shared responsability model
1. Security In cloud - customer responsability 
- Data configuration -- you are responsible for it if you don't secure it.
- if you don't turn on monitoring services 
- Many things you can use, you must configure
* Customer data
* Platform, applciations, IAM
* OS, Network and firewall config
2. Security of cloud
- Hardware 
- Operation of managed services
- Global infrastructure

#### AWS Compliance PRograms
1.  these are set of internal policies and procedures of a company to comply with laws, rules, and regulations or to uphold business reputation.
- HIPAA - health insurance potability and accountability- Secure health data (Hospital or insurances)
- PCI DSS - Credit card transaction regulation.

#### AWS Artifact
How do we prove AWS meets a Compliance?
- No $$ self service portal for on-demand access to aWS compliance reprots
- on demand Access to AWS sercurit and compliance reprots and seleect online agreements
- These checks are based on global complianbce frameworks.

#### Amazon inspector
- How do we prove an EC2 is Hardened?
- Hardenned - act of eliminating as many security risks as possible
AWS inspector runs a security benchmark against a specific EC2 isntance.
- You can run a variety of security benchmarks.

- Can perform both network and host assessments
1. Install AWS agent on EC2 instance
2. Runa ssesment for your assessment target
3. Review your fundings and remediate security issues
- 699 checks!!

#### AWS Waf
- Web application firewall - protect your web app from common web exploits, write your own rules to Allow or Deny traffic based on the contents of an HTTP request.
- use a ruleset from a trusted aws security partner in the AWS waf rules market place

* WAF has to be attached to cloudfront or ALB

#### AWS Shield
 - Manged DDOS protection service that safeguards applications.
 * When you route your traffic through Route53 or CloundFront you are using AWS shielf standard
 - Protects you against Layer 3,4,and 7 attacks
 * 7 application
 * 4 trasnport
 * 3 network

 - Shield Standard is free - DDos protection for many services 
 - SHielf advance - 3k / yr protection and consulting from security experts.
 - Route 53, cloud front ELB global accelerator elastic IP 
- protects even against cost

#### Penetration testing (PenTesting)
- An authorized simulated cyber attack on a computer system to evaluate the securirty of the system
- You can do this on aWS
1. EC2 , NAt gateways, ELB
2. RDS,
3. cloudFront
4. Aurora
5. API Gateway
6. Lambda and lambda edge functions
7. Lightsaild resources
8. Elastic Beanstalk envrionmnets

#### GuardDuty
1. Wjat is IDS/ IPS?
- Intrustion detection system and intrusion protection system
- A device or software application that monitors a network or system for malicous activity or policy violations
* How do we detect if someone is attempting to gain access to our AWS account or resources 
* Logs all access

#### Key managment service (KMS)
- managed service that makes it easy for you to create and control the encryption keys used to encrypt your data
* KMS is a multi-tenant HSM (Hardware security module)
* MAny AWS Services are integrated to USE KMS encrypt your data with a simple check box
* KMS uses envelope encryption

- Envelope Encryption - when you encrypt your data, your data is protected.
- Encryting hte key - so people cant see this,

#### AWS macie
- Fully managed service that continuously monitors S3 data access activity for anomolies, generated detailed alters whne it detects risk of unauthorized access or inadverted data leaks.
- S3 protection basically

Macie has a variety of alerts
* Ransomware
* Privilage escalation
* Identtity enumeration
* Information loss - stored credentials

Can identify most at risk users
Securty gorups vs NACLs (Networks access control lists)
* Acts as a firewall at the instance level
* Implicitly denies all traffic, You create allow rules.

* eg. Allow an EC2 instance acecss on port 22 for SSH
2. NACLS
* Acts as a firewall at the subnet level
* You can create allow and deny rules
* Eg. Block a specific IP address known for abuse

* You cant unblock all IP addresses

#### AWS VPN
* LEt's you establish a secure and private tunnel from your network or device to the AWS global network
1. AWS Site to side VPN
- securitly connect on-prem network or branch office site to VPC
2. AWS Client VPN
- Securely connect users to aWS or on-prem networks.

#### Cloud service

1. CloundFront - Infrastryctyre as code, setup service via template scripts, YML, Json - provisioning many resources
2. CloudTRail - Logging all API calls for all AWS services (Who you can blame)
3. CLound Front - Content distrbution network, create a cache copy of your website and ocpies to servers nlocated near people trying to donwload 
4. Cloud watch - collection of multiple services
 - cloud watch logs - any custom log data, memory usage, rails logs, nginx logs
 - cloud watch metrics - metrics that are based off of logs. Eg memory usage
 - cloud watch events - trigger an event based on a condition eg. every hour take a snapshot of server
 - cloud watch alarms - Trigger notafications based on metrics
 - cloud watch dashboard - create visualizations based on metrics
5. Cloud Search- searh engine, you have an ecommerce website and you want to add a search bar

#### Connect SErvices - services with connect in the name
1. Direct connect - Dedicated fiberoptic connection from data center to AWS
- If your campany needs insalty fast connection, we have this service
2. Amazon Connect-  Call center in the cloud -
- toll free num, accept inbound and outbound calls
3. Media connect - New Version of elastic transcodre, converst videos to different video types
- eg. You have 1k of videos you and you need to transcode them into different video formats, maybe you need to apply watermarks, or insert introduction video in fornt of every video.

#### Elastic transcoder vs media convert
- Elastic trans - the old way
* AWS Elemental media convert - new way 
- Transcodes videos to streaming formats
- overlays images
- insert videos clips
- extracts captions data
- robust UI

#### SNS vs SQS
- both used for messaging and application integration
- SNS - simple notafication service
* PAsses along messages
- used for sendin gPLAIN TEXT EMAILS which is triggered via other AWS services. THe best example of this is billing alarms.
- Can retry sending in case of failure of HTTPS
- Really good for webhooks, simple internal emails, triggering lambda functions
- SQS - queues up services
- Guarantee of delivery
- Placed messages into a queue .apps pull queue using AWS SDK
1. Can retain messages for up to 14 days
- can send them in squentioal order or in parallel


#### Inspector vs trusted advisor
- Both have security services
1. Amazon inspector
- Audit EC2 isntances that you've selected
- Generates a report from a long list of security checks i.e 699 checks

2. Trusted advisor
- Doesn't gen a pdf report
- Gives a holistic view of recommendations across multiple services and best practices
- eg. you ahve open ports on these security groups
- You should enable MFA on your root acocunt when using trusted advisor.


#### ALB vs NLB vs CLB
- CLB - calssic load balancers-  inteded for apps that were built within the EC2 classic network - doesn't use target groups. Layer 4 and layer 7. HTTP traffic.

- ALB - Layer 7 req HTTP(S) traffic
- - Routing rules, more usabiltiy from 1 load balancer
- Can attach WAF (Whcih is appliucation specific)

- Network
- Layer 4 IP Protocal data
* TCP and TLS traffic where extreme performance is requried (This videogame streaming)
capable of handling millions of request per second while maintianing ultra-low latencies
* Optimize for sudden and volatile traffic patterns while using a single statis IP address per Availability Zone

* * Can attach Amazon certification manager (ACM) SSL certificate

#### SNS vs SES 
- both send emails
- SNS - Sends notafications to subscribers of topics via multiple protocol. Eg HTTP, Email, SQS, SMS
- SNS is generally used for seding Plain textx
- Just made for information 
- most exam questions are 

- SES- ex. SendGRid- HTML emails - very professional
- Can monito email reputation
 - can recieve emails as well


 #### AWS artifact vs AWS Inspector - Both compile PDFs
 1. AWS Artifacts
 - Why should an enterprice trust AWS>
 * Generates a security report that's based on global compliance frameworks such as SOC or PCI (Service organization control or Payment credit intdustry)
 2. AWS inspector
 - How do ywe know if this EC2 isntance is secure? Prove it>
 - runs a scriot that analyzes your EC2 isntaces, then generates A pdf report tellign you which security checks passed.
 - Audit tool for security of EC2 instances.

 -- Next is practice exam
