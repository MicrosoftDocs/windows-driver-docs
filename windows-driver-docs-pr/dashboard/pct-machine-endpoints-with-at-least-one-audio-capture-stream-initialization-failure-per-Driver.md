---
title: Percent of machine endpoints with at least one audio capture stream initialization failure per driver
description: This measure calculates the percentage of machine endpoints on which there was nonzero audio stream initialization unexpected failures
ms.topic: article
ms.date: 11/07/2022
---

# Percent of machine endpoints with at least one audio capture stream initialization failure per driver

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement Criteria**|Aggregation of machine endpoints|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=1% of machine endpoints have at least one capture audio stream initialization failure|
|**Measure ID**|27539331|

## Calculation

1.	Measure is accounting for failures at an endpoint level, that is, if there is a failure on a specific endpoint that the driver is targeting, it is counted as a failure.
2.	The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines’ endpoints that have at least one unexpected initialization failure**
3.	*Machine endpoint with initialization failure = Count(endpoints driver is targeting with at least 1 unexpected capture initialization failure)*
4.	*Total machine endpoints = Count(machine endpoints targeted by driver that attempted to initialize an audio capture stream)*

### Final calculation

*Percent of machine endpoints with at least one capture stream initialization failure = Machine endpoints targeted by driver with capture initialization failure / Total machine endpoints targeted by driver*
