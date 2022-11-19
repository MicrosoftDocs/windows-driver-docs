---
title: Percent of devices with at least 1 audio render stream initialization failure 
description: This measure calculates the percentage of devices with atleast one ACI render stream initialization failure
ms.topic: article
ms.date: 11/07/2022
---

# Percent of devices with at least 1 audio render stream initialization failure

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|30 day sliding window|
|**Minimum population**|NA|
|**Machine Vs Instance**|Percentage of Machine|
|**Passing criteria**|<=1.5 % of devices have at least 1 audio render stream initialization failure|
|**Measure ID**|39415262|

## Calculation

1. The measure aggregates telemtry from a 30-day sliding window into a percentage of Machines that had a render stream initialization failure.
2. *Render stream initilzation failures = Count(machines with render stream init failure*)
3. *Total machines that played audio = Count(machines that had a render audio stream init event*)

### Final calculation

*Measure failure rate* = # of machines with atleast *one Render Stream init failure / Total* # *machines with a stream init event*
