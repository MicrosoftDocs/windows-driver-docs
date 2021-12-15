---
title: Number of user mode crashes in Windows components (ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a ratio of crashes in Microsoft Components, caused by the graphics drivers, over total runtime in years 
ms.topic: article
ms.date: 09/03/2021
---

# Number of user mode crashes in Windows components (ecosystem)

## Description

This measure is monitoring how often Windows components (dwm.exe, shell, logon ui, and so on) are crashing in the display driver, in relation to the number of all machines using the driver. If Windows component crashes, the user must wait for it to recover before being able to use it again.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum instances** | 10,000 machines |
| **Passing criteria** | <= 15 crashes per 10,000 machines |
| **Measure ID** | 20240811 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into the ratio of crashes in Windows components, caused by the graphics drivers, over all machines with the driver
1. Total crashes in Windows components = Count(Windows component crashes on machines that have the driver)
1. Total devices = Sum(machines that have the driver)

### Final Calculation

Crashes in Windows components normalized by device count = Total Windows component crashes * 10,000 / total devices
