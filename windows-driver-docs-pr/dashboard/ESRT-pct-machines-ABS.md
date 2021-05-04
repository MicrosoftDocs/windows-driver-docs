---
title: Percent of machines with abnormal shutdown not due to bugcheck or power button
description: The measure aggregates telemetry from a 28-day sliding window into a ratio of machines reported abnormal shutdown within 3 days of installation / machines successfuly installed
ms.topic: article
ms.date: 10/31/2019
ms.localizationpriority: medium
---
 
# Percent of machines with abnormal shutdown not due to bugcheck or power button

## Description

Percent of machines with successful installations where the machine abnormally shutdown for reasons excluding bugcheck (which automatically triggers an ABS) or ungraceful power button shutdown within 3 days of install, and did not abnormally shutdown 3 days before install.

The measure aggregates telemetry from a 28-day sliding window into a ratio of machines reported abnormal shutdown within 3 days of installation / machines successfuly installed

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Retail and Insider|
|**Time period**|28 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|170|
|**Passing criteria**|<= 20%|
|**Measure ID**|23260722|

## Calculation

machines reporting abnormal shutdown within 3 days of successful installation (defined by measure 20116729), and not ABS 3 days prior /

machines successfully installing

