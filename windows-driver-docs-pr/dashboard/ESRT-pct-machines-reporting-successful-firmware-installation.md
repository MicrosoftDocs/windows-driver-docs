---
title: Percent of machines reporting successful firmware installation from ESRT
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of successful installs over attempts
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines reporting successful firmware installation from ESRT

## Description

The measure aggregates telemetry from a 28-day sliding window into a ratio of successful installs over attempts.
A successful installation is defined where the following events happen:

1. firmware w/ device instance starting with UEFI is installed via drvinst
2. machine reboots and firmware is applied
3. UEFI.sys on boot reports a successful installation.


If the machine is reports a transient error (transient errors from UEFI.SYS are listed below) then it is not included in the population

|Error Code|Value|
|----|----|
|3221225659| STATUS_NOT_SUPPORTED|
|3221226195| STATUS_POWER_STATE_INVALID|
|3221226206| STATUS_INSUFFICIENT_POWER|
|3221225506| STATUS_ACCESS_DENIED|
|3221225473| STATUS_UNSUCCESSFUL|
|3221225517| STATUS_NOT_COMMITTED|
|3221225560| STATUS_UNKNOWN_REVISION|
|3221225626| STATUS_INSUFFICIENT_RESOURCES|
|3221226194| STATUS_PNP_REBOOT_REQUIRED|
|3221225659| STATUS_NOT_SUPPORTED|
|3221226195| STATUS_POWER_STATE_INVALID|
|3221226206| STATUS_INSUFFICIENT_POWER|
|3221225862| STATUS_DEVICE_PROTOCOL_ERROR|
|3221226681| STATUS_UNSATISFIED_DEPENDENCIES|
|3221226029| STATUS_RETRY|

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|>= 95%|
|**Measure ID**|23260700|

## Calculation

number of machines that were successful / 
number of machines that attempted a firmware device but excludes machines in a transient state

