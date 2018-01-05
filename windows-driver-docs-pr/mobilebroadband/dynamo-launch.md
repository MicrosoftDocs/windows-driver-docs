---
title: DYNAMO launch
description: This topic describes the launch step for the DYNAMO program.
ms.assetid: 85671090-C577-4EE7-9113-974E56FF65EB
keywords:
- Windows DYNAMO launch, DYNAMO launch mobile operators
ms.author: windowsdriverdev
ms.date: 01/04/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DYNAMO launch

This section describes the work needed to successfully launch DYNAMO with your mobile operator, including Web service API monitoring, running an end-to-end scenario, and the review escalation process.

## Before launch
You (the mobile operator) and Microsoft will review that all outstanding issues are properly addressed before moving to go live. This is important to fully migrate to a production environment. If you decide to use a staging endpoint during integration, this migration will take up to a week.

## Web Service API monitoring
The DYNAMO service will monitor the availability of the Web service API by using *Xping* test to ping the MO Direct portal twice per minute, making sure it is accessible.

If we fail to receive the expected response for more than 30 minutes, we will start the escalation process and engage you for investigation. 

## Run end-to-end validation
Microsoft must configure the eSIM and/or SIM ICCID range in the DYNAMO production environment before starting end-to-end testing and validation. This configuration will take up to a week to be implemented. 

It is up to you to decide if the eSIM/SIM range to be configurated is a test range (a subset of the full production range) or the full production range.

End-to-end validation is your responsibility, although Microsoft will support issues and help to address them accordingly.
The following are recommended minimum scenarios. It is expected that you thoughtfully validate your MO Direct web portal behavior.

### First run experience with eSIM

Initial conditions: The Windows 10 device does not have an eSIM profile but it is connected to the internet.

Steps in scenario:
1. Phone number lookup verification.
2. Launch MO Direct web portal.
3. Complete a transaction in the portal.
4. eSIM profile is installed and activated.
5. Device is connected.

### First run experience with SIM

Initial conditions: The Windows 10 device has a SIM.

1. Launch MO direct web portal.
2. Complete a transaction in portal.
3. Device is connected.

## Escalation process

Microsoft has established a two-way live site escalation process for mobile operators and Microsoft to work together on any customer-facing production incidents. A live site issue is any event that is not part of the standard operation of the either your service or Microsoft’s service, and causes (or might cause) an interruption or a reduction in quality of the DYNAMO experience. Key scenarios in the DYNAMO experience are:

- Ensuring that the Mobile Plans app can reach your MO Direct portal via Walled Garden or a Wi-Fi or Ethernet connection.
- Ensuring users can always consume purchased data.

The goal of this process is that both mobile operators and Microsoft agree to the following:

1. Monitor and escalate live site incidents following the process set forth within this topic.
2. Prior to escalation of an incident, assign the correct priority using the guidelines set forth within this topic.
3. Provide responses on all incidents in accordance with the maximum allowed response times associated to the incident priority as set forth within this topic.

### Live site performance SLAs

The following table provides detailed descriptions for live site performance SLAs, including service availability and expected API response times for key APIs integrated with the DYNAMO service.

| Service name | Description | Impact in case of incident | Included in DYNAMO MO API monitoring? | Availability | Latency |
| --- | --- | --- | --- | --- | --- |
| Core Network Services <p>(PGW, Online Charging System, internet access, GRX access, etc.)</p> | Services that provide the capability to: <ul><li>Access the internet for a user with data allowance.</li><li>Access walled garden even with no data allowance.</li></ul> | Users will not be able to connect to the internet using their cellular data plan.</li></ul> | No. <p>Mobile operators are responsible for monitoring their own Core Network Services.</p> | 99.90% | N/A |
| MO Direct portal | A web portal that users can access for the MO Direct scenario. | Users will not be able to engage with the MO Direct experience to sign up data plans. | Yes | 99.90% | 400ms |
| xDR <p>(CDR, SDR, TDR)</p> | <ul><li>CDR: Call details record</li><li>SDR: Subscription details record</li><li>TDR: Transaction details record	</li></ul> | Impacts Microsoft internal business intelligence reporting and sharing insights with mobile operators | No. <p>Mobile operators are responsible for monitoring their own xDR services.</p> | N/A | N/A |

### Incident escalation

#### Escalation to mobile operators

If a service interruption is detected by Microsoft, the incident will be triaged and processed based on the following severity table. For high severity incidents, Microsoft’s One Store Operations Center (OSOC) will contact mobile operators. For low severity incidents, Microsoft’s DYNAMO team will contact mobile operators.

| Severity | Definition | Communication SLAs |
| --- | --- | --- |
| **High** user or business impact.	| Loss of core business scenario(s): <ul><li>Service complete loss for more than 30 minutes (for example, if the API monitoring test fails for more than 30 minutes).</li></ul> | Escalation via phone by the Microsoft OSOC. <ul><li>Initial response from mobile operators is expected within 1 hour.</li><li>Ongoing updates are expected every business day until resolution.</li></ul> |
| **Low** user or business impact. | Impact on non-critical business scenario(s): <ul><li>Reporting failures.</li><li>Information requests.</li></ul> | Escalation via email by the DYNAMO team. <ul><li>Initial response from mobile operators is expected within 1 business day.</li><li>Ongoing updates are expected every week until resolution.</li></ul> |

#### Escalation to Microsoft

If you detect a service interruption, you can escalate through the Microsoft Operations Center and identify as a partner to the DYNAMO Services team and that you would like to report a problem. Service interruptions include, but are not limited to, core DYNAMO scenarios being down for more than 30 minutes, or mobile operators’ services receiving an abnormally high number of calls from DYNAMO services. You will be asked to provide details around the incident in a form of a template that will be supplied by the Operation Center to ensure we can engage the correct teams.

- For high severity incidents, escalation to Microsoft will occur via a call to the Microsoft Operations Center at **+1 425-538-9336** and an email to [osoc@microsoft.com](mailto:osoc@microsoft.com).
- For low severity incidents, escalation to Microsoft will occur via an email to [dmcellpd@microsoft.com](mailto:dmcellpd@microsoft.com).

### Services outage

#### Microsoft communication of services outage to mobile operators
Microsoft will inform mobile operators of any Microsoft network, DYNAMO or Microsoft Store service outages via telephone and email no more than 30 minutes after we first become aware of such an outage.

#### Mobile operator communication of services outage to Microsoft
You must inform Microsoft of any Core Network Services outages via telephone and email no more than 30 minutes after you first become aware of such outages. All such communications should be directed by phone to Microsoft Operations center at **+1 425-538-9336** and an email to [osoc@microsoft.com](mailto:osoc@microsoft.com).

#### Planned maintenance
Regularly scheduled or routine maintenance of the services operated by mobile operators or the Microsoft DYNAMO team that have or may have end user impact must be communicated beforehand through the channels defined in this section.  

#### Communication of planned maintenance to mobile operators
The Microsoft DYNAMO team will communicate planned maintenance to mobile operators no later than five business days prior to the event. Once the maintenance is completed, a notification will be sent to mobile operators.

#### Communication of planned maintenance to Microsoft
Regularly scheduled or routine maintenance of the mobile operator’s Core Network Services must be communicated via email to [osoc@microsoft.com](mailto:osoc@microsoft.com) no later than five business days prior to the event. Once the maintenance is completed a notification will be sent to [osoc@microsoft.com](mailto:osoc@microsoft.com).

#### Requesting bug fixes
**Reporting a bug** – Each team can report a bug via email to [DYNAMOpartnersup@microsoft.com](mailto:swifipartnersup@microsoft.com), and work with their counterparts to get a bug logged.

**Getting the bug fixed** – The DYNAMO team must triage the bug and provide business justification/impact.

**Deploying the fix for the bug** – Once the bug has been approved to be fixed, a tentative deployment schedule will be shared and network providers will be notified via email once the fix is deployed.

## Customer Support

Mobile operators are solely responsible for any customer support issues. 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Mobile%20operator%20scenarios%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")