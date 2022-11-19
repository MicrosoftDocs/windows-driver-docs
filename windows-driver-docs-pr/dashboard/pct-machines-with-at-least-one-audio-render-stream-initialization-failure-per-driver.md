---
title: Percent of machines with at least one audio render stream initialization failure per driver
description: The measure will track the percentage of device endpoints with atleast one audio stream initialization render failure.
ms.topic: article
ms.date: 11/07/2022
---

# Percent of machines with at least one audio render stream initialization failure per driver

## Description

See the "Audio stream initialization" section at [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio Measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement Criteria**|	Aggregation of machine endpoints|
|**Minimum Population**|1000 machines
|**Passing criteria**|<=1.5% of machine endpoints have at least 1 render audio steam initialization failure|
|**Measure ID**|27539296|

## Calculation
1.	Measure is accounting for failures at an endpoint level, that is, if there is a failure on a specific endpoint that the driver is targeting, it is counted as a failure.
2.	The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines’ endpoints that have at least one unexpected initialization failure**
3.	*Machine endpoint with initialization failure = Count(endpoints driver is targeting with at least 1 unexpected render initialization failure)*
4.	*Total machine endpoints = Count(machine endpoints targeted by driver that attempted to initialize an audio render stream)*


### Final calculation

*Percent of machines with at least 1 render stream initialization failure = Machine endpoints targeted by driver with render initialization failure / Total machine endpoints targeted by driver*
