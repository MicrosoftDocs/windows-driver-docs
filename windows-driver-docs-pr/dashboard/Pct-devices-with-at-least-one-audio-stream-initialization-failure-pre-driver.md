---
title: Percent of devices with at least 1 audio stream initialization failure per Driver
description: This measure calculates the percentage of device endpoints with at least one audio stream initialization failure.
ms.topic: article
ms.date: 11/18/2022
---

# Percent of devices with at least 1 audio stream initialization failure per Driver

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement Criteria**|	Aggregation of machine endpoints|
|**Minimum Population**|1000 machines
|**Passing criteria**|<=2 % of machine endpoints with at least 1 audio stream initialization failure|
|**Measure ID**|26628516|

## Calculation

1.	Measure is accounting for failures at an endpoint level, that is, if there is a failure on a specific endpoint that the driver is targeting, it is counted as a failure.
2.	The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines’ endpoints that have at least one unexpected initialization failure**
3.	*Machine endpoint with initialization failure = Count(endpoints driver is targeting with at least 1 unexpected initialization failure)*
4.	*Total machine endpoints = Count(machine endpoints targeted by driver that attempted to initalizate an audio stream)*

### Final calculation

*Percent of machines with at least 1 stream initialization failure = Machine endpoints targeted by driver with initialization failure / Total machine endpoints targeted by driver*
