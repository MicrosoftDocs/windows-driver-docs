---
title: Percent of Legacy Camera DShow failures
description: This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera DShow engine failure.
ms.date: 03/12/2025
ms.topic: reference
---

# Percent of legacy camera DShow failures

## Description

A driver-level measure used to track the legacy camera DShow engine failures. This measure tracks the percentage of distinct devices with at least one failure, determined by either the `CreateHResult`, `LoadHResult`, or `RunHResult` containing a nonzero value.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Camera DShow measure capture data from any machine that is using the camera through the DShow engine on Windows. |
| **Time period** | 30 day sliding window |
| **Machine vs. Instance** | Percentage of machine |
| **Minimum population** | NA |
| **Passing criteria** | <= 10% of devices have at least 1 camera DShow engine failure |
| **Measure ID** | 50182242 |

## Calculation

1. This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera device failure.

1. Legacy camera DShow machines

    `Count(Machines from Microsoft.Windows.DShow.KsProxy.DShowKsProxyEvents)`

1. Legacy camera DShow machine failures

    `Count(machines with CreateHResult != 0 OR LoadHResult != 0 OR RunHResult != 0)`

### Final calculation

Camera DShow Machine Failures / Camera DShow Machines
