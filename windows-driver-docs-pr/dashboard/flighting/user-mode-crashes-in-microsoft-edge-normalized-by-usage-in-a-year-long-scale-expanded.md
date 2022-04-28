---
title: Number of user mode crashes in Microsoft Edge
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in Microsoft Edge, caused by the graphics drivers, over total runtime in years 
ms.topic: article
ms.date: 05/20/2019
---

# Number of user mode reliability for crashes in Microsoft Edge, normalized by usage, is less than or equal to the baseline goal

## Description

When users are browsing the internet with Microsoft Edge, their graphics components will process visual data from the Web and display the rendered view on the user’s screen. This measure is monitoring how often Microsoft Edge crashes, in relation to the Microsoft Edge runtime on all devices with the driver. If Microsoft Edge crashes, the user must wait for the application to recover before being able to use it again.

This measure is normalized, by usage, in a year-long scale.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|30,000 hours of Microsoft Edge runtime|
|**Passing criteria**|<= 1 crash per year of runtime|
|**Measure ID**|22728062|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **ratio of crashes in Microsoft Edge, caused by the graphics drivers, over total runtime in years**
2. *Total Microsoft Edge crashes = count(Microsoft Edge crashes on machines that have the driver)*
3. *Total Microsoft Edge runtime = sum(Microsoft Edge runtime for each machine that has the driver)*
4. *Runtime in years = total Microsoft Edge runtime \* 60 (minute) \* 60 (hour) \* 24 (day) \* 365 (year)*

### Final calculation

*Crashes in Microsoft Edge normalized by usage = Total Microsoft Edge crashes / Runtime in years*
