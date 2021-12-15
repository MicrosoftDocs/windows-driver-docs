---
title: Percent of machines exceeded firmware max retry limit from ESRT
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that hit max retry over machines that had an install event
ms.topic: article
ms.date: 10/31/2019
---
 
# Percent of machines exceeded firmware max retry limit from ESRT

## Description

Percent of machines having successful installation that attempted to install a firmware and has exceeded the firmware max retry limit (defaults to 3).

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that hit max retry over machines that had an install event.

Many firmware that fail this measure are not abiding by the contract where the ESRT LastAttemptStatus field is not reporting a failure code as the ESRT version reported is the same as the previous version on the machine, prior to install. 

[Section 3 of this document](/windows-hardware/manufacture/desktop/validating-windows-uefi-firmware-update-platform-functionality) provides basic validation scenarios to ensure that the firmware implementation meets this requirement.  

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|<= 5%|
|**Measure ID**|23260704|

## Calculation

number of machines that installed a firmware that hit max retry limit /

number of machines that received a driver install event for a firmware device
