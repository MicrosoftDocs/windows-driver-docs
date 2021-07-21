---
title: Percent of machines that WU reported a successful download within the last 28 days
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a successful download from Windows Update
ms.topic: article
ms.date: 02/28/2020
ms.localizationpriority: medium
---
 
# Percent of machines that Windows Update (WU) reported a successful download within the last 28 days

## Description

Percent of machines that WU reported a successful download within the last 28 days
 
For more information about Windows Update error codes, see:
* [Windows Update error codes by component](/windows/deployment/update/windows-update-error-reference)
* [Windows Update common errors and mitigation](/windows/deployment/update/windows-update-errors)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|100|
|**Passing criteria**|>= 95%|
|**Measure ID**|24186432|

## Calculation

number of machines that WU reported a successful download (status == 0) / 

number machines that attempted a WU download