---
title: Percent of machines with at least one audio crash
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one audio crash in AudioSrv.dll or AudioDG.exe
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of machines with at least one audio crash

## Description

These measures monitor two process:
* The *Windows Audio* service, which is the instance of svchost.exe hosting AudioSrv.dll (AudioSrv)
* AudioSrv's helper process *Audio Device Graph Isolation*, which is AudioDG.exe (AudioDG)

If either process crashes, the user’s machine can’t play any audio and the user must wait till the service recovers to reinitialize any audio streams.

Audio drivers commonly include custom audio processing in Audio Processing Objects (APOs). These APOs are .dlls which are loaded into the AudioDG helper process. Note that if an APO .dll crashes it will be reflected in measure 23032999 but not measure 12518948.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|Daily, averaged over 7 days|
|**Measurement criteria**|Percent of machines|
|**Minimum population**|Dynamic, uses confidence intervals|
|**Passing criteria**|<=0.4 % of machines with at least 1 crash in AudioSrv<br/><1% of machines with at least 1 crash in either AudioSrv or AudioDG|
|**Measure IDs**|12518948 - AudioSrv only<br/>23032999 - both AudioSrv and AudioDG|

## Calculation

Every day:
1. Count the number of machines that hit a crash in AudioSrv or AudioDg
1. Count the number of machines which attempted to use audio
1. Percent of machines hitting a crash = (number of machines hitting a crash) / (number of machines which attempted to use audio)

The value of the measure at any time is the seven-day rolling average of this percentage.