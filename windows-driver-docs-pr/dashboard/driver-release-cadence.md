---
title: Driver Release Cadence
description: Policy around when drivers are released
ms.topic: article
ms.date: 11/17/2020
ms.localizationpriority: medium
---

# Driver Shiproom Release Cadence Windows 2021 
Last Updated: November 18, 2020

Windows as a Service has a well-established OS update release cadence.
    **Latest Cumulative Update (LCU)**: Monthly Quality and Security updates released during the second week.  This is also known as the “B” release and is offered to all eligible Windows 10 devices through Windows Update (WU) scans.
    **Feature Updates**: Provide the latest feature experiences and quality fixes.

We have a shared goal of keeping devices up to date while providing users a high-quality experience.  Recently when a driver update is released alongside OS updates, it has resulted in a poor experience and significantly impacted end-users. Occasionally, we have had other driver release incidents which occur outside of normal business hours (Redmond time) which impact our ability to intervene and prevent additional devices from receiving “poor” drivers. Additionally, we have received many requests to have a predictable driver release cadence from many partners.

To ensure we release quality drivers, reduce the risk of releasing drivers at the same time as OS changes and provide ecosystem partners a predictable driver release cadence; we are making the following changes for releasing drivers marked as needing “Microsoft Approval”. Today, this includes:
* Flighted drivers:  Drivers (Shipping Label) marked as **Automatic** = Critical Update (CU) or Dynamic Update (DU) or both 
* Optional driver classes which always go through Shiproom approval

**Predictable driver release windows**: During OS update release timeframes, we will defer releasing drivers needing “Microsoft Approval” to WU and will resume automatic publishing after the deferral window.

1. **Monthly Quality Update “B” release**: Driver needing “Microsoft Approval” will not be released one day before and for one day after monthly security “B” release. 

|Monday|2nd Tuesday of each month|Wednesday| 
|----|----|----|
|1 day before|“B” monthly security release day|1 day after|

2. **Feature update offer via Windows Update**: Driver needing “Microsoft Approval” will not be released two days before and for two days after start of feature OS update rollout.

|Before | Day Of | After |
|----|----|----|
|2 days before | Feature OS Rollout | 2 days after |

> A. If there are known issues for feature update and driver compatibility, partners can request feature update offer block mitigation while a compatible driver update is being validated and posted to WU. For more information see: [Feature Update Windows Update (WU) Offer Block Mitigation Request](#featureUpdates)

3. **Weekends**: Driver needing “Microsoft Approval” will not be released from Friday until Sunday 5PM Pacific Time, unless the next day is in a deferral period.

|Friday & Saturday |	Sunday |
|--------|----|
|No release for “Microsoft Approval” drivers | Release after 
5PM Pacific time |

4. **US Microsoft Holidays**: Drivers needing “Microsoft Approval” will not be released on Microsoft US Holidays

|US Microsoft Holidays | 2020 |	2021 |
|----|----|----|
|New Year's Day | Tuesday Jan 01 | Friday Jan 01 |
|Martin Luther King Day | Monday Jan 20 | Monday Jan 18 |
|Presidents Day | Monday Feb 17 | Monday Feb 15 |
|Memorial Day | Monday May 25 | Monday May 31 |
|Fourth of July | Thursday Jul 03 | Monday Jul 5 |
|Labor Day | Monday Sep 07 | Monday Sep 6 |
|Thanksgiving Day | Thursday Nov 26 | Thursday Nov 25 |
|Day after Thanksgiving | Friday Nov 27 |  Friday Nov 26 |
|Christmas Eve | Tuesday Dec 24 | Thursday Dec 23 |
|Christmas Day | Wednesday Dec 25 | Friday December 24 |

5. **US Winter Holiday timeframe release moratorium**: During the US Winter Holiday season, for approximately two weeks driver shiproom will not be releasing ANY drivers, for calendar year 2020 this is December 17, 2020 through January 1, 2021 and for CY2021 this will be December 16, 2021 through January 1, 2022. 

Please see the 2021 driver deferral periods in the Appendix calendars for additional dates. 
 
## Call to Action
We believe that creating a predictable driver release cadence will result in better update user experience across both Windows 10 OS and driver updates. We encourage ecosystem partners to _plan for their driver flighting and publication releases_ in alignment with above cadence and help us improve the experience of our mutual users and customers. 

### Exception Process
We recognize the need for partners to release critical/security driver updates during the limited driver release windows and these will be handled via an exception process. For any drivers needing immediate release, please open a Hardware Dev Center Partner Support Request (ticket) with the keywords **“Driver release deferral exception request”** added to the title. Please also, include the following information in the ticket:
* Shipping Label ID(s)
* Reason for “Urgent Driver release request”
* Impact to end-users if driver release is delayed

For additional information to contact Hardware Dev Center Support, please see the [**How Do I contact Hardware Dev Center Dashboard Support?**](./hardware-dashboard-faq.md).

 
## Appendix
### FAQ:
What does this deferral mean for newly submitted drivers or drivers currently In-Flight?
* This deferral is for the actual “Release” of a driver needing “Microsoft Approval” (marked as Automatic or Dynamic Update) to WU.  Newly submitted drivers and drivers currently In-Flight will proceed as they normally do.  

### 2021 Driver Deferral Calendar:
** This calendar is subject to changes based on OS release timelines.
 
![Image 2021 Driver Release Calendar](images/2021driverReleaseCalendar.png)
### Feature Update Windows Update (WU) Offer Block Mitigation Request
In order to ensure that end users have a good post-update experience, when a driver has a known incompatibility with a feature update. Partners can request a temporary WU offer block (~30 – 60 days) so that Windows Update will not offer the feature update to devices running a driver version with a known incompatibility. The offer block will be removed once a partner has posted an updated driver (as Automatic and/or Dynamic) via Hardware Dev Center portal.

|Mitigation type|Description|Criteria for application|
|-------|-------|--------| 
|Windows Update (WU) offer block|A temporary hold on offering an OS upgrade to a device. These devices are blocked until the fix is released via servicing, at which point the device is then unblocked. This does not impact media installs.|An issue that directly impacts the OS after upgrade, such as a driver crash, BSOD or data loss, security issues, connectivity loss, etc, for which a fix is in progress.|

To request an offer block:
1)	File a new feedback on [MS Collaborate in the EEAP Engagement](https://partner.microsoft.com/dashboard/collaborate/feedback/wits/bugs/create).
2)	Title must begin with **[WU offer block request] [IHV/ISV - Driver Name] [Impacted driver versions]**, i.e. [WU Offer block request] [Contoso – contoso.sys] [1.1 through 1.5]
3)	Provide the following information in the **Repro Steps**

    End user scenario: Description of how end user scenario is impacted, i.e. Garbled video playback after feature os update with graphics driver version X

    Estimated impact (number of in-market devices): 
    Detailed Repro steps:
    Block criteria (e.g., driver name + version, BIOS, HWIDs, etc): 
    Name and path of driver binary:
    Found in OS version:
    Workaround (if any):
    Related OS bug (if any):
    Driver owner: Name of IHV/ISV/partner creating fixed driver version
    Requested lifetime of block – i.e. 30 days
    Access to a device in Redmond, WA (Y/N/NA)
    Repro rate (%)
    Is this a regression caused by an OS change? [Release/Release]
    Business impact (sales volume)



    