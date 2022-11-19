---
title: Percent of devices with at least one crash
description: This measure calculates the percentage of devices with at least crash in AudioSrv
ms.topic: article
ms.date: 11/18/2022
---

# Percent of devices with sub-par stream initialization success rate

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement Criteria**|	Aggregation of machine endpoints|
|**Minimum Population**|1000 machines|
|**Passing criteria**|<=0.3% of machine endpoints with at least 1 crash in AudioSrv or AudioDg|
|**Measure ID**|29568277|

## Calculation

1.	Count the number of machine endpoints targeted by driver that hit a crash in AudioSrv or AudioDg
2.	Count the number of machine endpoints targeted by driver which attempted to use audio
3.	Percent of machine endpoints targeted by driver hitting a crash = (number of machine endpoints targeted by driver hitting a crash) / (number of machines targeted by driver which attempted to use audio)



### Final calculation

*The value of the measure at any time is the seven-day rolling average of this percentage.*
