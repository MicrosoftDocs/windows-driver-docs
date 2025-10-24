---
title: Percent of Machines With User Mode Crashes Out of the Total Flighting Population (Ecosystem, Missing INF Matching ID)
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of machines that have at least one user mode crash, for ecosystem drivers without a missing INF matching ID
ms.date: 10/22/2025
ms.topic: reference
---

# Percent of machines with user mode crashes out of the total flighting population (ecosystem, missing Setup Information File (INF) matching ID)

Unexpected user-mode crashes can degrade device reliability and lead to poor user experiences. To help identify and mitigate these issues, Microsoft tracks the percentage of machines affected by such crashes within the flighting population. This measure focuses specifically on ecosystem drivers where the failing device lacks a matching Setup Information File (INF) hardware ID in the submission. By monitoring this metric, Microsoft and hardware partners can detect driver mismatches, improve INF coverage, and enhance overall system stability.

## Description

This metric shows the percentage of machines with user-mode crashes and valid FailureInfo data, where the failing device doesn't have a hardware ID that matches the hardware ID in the submission.
It reflects the total flighting population.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail|
|**Time period**|60-day window|
|**Machine vs. Instance**|Machine|
|**Minimum population**|25 machines|
|**Passing criteria**|value <= 0.5%|
|**Measure ID**| 55368584 |

## Calculation

This measure is calculated by taking the count of failing machines per Promotion Request ID and dividing it by the total population per Promotion Request ID.
