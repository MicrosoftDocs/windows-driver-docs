---
title: Number of crashes and hangs in UWP games, normalized by usage, in a year-long scale
description: The measure aggregates telemetry from a 14-day sliding window into a percentage of machines that haven’t experienced a kernel mode crash 
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Number of crashes and hangs in UWP games, normalized by usage, is less than or equal to the baseline goal

## Description

When users are playing UWP games, their graphics components process visual data and then display the rendered view on the screen. This measure monitors how often UWP games crash and hang due to the graphics component, in relation to the runtime of those applications on all devices with the driver. If an application crashes, the user can lose their progress and must wait for it to recover before being able to use it again.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|100 hours of UWP games runtime|
|**Passing criteria**|<= 5 crashes per year of runtime|
|**Measure ID**|14842478|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **ratio crashes and hangs in UWP games over runtime normalized to years**
2. *Total UWP game crashes and hangs = count(crashes and hangs in UWP gaming applications for each machine that has the driver)*
3. *Total UWP gaming runtime = sum(runtime of all UWP games on each machine that has the driver)*
4. *Runtime in years = Total UWP gaming runtime \* 60 (minute) \* (hour) \* 24 (day) \* 365 (year)*

### Final calculation

*Crashes in UWP games normalized by usage = Total UWP game crashes and hangs / Runtime in years*  
