---
title: Percent of machines with a kernel mode crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have experienced a kernel mode crash 
ms.topic: article
ms.date: 05/29/2020
---

# Percent of machines without a kernel mode crash

## Description

A Kernel Mode Crash (KMC) is caused by a kernel error which halts the Operating System. When users experience a KMC, their machine abruptly crashes, and they are presented with a blue screen. This type of crash can cause an interruption in the user’s workflow and lead to data loss.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<= 1% machines did encounter a kernel mode crash|
|**Cohort-enabled**|Yes|
|**Minimum population per cohort**|500 machines|
|**Measure ID**|26118008|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have experienced a KMC.**
2. *Crashing Machines = Count(machines that have installed the driver with a KMC)*
3. *Total Machines = Count(machines that successfully installed the driver)*

### Final calculation

*Percentage of Machines without a KMC = Crashing Machines / Total Machines*
