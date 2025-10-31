---
title: Percent of Machines With WUDF User Mode Crashes Out of the Total Flighting Population (Ecosystem, Missing INF Matching ID)
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of machines that have at least one WUDF user mode crash, for ecosystem drivers without a missing INF matching ID
ms.date: 10/31/2025
ms.topic: reference
---

# Percent of machines with WUDF user mode crashes out of the total flighting population (ecosystem, missing Setup Information File (INF) matching ID)

WUDF (Windows User-Mode Driver Framework) is a Microsoft driver model that allows certain device drivers to run in user mode rather than kernel mode, improving system stability and security. However, unexpected crashes in WUDF-hosted drivers can degrade device reliability and lead to poor user experiences. To help identify and mitigate these issues, Microsoft tracks the percentage of machines affected by such crashes within the flighting population. This measure focuses specifically on ecosystem drivers where the failing device lacks a matching Setup Information File (INF) hardware ID in the submission. By monitoring this metric, Microsoft and hardware partners can detect driver mismatches, improve INF coverage, and enhance overall system stability.

## Description

This metric shows the percentage of machines with WUDF user-mode crashes and valid FailureInfo data, where the failing device doesn't have a hardware ID that matches the hardware ID in the submission.
It reflects the total flighting population.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail|
|**Time period**|60-day window|
|**Machine vs. Instance**|Machine|
|**Minimum population**|25 machines|
|**Passing criteria**|value <= 0.5%|
|**Measure ID**| 55581235 |

## Calculation

This measure is calculated by taking the count of failing machines per Promotion Request ID and dividing it by the total population per Promotion Request ID.
