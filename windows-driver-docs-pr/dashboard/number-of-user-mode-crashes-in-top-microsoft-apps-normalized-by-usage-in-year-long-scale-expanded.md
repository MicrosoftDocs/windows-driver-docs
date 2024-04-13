---
title: Number of user mode crashes in top Microsoft apps
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in top Microsoft apps, caused by the graphics drivers, over total runtime in years 
ms.topic: article
ms.date: 08/08/2019
---

# Number of user mode crashes in top Microsoft apps, normalized by usage, is less than or equal to the baseline goal

## Description

When users open and use applications, their graphics components will process the apps’ visual information and display the rendered view on the user’s screen. This measure is monitoring how often top Microsoft apps are crashing, in relation to the runtime of those applications on all devices with the driver. If an application crashes, the user must wait for it to recover before being able to use it again.

This measure is normalized by usage, in a year-long scale.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|50,000 hours of Top Microsoft apps runtime|
|**Passing criteria**|<= 1.5 crash per year of runtime|
|**Measure ID**|21839387|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **ratio of crashes in top Microsoft apps, caused by the graphics drivers, over total runtime in years**.
2. *Total crashes in top Microsoft apps = count(top Microsoft app crashes on machines that have the driver)*
3. *Total runtime of top Microsoft apps = sum(runtime of top Microsoft apps, for each machine that has the driver)*
4. *Runtime in years = Total runtime of top Microsoft apps in seconds / (60 (minute) \* 60 (hour) \* 24 (day) \* 365 (year))*

### Final calculation

*Crashes in top Microsoft apps normalized by usage = Total crashes in top Microsoft apps / Runtime in years*
