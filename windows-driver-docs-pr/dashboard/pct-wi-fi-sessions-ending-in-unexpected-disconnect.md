---
title: Percentage of Wi-Fi sessions ending in a disconnection with more than 50% signal quality
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device unexpectedly disconnects from Wi-Fi
ms.topic: article
ms.date: 01/23/2023
---

# Percentage of Wi-Fi sessions ending in a disconnection with more than 50% signal quality

## Description

Once a device successfully connects to Wi-Fi, it must maintain that connection, so the device can continuously access the internet. This measure monitors for any unexpected Wi-Fi disconnections. If a user's device has an unexpected Wi-Fi disconnect their internet-dependent applications won't work properly, and they are either presented with a warning icon (an exclamation point on a yellow field) on the Internet access button or the machine fully disconnects from the internet.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Measurement criteria** | Device / AP pair aggregation |
| **Minimum instances** | 1,000 instances |
| **Passing criteria** | <= 26% of Instances don't end in an unexpected disconnect |
| **Measure ID** | 40408290 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device unexpectedly disconnects from Wi-Fi.

   1. The measure aggregates multiple instances from the same Device-AP pair into a single data point.
   2. The measure does not aggregate any Device–AP pairs if their signal strength is below 50%.

2. Expected disconnections are:

   1. User disconnects
   2. Machine powers down
   3. Disconnected due to low power state
   4. Switching to ethernet

3. An unexpected disconnect is counted as 100 and successful sessions are counted as zero

### Final calculation

Percent of Wi-Fi sessions ending in an unexpected disconnect = average (all instances)
