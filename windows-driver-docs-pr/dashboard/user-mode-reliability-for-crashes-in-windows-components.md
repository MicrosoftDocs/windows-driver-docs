---
title: User mode reliability for crashes in Windows Components, normalized by population, is less than or equal to the baseline goal
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in Microsoft Components, caused by the graphics drivers, over total runtime in years 
ms.topic: article
ms.date: 08/08/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Graphics drivers' health: User mode reliability for crashes in Windows Components Photos app, normalized by population, is less than or equal to the baseline goal

## Description

This measure is monitoring how often Windows Components (e.g. dwm.exe, shell, logon ui, etc.) are crashing in the display driver, in relation to the number of all devices using the driver. If Windows Component crashes, the user must wait for it to recover before being able to use it again.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of Machines|
|**Minimum instances**|10,000 devices|
|**Passing criteria**|<= 15 crashes per 10,000 devices|
|**Measure ID**|22725967|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into the Ratio of Crashes in Windows Components, caused by the graphics drivers, over all machines with the driver
2. *Total Crashes in Windows Components = Count(Windows Component crashes on machines that have the driver)*
3. *Total Devices = Sum(Machines that have the driver)*

### Final Calculation 

4. *Crashes in Windows Components Normalized by device count = Total Windows Component Crashes * 10000 / TotalDevices*
