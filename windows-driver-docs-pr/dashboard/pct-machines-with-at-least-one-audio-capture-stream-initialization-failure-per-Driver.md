---
title: Percent of devices with at least 1 audio capture stream initialization failure per driver
description: This measure calculates the percentage of devices on which there was nonzero audio stream initialization unexpected failures
ms.topic: article
ms.date: 11/07/2022
---

# Percent of devices with at least 1 audio capture stream initialization failure per driver

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|30 day sliding window|
|**Minimum population**|NA machines|
|**Passing criteria**|<=4 % of machines have at least 1 audio stream initialization capture failure|
|**Measure ID**|27539331|

## Calculation

1. The measure aggregates telemtry from a 30-day sliding window into a percentage of Machine's endpoints that had an audio caputre stream initialization failure.
2. *Audio render stream initilzation = Count*(audio endpoints with audio capture *stream init failure*)
3. Universal set of devices = *Count*(all device id's and endpoints)
    *note: ACI events are sampled at 1%, if a device is part of sampling, all of it's endpoints are.

### Final calculation

*Measure failure rate* = # of endpoints with atleast *one audio render stream init failure / Total* # endpoints in universal set that have an audio capture stream initialization
