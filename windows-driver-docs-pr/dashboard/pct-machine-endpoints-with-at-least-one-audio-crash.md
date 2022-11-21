---
title: Percent of machine endpoints with at least one audio crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machine endpoints that have at least one audio crash in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 11/19/2022
---

# Percent of machine endpoints with at least one audio crash

## Description

See the "Audio user-mode reliability" section at [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machine endpoints|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=0.3% of machine endpoints with at least one crash in AudioSrv or AudioDG|
|**Measure IDs**|29568277|

## Calculation

Every day:
1.	Measure is accounting for failures at an endpoint level, that is, if there is a failure on a specific endpoint that the driver is targeting, it is counted as a failure.
2. Count the number of machine endpoints targeted by driver that hit a crash in AudioSrv or AudioDg
3. Count the number of machines which attempted to use audio

## Final Calculation

Percent of machine endpoints targeted by a driver hitting a crash = *(number of machine endpoints targeted by a driver hitting a crash) / (number of machine endpoints targeted by a driver which attempted to use audio)

The value of the measure at any time is the seven-day rolling average of this percentage.
