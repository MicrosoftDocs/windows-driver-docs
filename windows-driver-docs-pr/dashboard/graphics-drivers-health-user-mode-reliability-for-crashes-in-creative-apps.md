---
title: Number of user mode reliability for crashes in creative applications
description: Learn about the measure that counts crashes in display drivers that happen in creative applications. The measure then normalizes the total runtime to years.
ms.topic: article
ms.date: 05/20/2019
---

# Number of user mode reliability for crashes in creative applications, normalized by usage, is less than or equal to the baseline goal

## Description

This measure counts the number of crashes in display drivers that happen in the context of the creative applications and calculating the runtime of [creative applications](measure-appendix.md#creative-applications-example) on all machines that have the updated driver. The measure then normalizes the total runtime to years, indicating the number of crashes a user would experience if they used the creative applications for a year.

This measure is normalized by usage, which is less than or equal to the baseline goal.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|1,000 hours of creative application runtime|
|**Passing criteria**|<= 10 crashes per year of runtime|
|**Measure ID**|20240835 (Legacy)|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **ratio of crashes in creative applications, caused by the graphics drivers, over total runtime in years**.
2. *Total crashes in creative applications = count(crashes in creative applications on machines that have the driver)*
3. *Total creative applications runtime = sum(runtime of creative applications, for each machine that has the driver)*
4. *Runtime in years = Total creative applications runtime in seconds  / (60 (minute) \* 60 (hour) \* 24 (day) \* 365 (year))*

### Final calculation

*Crashes in creative applications normalized by usage in years = Total crashes in creative applications / Runtime in years*
