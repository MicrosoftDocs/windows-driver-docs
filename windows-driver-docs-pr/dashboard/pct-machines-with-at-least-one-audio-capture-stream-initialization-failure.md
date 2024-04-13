---
title: Percent of machines with at least one audio capture stream initialization failure 
description: This measure tracks the percentage of machines  with at least one ACI capture stream initialization failure
ms.topic: article
ms.date: 11/07/2022
---

# Percent of machines with at least one audio capture stream initialization failure

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|30 day sliding window|
|**Minimum population**|1000 machines|
|**Machine Vs Instance**|Percentage of Machine|
|**Passing criteria**|<=1 % of machines have at least 1 audio capture stream initialization failure|
|**Measure ID**|39415321|

## Calculation

1. The measure aggregates telemtry from a 30-day sliding window into a percentage of Machines that had a capture stream initialization failure.
2. *Capture stream initilzation failures = Count(machines with capture stream init failure*)
3. *Total machines that played audio = Count(machines that had a capture audio stream init event*)

### Final calculation

*Measure failure rate* = # of machines with atleast *one capture init failure / Total* # *machines with atleast one capture stream init event*
