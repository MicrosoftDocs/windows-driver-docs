---
title: Internet connection failures of device and access-point pairs with more than 50% signal quality
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device fails to connect to the internet via Wi-Fi.
ms.topic: article
ms.date: 01/23/2023
---

# Internet connection failures of device and access-point pairs with more than 50% signal quality

## Description

After a device connects to an access point (AP), it can use that connection to attempt connecting to the internet via Wi-Fi. When users are unable to use Wi-Fi to connect to the internet, they are presented with a warning icon (an exclamation point on a yellow field) on the internet access button. They are unable to fully operate applications that need Wi-Fi.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Measurement criteria** | Device / AP pair aggregation  |
| **Minimum instances** | 1,000 |
| **Passing criteria** | <= 6% of Instances have connection failures to internet via Wi-Fi |
| **Measure ID** | 32321427 (Legacy), 40722956 |

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device fails to connect to the internet via Wi-Fi.

   1. An instance is a pairing between a machine and unique AP; per device–AP pair, the measure aggregates every attempted connection to internet via Wi-Fi to a single data point.
   1. The measure does not aggregate any device–AP pairs if their signal strength is below 50%.

1. A connection failure is counted as 100 and a connection success is counted as zero

### Final calculation

Connection failure rate of device–AP pairs to Internet failure = average(all instances)
