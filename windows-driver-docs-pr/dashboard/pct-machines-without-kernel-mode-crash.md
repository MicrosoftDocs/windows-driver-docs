---
title: Percent of machines without a kernel mode crash
description: The measure aggregates telemetry from a 14-day sliding window into a percentage of machines that haven’t experienced a kernel mode crash 
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of machines without a kernel mode crash

## Description

A Kernel Mode Crash (KMC) is caused by a kernel error which halts the Operating System. When users experience a KMC, their machine abruptly crashes, and they are presented with a blue screen. This type of crash can cause an interruption in the user’s workflow and lead to data loss.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|14 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|>= 96% machines did not encounter a kernel mode crash|
|**Measure ID**|19888712|

## Calculation

1. The measure aggregates telemetry from a 14-day sliding window into a **percentage of machines that haven’t experienced a KMC.**
2. *Non Crashing Machines = Count(machines that have installed the driver without a KMC)*
3. *Total Machines = Count(machines that successfully installed the driver)*

### Final calculation

*Percentage of Machines without a KMC = Non Crashing Machines / Total Machines*
