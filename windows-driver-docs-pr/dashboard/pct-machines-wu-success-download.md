---
title: Percent of machines that WU reported a successful download within the last 28 days
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that reported a successful download from Windows Update
ms.topic: article
ms.date: 02/28/2020
ms.localizationpriority: medium
---
 
# Percent of machines that WU reported a successful download within the last 28 days

## Description

Percent of machines that WU reported a successful download within the last 28 days

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
