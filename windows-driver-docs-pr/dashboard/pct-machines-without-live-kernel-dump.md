---
title: Percent of machines without a live kernel dump
description: The measure aggregates telemetry from a 14-day sliding window into a percentage of machines that haven’t experienced a live kernel dump
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of machines without a live kernel dump

## Description

A live kernel dump (LKD) is the product of a kernel error, where the machine can recover without crashing. When users experience an LKD, their applications can hang or crash. A common type of LKD is timeout detection and recovery (TDR) in which the graphics driver crashes and the display momentarily goes black until the driver recovers.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|14 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|>= 90% machines did not encounter an LKD|
|**Measure ID**|19888731|

## Calculation

1. The measure aggregates telemetry from a 14-day sliding window into a **percentage of machines that haven’t experienced an LKD**
2. *Machines Without LKD = Count(machines that have installed the driver without an LKD)*
3. *Total Machines = Count(machines that successfully installed the driver)*

### Final calculation

*Percentage of Machines without an LKD = Machines without LKD / Total Machines*
