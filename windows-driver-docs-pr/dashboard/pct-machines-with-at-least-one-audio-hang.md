---
title: Percent of machines with at least one audio hang
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio hang in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 11/19/2022
---

# Percent of machines with at least one audio hang

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 days|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=0.5 % of machines with at least 1 hang in either audio service|
|**Measure ID**|*11458540 (Legacy)*, 38880837|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have at least one audio hang in AudioSrv.dll or AudioDG.exe**.
2. *Hanging machines = count (machines with at least 1 hang in AudioSrv.dll or AudioDG.exe)*
3. *Total machines = count (machines that successfully initialzed at least one audio stream)*

### Final calculation

*Percent of machines with at least one audio hang = Hanging machines / Total machines*
