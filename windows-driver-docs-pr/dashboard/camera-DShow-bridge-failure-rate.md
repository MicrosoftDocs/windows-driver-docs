---
title: Percent of Camera DShow Bridge Engine Failures
description: This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera DShow bridge engine failure.
ms.date: 03/13/2025
ms.topic: reference
---

# Percent of camera DShow bridge engine failures

## Description

A driver-level measure used to track the camera DShow bridge engine failures. This measure tracks the percentage of distinct devices with at least one failure, determined by either the `CreateHResult`, `LoadHResult`, or `RunHResult` containing a nonzero value.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Camera DShow measure capture data from any machine that is using the camera through the DShow engine on Windows. |
| **Time period** | 30 day sliding window |
| **Machine vs. Instance** | Percentage of machine |
| **Minimum population** | NA |
| **Passing criteria** | <= 10% of devices have at least one camera DShow engine failure |
| **Measure ID** | 50182120 |

## Calculation

1. This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera DShow engine failure.

1. Camera DShow bridge machines

    `Count(Machines from Microsoft.Windows.DShow.MFProxy.DShowKsProxyEvents)`

1. Camera DShow bridge machine failures

    `Count(machines with CreateHResult != 0 OR LoadHResult != 0 OR RunHResult != 0)`

### Final calculation

Camera DShow machine failures / Camera DShow machines
