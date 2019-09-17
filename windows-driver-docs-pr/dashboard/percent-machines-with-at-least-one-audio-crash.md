---
title: Percent of machines with at least one audio crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio crash in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of machines with at least one audio crash

## Description

This measure monitors two services - *Windows Audio Service (AudioSrv.dll)* and the *Audio Device Graph (AudioDG.exe)* - to examine if a crash occurred in either service. If either service crashes, the user’s machine can’t play any audio and the user must wait till the service recovers to reinitialize any audio streams.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 days|
|**Measurement criteria**|Percent of machines|
|**Minimum population**|50 machines|
|**Passing criteria**|<=0.4 % of machines with at least 1 crash in either audio service|
|**Measure ID**|12518948|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have at least one audio crash in AudioSrv.dll or AudioDG.exe**
2. *Crashing Machines = Count (Machines with at least one crash in either AudioSrv.dll or AudioDG.exe)*
3. *Total Machines=Count (Machines that successfully initialzed at least 1 audio stream)*

### Final calculation

*Percent of devices with at least one audio crash = Crashing Machines / Total Machines*