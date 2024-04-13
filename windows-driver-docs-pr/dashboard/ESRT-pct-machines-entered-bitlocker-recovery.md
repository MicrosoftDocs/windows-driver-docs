---
title: Percent of machines updated and successfully unlocked bitlocker recovery
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a bitlocker recovery event over the machines that attempted a firmware install
ms.topic: article
ms.date: 10/31/2019
---
 
# Percent of machines updated and successfully unlocked bitlocker recovery

## Description

Percent of machines that installed firmware and entered bitlocker recovery causing the customer to recover by entering the bitlocker recovery key

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a bitlocker recovery event over the machines that attempted a firmware install

Asking for the Bitlocker recovery key after a new firmware is most commonly due to the Platform Configuration Registers (PCR) 7 haveing unacceptable measurements for Bitlocker to seal, therefore Bitlocker reads legacy PCRs, which includes PCR 0. Since PCR 0 will change on a firmware update, Bitlocker will trigger recovery. To debug, look at one of these devices and see what is in PCR 7, then check if a component of the firmware package added any mechanism that would cause this condition (debug, dma protections off, option roms, 3rd party pre boot fw, etc.) to occur.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|<= 5%|
|**Measure ID**|23260740|

## Calculation

number of machines that reported the bit locker recovery event on boot /

number of machines that attempted to install a firmware

