---
title: Number of user mode reliability for crashes in Windows Components, normalized by population, is less than or equal to the baseline goal (Ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in Microsoft Components, caused by the graphics drivers, over total runtime in years 
ms.topic: article
ms.date: 08/08/2019
ms.localizationpriority: medium
---

# Number of user mode reliability for crashes in Windows Components Photos app, normalized by population, is less than or equal to the baseline goal (Ecosystem)

## Description

This measure is monitoring how often Windows Components (e.g. dwm.exe, shell, logon ui, etc.) are crashing in the display driver, in relation to the number of all machines using the driver. If Windows Component crashes, the user must wait for it to recover before being able to use it again.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|10,000 machines|
|**Passing criteria**|<= 15 crashes per 10,000 machines|
|**Measure ID**|20240811|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into the **ratio of crashes in Windows Components, caused by the graphics drivers, over all machines with the driver**
2. *Total Crashes in Windows Components = Count(Windows Component crashes on machines that have the driver)*
3. *Total Devices = Sum(Machines that have the driver)*

### Final Calculation 

4. *Crashes in Windows Components Normalized by device count = Total Windows Component Crashes * 10,000 / Total Devices*
