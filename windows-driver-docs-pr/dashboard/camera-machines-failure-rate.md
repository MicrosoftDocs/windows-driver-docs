---
title: Percent of Machines with Camera Failures 
description: This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera failure.
ms.date: 03/12/2025
---

# Percent of machines with camera failures

## Description

A driver-level measure used to track camera user-mode crashes per driver version. Specifically, this measure calculates the number of distinct devices with crashes over the total device population for a driver version.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Camera measures capture data from any machine using camera on Windows. |
| **Time period** | 30 day sliding window |
| **Machine vs. Instance** | Percentage of machine |
| **Minimum population** | NA |
| **Passing criteria** | <= 10% of devices have at least one camera failure |
| **Measure ID** | 49005400 |

## Calculation

1. This measure aggregates telemetry from a 30-day sliding window into a percentage of machines that had a camera failure.

1. Camera machines

    `Count(Daily Active Devices for a Driver)`

1. Camera machine failures

    `Count(Crashes for a Driver)`

### Final calculation

Camera Machine Failures / Camera Machines
