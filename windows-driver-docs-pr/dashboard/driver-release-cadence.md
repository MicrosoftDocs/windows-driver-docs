---
title: Driver Ship Room Release Cadence Windows
description: This article provides information about the operation schedule for Windows driver ship room. In order to provide the best experience for Windows users, there are certain times where aspects of publication operations are suspended.
ms.date: 11/25/2025
ms.topic: release-notes
---

# Driver ship room release cadence windows

Last Updated: November 25, 2025

This article provides information about the operation schedule for Windows driver ship room. In order to provide the best experience for Windows users, there are certain times where aspects of publication operations are suspended.

We have a shared goal of keeping devices up to date while providing users a high quality experience. When a driver update is released alongside OS updates, it results in a poor experience and impacts end-users.

Windows as a Service has a well-established OS update release cadence.

- **Latest Cumulative Update (LCU)**: Monthly quality and security updates are released during the second week. The LCU is also known as the *B* release, and is offered to all eligible Windows 11 devices through Windows Update (WU) scans.

- **Feature Updates**: Provide the latest feature experiences and quality fixes.

There are changes for releasing drivers marked as needing *Microsoft approval*. These changes ensure we release quality drivers, reduce the risk of releasing drivers at the same time as OS changes, and provide ecosystem partners a predictable driver release cadence. The drivers affected by these changes include:

- Flighted drivers: Drivers (shipping label) marked as **Automatic** = Critical Update (CU) or Dynamic Update (DU) or both
- Optional driver classes, which always go through ship room approval

**Predictable driver release windows**: During OS update release time frames, we defer releasing drivers needing *Microsoft approval* to Windows Update and will resume automatic publishing after the deferral window.

1. **Monthly Quality Update *B* release**: Drivers needing *Microsoft approval* aren't released one day before and for one day after monthly security *B* release.

    | Monday | Second Tuesday of each month | Wednesday |
    |--|--|--|
    | One day before | *B* monthly security release day | One day after |

1. **Feature update offer via Windows Update**: Drivers needing *Microsoft approval* aren't released two days before, and for two days after the start of a feature OS update rollout.

    | Before | Day Of | After |
    |--|--|--|
    | Two days before | Feature OS Rollout | Two days after |

    If there are known issues for feature update and driver compatibility, you can request a *feature update offer block mitigation* while a compatible driver update is being validated and posted to Windows Update.

1. **Certain US holidays**: Drivers needing *Microsoft approval* aren't released on certain US Holidays and long weekends

    | US Holidays | 2026 | 2025 |
    |--|--|--|
    | New Year's Day | Tuesday, January 01 | Wednesday, January 01 |
    | Martin Luther King Day | Monday, January 19 | Monday, January 20 |
    | Presidents Day | Monday, February 16 | Monday, February 17 |
    | Memorial Day | Monday, May 25 | Monday, May 26 |
    | Fourth of July | Friday, July 03 | Friday, July 04 |
    | Labor Day | Monday, September 07 | Monday, September 01 |
    | Thanksgiving Day | Thursday, November 26 | Thursday, November 27 |
    | Day after Thanksgiving | Friday, November 27 | Friday, November 28 |
    | Christmas Eve | Thursday, December 24 | Wednesday, December 24 |
    | Christmas Day | Friday, December 25 | Thursday, December 25 |
    | Day after Christmas | - | Friday, December 26 |

1. **US Winter Holiday time frame release moratorium**: During the US winter holiday season, the driver ship room isn't releasing *any* drivers. For calendar year 2025, the time frame is December 18, 2025 through January 1, 2026. For calendar year 2026, the time frame is December 18, 2026 through January 1, 2027.

    See the calendars in the [Appendix](#appendix) for more dates.

> [!NOTE]
> Because a predictable driver release cadence results in a better user experience, we encourage ecosystem partners to plan for driver flighting and publication releases.

## Appendix

### FAQ

1. What does this deferral mean for newly submitted drivers or drivers currently in-flight?

    This deferral is for the release of a driver needing *Microsoft approval* (marked as Automatic or Dynamic Update) to Windows Update. Newly submitted drivers, and drivers currently in-flight, proceed as they normally do.

1. What is the latest deferral calendar?

    **These calendars are subject to change based on OS release timelines.**

    :::image type="content" source="images/2025-driver-calendar.png" alt-text="September - December 2025 driver release calendar showing excluded dates.":::

    :::image type="content" source="images/2026-driver-calendar.png" alt-text="September - December 2026 driver release calendar showing excluded dates.":::
