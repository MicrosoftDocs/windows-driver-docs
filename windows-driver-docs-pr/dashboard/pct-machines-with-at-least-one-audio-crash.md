---
title: Percent of machines with at least one audio crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio crash in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 11/19/2022
---

# Percent of machines with at least one audio crash

## Description

See the "Audio user-mode reliability" section at [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Percent of machines|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=0.4 % of machines with at least one crash in AudioSrv<br><1% of machines with at least one crash in either AudioSrv or AudioDG|
|**Measure IDs**| 38373370 - both AudioSrv and AudioDG|

## Calculation

Every day:
1. Count the number of machines that hit a crash in AudioSrv or AudioDg
2. Count the number of machines which attempted to use audio


## Final Calculation

Percent of machines hitting a crash = *(number of machines hitting a crash) / (number of machines which attempted to use audio)*

The value of the measure at any time is the seven-day rolling average of this percentage.
