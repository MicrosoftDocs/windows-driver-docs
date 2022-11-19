---
title: Percent of machines with at least one audio hang
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio hang in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 05/20/2019
---

# Percent of machines with at least one audio hang

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machine endpoints|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=0.5 % of devices have at least 1 audio crash in AudioSrv or AudioDg|
|**Measure ID**|*11458540 (Legacy)*, 29745823|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have at least one audio hang in AudioSrv.dll or AudioDG.exe**.
2. *Hanging machines = count (machines with at least 1 hang in AudioSrv.dll or AudioDG.exe)*
3.  Percent of machine endpoints targeted by driver hitting a hang = *(number of machine endpoints targeted by driver hitting a hang) / (number of machines targeted by driver which attempted to use audio)*

### Final calculation

*Percent of machines with at least one audio hang = Hanging machines / Total machines*
