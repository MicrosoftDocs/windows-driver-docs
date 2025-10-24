---
title: Percent of Machines With User Mode Crashes Out of the Total Flighting Population (Non-Ecosystem, With INF Matching ID)
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of machines that have at least one user mode crash, for non-ecosystem drivers with an INF matching ID
ms.date: 10/22/2025
ms.topic: reference
---

# Percent of machines with user mode crashes out of the total flighting population (non-ecosystem, with Setup Information File (INF) matching ID)

Unexpected user-mode crashes can degrade device reliability and lead to poor user experiences. To help identify and mitigate these issues, Microsoft tracks the percentage of machines affected by such crashes within the flighting population. This measure focuses specifically on non-ecosystem drivers where the failing device has a matching Setup Information File (INF) hardware ID in the submission. By monitoring this metric, Microsoft and hardware partners can detect driver mismatches, improve INF coverage, and enhance overall system stability.

## Description

This metric shows how many machines had user-mode crashes with valid FailureInfo data. It includes only devices whose hardware ID matches the one in the submission, based on the total flighting population.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|In-Flight|
|**Time period**|60-day window|
|**Machine vs. Instance**|Machine|
|**Minimum population**|25 machines|
|**Passing criteria**|value <= 0.5%|
|**Measure ID**| 55368551 |

## Calculation

This measure is calculated by taking the count of failing machines per Promotion Request ID and dividing it by the total population per Promotion Request ID.
