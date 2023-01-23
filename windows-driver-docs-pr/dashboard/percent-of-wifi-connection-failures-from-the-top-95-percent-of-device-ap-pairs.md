---
title: Wi-Fi connection failures from devices and access-point pairs with more than 50% signal quality
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device fails to connect to an access point
ms.topic: article
ms.date: 01/23/2023
---

# Wi-Fi connection failures from devices and access-point pairs with more than 50% signal quality

## Description

A Wi-Fi access point (AP) is networking hardware that allows other Wi-Fi enabled devices to connect to a wireless local area network (WLAN). When users cannot connect to an AP, their machines display a connection error message and will not have access to the WLAN or Wi-Fi.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Targeted HWIDs and CHIDs |
| **Time period** | 7 days |
| **Measurement criteria** | Device / AP pair aggregation |
| **Minimum instances** | 1,000 |
| **Passing criteria** | <= 6% of Instances have connection failures to APs |
| **Measure ID** | 32321149 (Legacy), 40722983 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device fails to connect to an AP

   1. An instance is a pairing between a device and unique AP; per device, the measure aggregates every attempted connection to a unique AP.
   1. The measure does not aggregate any device–AP pairs if their signal strength is below 50%.

1. A connection failure is counted as 100 and a connection success is counted as zero

### Final calculation

Connection failure rate of device–AP pairs = average(all instances)
