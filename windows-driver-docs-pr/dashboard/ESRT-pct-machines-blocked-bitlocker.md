---
title: Percent of machines with pending firmware updates due to Bitlocker Risk
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that were blocked by bitlocker over the machines that attempted a firmware install
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines with pending firmware updates due to Bitlocker Risk

## Description

Percent of machines that installed a firmware and was blocked by bitlocker 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|250|
|**Passing criteria**|>= 90%|
|**Measure ID**|23153969|

## Calculation

number of machines that was blocked by bitlocker /

number of machines that attempted a firmware install

