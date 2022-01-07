---
title: Number of user mode crashes or TDRs in Win32 gaming applications
description: Counts the number of crashes in display drivers that happen in the context of Win32 gaming applications
ms.topic: article
ms.date: 07/20/2021
---

# Number of user mode crashes or TDRs in Win32 gaming applications

## Description

This measure counts the number of crashes in display drivers that happen in the context of Win32 gaming applications and calculates the run time of such applications on all machines that have the updated driver. The measure then normalizes the crash count by cumulative application runtime in years (HOART - hit over application runtime).

This measure is normalized by usage, less than or equal to the baseline goal.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|1,000 hours of gaming application runtime|
|**Passing criteria**|<= 5 crashes per year of runtime|
|**Measure ID**|22843841|

## Calculation

1.	The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in gaming applications, caused by the graphics driver, over total runtime in years.
2.	Total crashes in gaming applications = count(crashes in gaming applications on machines that have the driver)
3.	Total gaming applications runtime = sum(runtime of gaming applications, for each machine that has the driver)
4.	Runtime in years = Total gaming applications runtime * 60 (minute) * 60 (hour) * 24 (day) * 365 (year)

### Final calculation

Crashes in gaming applications normalized by usage in years = Total crashes in gaming applications / Runtime in years
