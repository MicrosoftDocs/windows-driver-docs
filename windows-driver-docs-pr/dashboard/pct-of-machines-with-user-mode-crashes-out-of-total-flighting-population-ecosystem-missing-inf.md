---
title: Percent of machines with user mode crashes out of the total flighting population (ecosystem, missing INF matching ID)
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one user mode crash
ms.date: 10/22/2025
ms.topic: reference
---

# Percent of machines with user mode crashes out of the total flighting population (ecosystem, missing INF matching ID)

## Description

This is a measure of the percentage of machines with user mode crashes with valid FailureInfo data out of the total flighting population, where the failing device does not have a hardware ID that matches the hardware ID of the submission.

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
