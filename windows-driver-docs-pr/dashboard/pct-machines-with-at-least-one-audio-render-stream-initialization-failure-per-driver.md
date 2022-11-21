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
|**Time period**|30 day sliding window|
|**Machine vs. Instance**|	Endpoint level on a machine (each machine can have more than one audio endpoint)|
|**Passing criteria**|<=4 % of devices have at least 1 audio steam initialization failure|
|**Measure ID**|27539296|

## Calculation

1. The measure aggregates telemetry from a 30-day sliding window into a **percentage of machines endpoints that have an audio render stream initialization failure**
2. *Audio render stream initialization failure = Count(audio endpoints with audio render stream init failure)*
3. Universal set of devices = *Count*(all device id's and endpoitns)
    *note ACI events are sampled at 1%, if a device is part of sampling, all of its endpoints are

### Final calculation

*Measure failure rate = *# of endpoitns with atleast *one audio render stream init failure / Total *# endpoints in universal set that have an audio render stream initialization 
