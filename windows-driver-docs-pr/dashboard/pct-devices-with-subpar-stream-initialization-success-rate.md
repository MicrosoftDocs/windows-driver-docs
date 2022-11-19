---
title: Percent of devices with sub-par stream initialization success rate
description: This measure calculates the percentage of devices with sub-par stream initialization success rate
ms.topic: article
ms.date: 11/18/2022
---

# Percent of devices with sub-par stream initialization success rate

## Description

See "Audio user-mode reliability" on [Audio measures](audio-measures.md)

These measures determine an audio stream initialization success rate for each machine and calculates a percentage of machines with less than 90% stream initialization rate. When an application is unable to initialize an audio stream, the user will not have access to the application’s audio experience.

Some machines have multiple audio drivers on them. Some audio drivers work together to power the same audio hardware; some audio drivers work separately to power different audio hardware on the same machine.

Measure 27657901 looks at the audio stream initialization success rate for audio hardware on the machine endpoints where the driver flight landed.


## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement Criteria**|	Aggregation of machine endpoints|
|**Minimum Population**|1000 machines
|**Passing criteria**|<=5 % of machine endpoints with at least 1 capture audio stream initialization failure|
|**Measure ID**|27657901|

## Calculation

1.	Measure is accounting for failures at an endpoint level, that is, if there is a failure on a specific endpoint that the driver is targeting, it is counted as a failure.
2.	The measure aggregates telemetry from a 7-day sliding window into a percentage of machine endpoints that have a subpar initialization rate.
3.	For each machine, calculate the:
    a.	Endpoint’s initialization success rate = count (Failed Initializations) / count (total attempted initializations)
    b.	Failing endpoint = endpoint’s initialization success rate < 90%
4.	Machine endpoints with subpar initialization = count (failing machine endpoints)
5.	Total machine endpoints = count (all machine endpoints targeted by driver that attempted initialization)


### Final calculation

*Percent of machine endpoints with subpar initialization rates = Machine endpoints targeted by driver with subpar initialization / Total machine endpoints targeted by driver*
