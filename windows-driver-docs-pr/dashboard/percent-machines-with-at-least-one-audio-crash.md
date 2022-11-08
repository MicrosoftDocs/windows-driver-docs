---
title: Percent of machines with at least one audio crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio crash in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 05/20/2019
---

# Percent of machines with at least one audio crash

## Description

See the "Audio user-mode reliability" section at [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|Daily, averaged over 7 days|
|**Measurement criteria**|Percent of machines|
|**Minimum population**|Dynamic, uses confidence intervals|
|**Passing criteria**|<=0.4 % of machines with at least 1 crash in AudioSrv<br/><1% of machines with at least 1 crash in either AudioSrv or AudioDG|
|**Measure IDs**|12518948 - AudioSrv only<br/>*23032999 (Legacy), 38373370, 29568277 - both AudioSrv and AudioDG|

## Calculation

Every day:
1. Count the number of machines that hit a crash in AudioSrv or AudioDg
1. Count the number of machines which attempted to use audio
1. Percent of machines hitting a crash = (number of machines hitting a crash) / (number of machines which attempted to use audio)

The value of the measure at any time is the seven-day rolling average of this percentage.
