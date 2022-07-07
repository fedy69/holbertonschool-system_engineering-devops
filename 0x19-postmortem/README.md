# 0x19-postmortem

# Issue Summary

06/07/2022 From 11 AM to 12:20 AM  when we requested for the homepage to our servers became unresponsive

# Timeline
- 11:10 AM : Our load balancer CPU usage I/O Wait time increases dramatically.
- 11:15 AM : All request processing has stopped, and I/O Wait is consuming 100% of our load balancer's CPU
- 11:15 AM : Notifyed both the front end and backend teams
- 11:20 AM : Our monitoring alerts us that there is a major problem. At this point, our engineering team begins to diagnose the problem
- 11:24 AM : We've determined that this doesn't appear to be a DoS attack, and that the load balancer server is no longer operable; a hardware failure of the boot disk is thought to be the cause of the problem. We start bringing a new load balancer online
- 11:27 AM : A new load balancer is ready to serve requests.
- 11:30 AM : The DNS A record for onesignal.com is updated for the new load balancer
- 11:50 AM :  DNS has propagated within CloudFlare, and the new load balancer begins serving requests. We realize that the DNS records for a legacy domain (used by some older SDKs in the wild) still needs to be updated.
- 11:55 AM : DNS for the legacy domain is updated.
- 12:20 AM : Service is fully restored.

# Root cause and resolution

The next issue in this timeline was the 8 minutes spent attempting to resolve the problem with the existing load balancer. Within a minute of starting this investigation, the server appeared to simply be unresponsive and we attempted a hard reboot. A minute later there was no sign the server was coming back. At this point, we should have cut our losses and moved onto provisioning a replacement. This could have saved a further 6 minutes..

# Corrective and preventative measures
We would be remiss if we didn't take this opportunity to consider other possible failure modes which would result in such significant downtimes.
We will be auditing the rest of our system to identify such possibilities, and we will implement any mitigations necessary