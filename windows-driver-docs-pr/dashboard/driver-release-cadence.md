---
title: Driver Release Cadence
description: Policy around when drivers are released
ms.topic: article
ms.date: 12/14/2020
ms.localizationpriority: medium
---

# Driver Shiproom Release Cadence Windows
Last Updated: December 14, 2020

This page provides information on the operation schedule for driver shiproom. In order to provide the best experience for Windows users, there are certain times where aspects of publication operations are suspended.

We have a shared goal of keeping devices up to date while providing users a high-quality experience.  Recently when a driver update is released alongside OS updates, it has resulted in a poor experience and significantly impacted end-users. Occasionally, we have had other driver release incidents which occur outside of normal business hours (Redmond time) which impact our ability to intervene and prevent additional devices from receiving "poor" drivers. Additionally, we have received many requests to have a predictable driver release cadence from many partners.

Windows as a Service has a well-established OS update release cadence.
    **Latest Cumulative Update (LCU)**: Monthly Quality and Security updates released during the second week.  This is also known as the “B” release and is offered to all eligible Windows 10 devices through Windows Update (WU) scans.
    **Feature Updates**: Provide the latest feature experiences and quality fixes.

To ensure we release quality drivers, reduce the risk of releasing drivers at the same time as OS changes and provide ecosystem partners a predictable driver release cadence; we are making the following changes for releasing drivers marked as needing "Microsoft Approval". Today, this includes:
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

> A. If there are known issues for feature update and driver compatibility, partners can request feature update offer block mitigation while a compatible driver update is being validated and posted to WU.

3. **Weekends**: Driver needing “Microsoft Approval” will not be released from Friday until Sunday 5PM Pacific Time, unless the next day is in a deferral period.

|Friday & Saturday |	Sunday |
|--------|----|
|No release for “Microsoft Approval” drivers | Release after 
5PM Pacific time |

4. **Certain US Holidays**: Drivers needing “Microsoft Approval” will not be released on certain US Holidays

|US Holidays | 2020 |	2021 |
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

See the [2021 driver deferral periods](#calendar) calendars for additional dates. 
 
> 📘 Note
>
> We believe that creating a predictable driver release cadence will result in better update user experience across both Windows 10 OS and driver updates. We encourage ecosystem partners to _plan for their driver flighting and publication releases_ in alignment with above cadence and help us improve the experience of our mutual users and customers. 
 
## Appendix
### FAQ:
1. What does this deferral mean for newly submitted drivers or drivers currently In-Flight?
* This deferral is for the actual “Release” of a driver needing “Microsoft Approval” (marked as Automatic or Dynamic Update) to WU.  Newly submitted drivers and drivers currently In-Flight will proceed as they normally do.  

2. <a id="calendar"></a>What is the latest deferral calendar?
** This calendar is subject to changes based on OS release timelines.
 
![2021 Driver Release Calendar showing excluded dates as described above.](images/2021driverReleaseCalendar.png)