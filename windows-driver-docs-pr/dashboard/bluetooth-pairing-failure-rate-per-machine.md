---
title: Percent of Bluetooth pairing failures
description: 
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of Bluetooth pairing failures

## Description

On a successful Bluetooth pairing, the authentication information is saved locally for future usage. If the devices are unable to pair, the user will not be able to authenticate their connection and cannot stream content between the devices.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of instances|
|**Minimum population**|10 instances|
|**Passing criteria**|<=5 % of Instances are pairing failures|
|**Measure ID**|14612509|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of instances where a Bluetooth device failed to pair with another device**.

   a. *A single machine can have multiple pairing Instances counted by the measure*

2. Types of Instances:

   a. *Successful pairing event = 0% failure*

   b. *Pairing cancel event or neutral pairing = 5% failure*

   c. *Timeout = 20% failure*

   d. *Failure to pair event = 100% failure*

### Final calculation

*Bluetooth pairing failure rate = average (all occurrences)*