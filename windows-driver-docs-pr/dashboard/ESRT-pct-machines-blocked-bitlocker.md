---
title: Percent of machines with pending firmware updates due to Bitlocker Risk
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that were blocked by bitlocker over the machines that attempted a firmware install
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines with pending firmware updates due to Bitlocker Risk

## Description

Percent of machines with pending firmware updates due to the risk of entering bitlocker recovery post install. This is due to customers running versions less than Windows 10 w/ June 2018 cumulative updates.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|<= 5%|
|**Measure ID**|23260737|

## Calculation

number of machines that was blocked by bitlocker /

number of machines that attempted a firmware install

