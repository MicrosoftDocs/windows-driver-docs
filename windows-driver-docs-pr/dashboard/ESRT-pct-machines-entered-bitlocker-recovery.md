---
title: Percent of machines updated and successfully unlocked bitlocker recovery
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a bitlocker recovery event over the machines that attempted a firmware install
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines updated and successfully unlocked bitlocker recovery

## Description

% of machines that installed firmware and entered bitlocker recovery causing the customer recover by entering the bitlocker recovery key

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|250|
|**Passing criteria**|>= 90%|
|**Measure ID**|23154031|

## Calculation

number of machines that reported the bit locker recovery event on boot /

number of machines that attempted to install a firmware

