---
title: Percent of machines with a live kernel dump
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have experienced a live kernel dump
ms.topic: article
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# Percent of machines without a live kernel dump

## Description

A live kernel dump (LKD) is the product of a kernel error, where the machine can recover without crashing. When users experience an LKD, their applications can hang or crash. A common type of LKD is timeout detection and recovery (TDR) in which the graphics driver crashes and the display momentarily goes black until the driver recovers.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<= 3% machines encounter an LKD|
|**Cohort-enabled**|Yes|
|**Minimum population per cohort**|500 machines|
|**Measure ID**|25739929 or 26118015|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have experienced an LKD**
2. *Machines With LKD = Count(machines that have installed the driver with an LKD)*
3. *Total Machines = Count(machines that successfully installed the driver)*

### Final calculation

*Percentage of Machines without an LKD = Machines with LKD / Total Machines*
