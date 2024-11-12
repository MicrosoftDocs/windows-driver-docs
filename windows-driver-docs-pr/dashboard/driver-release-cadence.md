---
title: Driver Ship Room Release Cadence Windows
description: This page provides information on the operation schedule for driver ship room. In order to provide the best experience for Windows users, there are certain times where aspects of publication operations are suspended.
ms.topic: article
ms.date: 11/11/2024
---

# Driver Ship Room Release Cadence Windows

Last Updated: November 11, 2024

This article provides information on the operation schedule for Windows driver ship room. In order to provide the best experience for Windows users, there are certain times where aspects of publication operations are suspended.

We have a shared goal of keeping devices up to date while providing users a high quality experience. When a driver update is released alongside OS updates, it results in a poor experience and impacts end-users.

Windows as a Service has a well-established OS update release cadence.

- **Latest Cumulative Update (LCU)**: Monthly quality and security updates are released during the second week. The LCU is also known as the *B* release, and is offered to all eligible Windows 10 devices through Windows Update (WU) scans.

- **Feature Updates**: Provide the latest feature experiences and quality fixes.

There are changes for releasing drivers marked as needing *Microsoft approval*. These changes ensure we release quality drivers, reduce the risk of releasing drivers at the same time as OS changes, and provide ecosystem partners a predictable driver release cadence. The drivers affected by these changes include:

- Flighted drivers: Drivers (shipping label) marked as **Automatic** = Critical Update (CU) or Dynamic Update (DU) or both
- Optional driver classes which always go through ship room approval

**Predictable driver release windows**: During OS update release time frames, we defer releasing drivers needing *Microsoft approval* to WU and will resume automatic publishing after the deferral window.

1. **Monthly Quality Update *B* release**: Drivers needing *Microsoft approval* aren't released one day before and for one day after monthly security *B* release.

    | Monday | Second Tuesday of each month | Wednesday |
    |--|--|--|
    | One day before | *B* monthly security release day | One day after |

1. **Feature update offer via Windows Update**: Driver needing *Microsoft approval* aren't released two days before, and for two days after the start of a feature OS update rollout.

    | Before | Day Of | After |
    |--|--|--|
    | Two days before | Feature OS Rollout | Two days after |

    If there are known issues for feature update and driver compatibility, you can request a *feature update offer block mitigation* while a compatible driver update is being validated and posted to WU.

1. **Certain US holidays**: Drivers needing *Microsoft approval* aren't released on certain US Holidays and long weekends

    | US Holidays | 2025 | 2024 |
    |--|--|--|
    | New Year's Day | Wednesday, January 01 | Monday, January 01 |
    | Martin Luther King Day | Monday, January 20 | Monday, January 17 |
    | Presidents Day | Monday, February 17 | Monday, February 19 |
    | Memorial Day | Monday May 26 | Monday May 27 |
    | Fourth of July | Friday, July 04 | Tuesday, July 04 |
    | Labor Day | Monday, September 01 | Monday, September 02 |
    | Thanksgiving Day | Thursday, November 27 | Thursday, November 28 |
    | Day after Thanksgiving | Friday, November 28 | Friday, November 29 |
    | Christmas Eve | Wednesday, December 24 | Tuesday, December 24 |
    | Christmas Day | Thursday, December 25 | Wednesday, December 25 |
    | Day after Christmas | Friday, December 26 | Thursday, December 26 |

1. **US Winter Holiday time frame release moratorium**: During the US winter holiday season, the driver ship room isn't releasing *any* drivers. For calendar year 2024, the time frame is December 14, 2024 through January 1, 2025. For calendar year 2025, the time frame is December 18, 2025 through January 1, 2026.

    See the calendars in the [Appendix](#appendix) for more dates.

> [!NOTE]
> Because a predictable driver release cadence results in a better user experience, we encourage ecosystem partners to plan for driver flighting and publication releases.

## Appendix

### FAQ

1. What does this deferral mean for newly submitted drivers or drivers currently In-Flight?

    This deferral is for the release of a driver needing *Microsoft approval* (marked as Automatic or Dynamic Update) to WU. Newly submitted drivers, and drivers currently in-flight, proceed as they normally do.

1. What is the latest deferral calendar?

    **These calendars are subject to change based on OS release timelines.**

    :::image type="content" source="images/2024_driver_calendar.png" alt-text="September - December 2024 driver release calendar showing excluded dates.":::

    :::image type="content" source="images/2025_driver_calendar.png" alt-text="September - December 2025 driver release calendar showing excluded dates.":::
