---
title: Number of crashes and hangs in Win32 games
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes and hangs over runtime in Win32 games.
ms.topic: article
ms.date: 10/24/2019
ms.localizationpriority: medium
---
 
# Number of crashes and hangs in Win32 games, normalized by usage, is less than or equal to the baseline goal

## Description

When users are playing Win32 games, their graphics components will process visual data and then display the rendered view on the user’s screen. This measure is monitoring how often Win32 games are crashing & hanging due to the graphics component, in relation to the runtime of those applications on all devices with the driver. If an application crashes, the user can lose their progress and must wait for it to recover before being able to use it again.  

This measure is normalized by usage, in a year-long scale.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|100 hours of Win32 games runtime|
|**Passing criteria**|<= 5 crashes per year of runtime|
|**Measure ID**|22843841|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **ratio of crashes and hangs over runtime in Win32 games**.
2. *Total Win32 game crashes and hangs = count(crashes and hangs in Win32 gaming applications for each machine that has the driver)*
3. *Total Win32 gaming runtime = sum(runtime of all Win32 games on each machine that has the driver)*
4. *Runtime in years = Total Win32 gaming runtime \* 60 (minute) \* 60 (hour) \* 24 (day) \* 365 (year)*

### Final calculation

*Crashes in Win32 games normalized by usage = Total Win32 game crashes and hangs / Runtime in years*
