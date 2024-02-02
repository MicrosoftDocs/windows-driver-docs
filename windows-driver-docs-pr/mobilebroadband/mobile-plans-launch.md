---
title: Mobile Plans Launch
description: This topic describes the launch step for the Mobile Plans program.
keywords:
- Windows Mobile Plans launch, Mobile Plans launch mobile operators
ms.date: 03/25/2019
ms.topic: article
---

# Mobile Plans launch

This section describes the work needed to successfully launch Mobile Plans with your mobile operator, including Web service API monitoring, running an end-to-end scenario, and the review escalation process.

## Before launch

You (the mobile operator) and Microsoft will review that all outstanding issues are properly addressed before moving to go live. This is important to fully migrate to a production environment.

## Launch validation

On the agreed-upon launch date, Microsoft will move the mobile operator portal to production. The mobile operator is responsible for performing end-to-end validation immediately and reporting back any potential issues to Microsoft. This will enable providing support to address the issues accordingly.

Mobile operatosr are ultimately responsible for accepting the live, in-production service.

## After Launch

### API monitoring

The Mobile Plans service monitors the availability of the Web service API (mobile operator portal) by using *Xping* to ping the portal twice per minute, making sure it is accessible.

The Mobile Plans service monitors the availability of the `GetBalance` API using the defined protocol, twice per minute, making sure it is accessible. For this monitoring the mobile operator should provide an ICCID that will be continually used.

### Escalation process

Microsoft has established a two-way live site escalation process for mobile operators and Microsoft to work together on any customer-facing production incidents. A live site issue is any event that is not part of the standard operation of the either your service or Microsoft’s service, and causes (or might cause) an interruption or a reduction in quality of the Mobile Plans experience. Key scenarios in the Mobile Plans experience are:

- Ensuring that the Mobile Plans app can reach your MO Direct portal via Walled Garden or a Wi-Fi or Ethernet connection.
- Ensuring users can always consume purchased data.

The goal of this process is that both mobile operators and Microsoft agree to the following:

1. Monitor and escalate live site incidents following the process described in this topic.
2. Prior to escalation of an incident, assign the correct priority using the guidelines described in this topic.
3. Provide responses on all incidents in accordance with the maximum allowed response times associated to the incident priority as described in this topic.

#### Live site performance SLAs

The following table provides detailed descriptions for live site performance SLAs, including service availability and expected API response times for key APIs integrated with the Mobile Plans service.

| Service name | Description | Impact in case of incident | Included in Mobile Plans MO API monitoring? | Availability | Latency |
| --- | --- | --- | --- | --- | --- |
| Core Network Services <p>(PGW, Online Charging System, internet access, GRX access, etc.)</p> | Services that provide the capability to: <ul><li>Access the internet for a user with data allowance.</li><li>Access Walled Garden even with no data allowance.</li></ul> | Users will not be able to connect to the internet using their cellular data plan.</li></ul> | No. <p>Mobile operators are responsible for monitoring their own Core Network Services.</p> | 99.90% | N/A |
| MO Direct portal | A web portal that users can access for the MO Direct scenario. | Users will not be able to engage with the MO Direct experience to sign up data plans. | Yes | 99.90% | 400ms |
| xDR <p>(CDR, SDR, TDR)</p> | <ul><li>CDR: Call details record</li><li>SDR: Subscription details record</li><li>TDR: Transaction details record</li></ul> | Impacts Microsoft internal business intelligence reporting and sharing insights with mobile operators | No. <p>Mobile operators are responsible for monitoring their own xDR services.</p> | N/A | N/A |

### Incident escalation

#### Escalation to mobile operators

If a service interruption is detected by Microsoft, the incident is triaged and processed based on the following severity.

| Severity | Business Impact | Threshold | Expected Resolution Time | Update Cadence |
| --- | --- | --- | --- | --- |
| **1** | **Outage/Disaster:** Issue with high impact, affecting all traffic to a single partner, or a moderate or greater amount of overall global traffic. | Partner Failure Percentage = 100% OR Global Failure Percentage > 5% | 8 hours | Once partner contact is made, email updates should be provided every 2 hours |
| **2** | **Service Disruption:** Issue with medium impact, affecting a high amount of user traffic for a single partner, but still a low amount of overall global traffic. | Partner Failure Percentage = 75% OR Global Failure Percentage = 1% to 5% | 24 hours | Once partner contact is made, email updates should be provided every 6 hours |
| **3** | **Standard Escalation:** Issue with low-to-medium impact, affecting moderate amount of user traffic for a single partner, but a very low amount of overall global traffic. | Partner Failure Percentage = 25% - 75% OR Global Failure Percentage < 1% OR 12 consecutive xPing tests to MO’s Get Balance endpoints fail (MPS makes one xPing call per 5 minutes) | Best effort | Once partner contact is made, emails updates should be provided as needed |

#### Escalation to Microsoft

If you detect a service interruption, you can escalate to the Mobile Plans Services team. Service interruptions include, but are not limited to, core Mobile Plans scenarios being down for more than 30 minutes, or mobile operators’ services receiving an abnormally high number of calls from Mobile Plans services.

For incidents during staging / onboarding, escalate to [Mobile Plans Implementation Support](mailto:mpimplementation@microsoft.com). For incidents post onboarding, escalate to [Mobile Plans Operations support](mailto:DYNAMOPARTNERSUP@microsoft.com).

### Services outage

#### Microsoft communication of services outage to mobile operators

Microsoft will inform mobile operators of any Microsoft network Mobile Plans service outages via email no more than 30 minutes after we first become aware of such an outage.

#### Mobile operator communication of services outage to Microsoft

You must inform Microsoft of any Core Network Services outages via email no more than 30 minutes after you first become aware of such outages. [Mobile Plans Operations support](mailto:DYNAMOPARTNERSUP@microsoft.com)

##### Planned maintenance

Regularly scheduled or routine maintenance of the services operated by mobile operators or the Microsoft Mobile Plans team that have or may have end user impact must be communicated beforehand through the channels defined in this section.  

##### Communication of planned maintenance to mobile operators

The Microsoft Mobile Plans team will communicate planned maintenance to mobile operators no later than five business days prior to the event. Once the maintenance is completed, a notification is sent to mobile operators.

##### Communication of planned maintenance to Microsoft

Regularly scheduled or routine maintenance of the mobile operator’s Core Network Services must be communicated via email to Microsoft no later than five business days prior to the event to [Mobile Plans Operations support](mailto:DYNAMOPARTNERSUP@microsoft.com).

##### Requesting bug fixes

**Reporting a bug** – Each team can report a bug via email to [Mobile Plans Operations support](mailto:DYNAMOPARTNERSUP@microsoft.com), and work with their counterparts to get a bug logged.

### Customer Support

Mobile operators are solely responsible for any customer support issues.
