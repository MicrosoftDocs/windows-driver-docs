---
title: Percent of internet connection failures of device and access-point pairs that have greater than 50 percent signal quality
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of instances where a device Fails to connect to the Internet via Wi-Fi.
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of internet connection failures of device and access-point pairs that have greater than 50 percent signal quality

## Description

After a device connects to an access point (AP), it can use that connection to attempt connecting to the internet via Wi-Fi. When users are unable to use Wi-Fi to connect to the internet, they are presented with a warning icon (an exclamation point on a yellow field) on the Internet access button. They are unable to fully operate applications that need Wi-Fi.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 days|
|**Measurement criteria**|Aggregation of instances|
|**Minimum instances**|3,000|
|**Passing criteria**|<= 10% of Instances have connection failures to Internet via Wi-Fi|
|**Measure ID**|25975470|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of instances where a device Fails to connect to the Internet via Wi-Fi**.

   a. An instance is a pairing between a machine and unique AP; per device–AP pair, the measure aggregates every attempted connection to internet via Wi-Fi to a single data point.

   b. The measure does not aggregate any device–AP pairs if their signal strength is below 50%.

2. A connection failure is counted as “100” and a connection success is counted as “0”

### Final calculation

*Connection failure rate of device–AP pairs to Internet failure = average(all instances)*