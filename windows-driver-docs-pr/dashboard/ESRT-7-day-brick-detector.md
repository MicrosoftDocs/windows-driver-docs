---
title: Percent of machines that successfully installed firmware and have seen no heartbeat within 7 days
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that have not reported any telemetry in 7 days over machines that successfully installed the firmware
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines that successfully installed firmware and have seen no heartbeat within 7 days

## Description

Percent of machines successfully installing firmware that has have seen no heartbeat for 7 days.   

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines that have not reported any telemetry in 7 days over machines that successfully installed the firmware

This is to detect machines that have potentially bricked. 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|> 50%|
|**Measure ID**|23260730|

## Calculation

machines not heartbeating within 7 days /

machines that have successfully installed the firmware (per measure 20116729)

