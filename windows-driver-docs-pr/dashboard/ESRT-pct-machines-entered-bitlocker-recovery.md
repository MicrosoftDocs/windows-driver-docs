---
title: Percent of machines updated and successfully unlocked bitlocker recovery
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a bitlocker recovery event over the machines that attempted a firmware install
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines updated and successfully unlocked bitlocker recovery

## Description

Percent of machines that installed firmware and entered bitlocker recovery causing the customer to recover by entering the bitlocker recovery key

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a bitlocker recovery event over the machines that attempted a firmware install

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

