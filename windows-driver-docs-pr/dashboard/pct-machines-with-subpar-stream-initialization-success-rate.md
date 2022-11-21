---
title: Percent of machines with subpar stream initialization success rate
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have a subpar initialization rate
ms.topic: article
ms.date: 11/19/2021
---

# Percent of Machines with Subpar Stream Initialization Success Rate

## Description

See the "Audio stream initialization" section at [Audio measures](audio-measures.md)

These measures determine an *audio stream initialization success rate* for each machine and calculates a percentage of machines with less than 90% stream initialization rate. When an application is unable to initialize an audio stream, the user will not have access to the application’s audio experience.

Some machines have multiple audio drivers on them. Some audio drivers work together to power the same audio hardware; some audio drivers work separately to power different audio hardware on the same machine.

Measure 11458866 looks at the audio stream initialization success rate for *all* audio hardware on the machine where the driver flight landed.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Audio measures capture data from any machine that is playing audio on Windows|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|1000 machines|
|**Passing criteria**|<=0.5% of machines with an initialization success rate below 90%|
|**Measure IDs**|11458866|

## Calculation

1.	The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have a subpar initialization rate.
2.	For each machine, calculate the:
    a.	Machine initialization success rate = count (Failed Initializations) / count (total attempted initializations)
    b.	Failing machine = machines initialization success rate < 90%
3.	Machines  with subpar initialization = count (failing machines)
4.	Total machines = count (all machines that attempted initialization)

### Final calculation

*Percent of machines with subpar initialization rates = Machines with subpar initialization / Total machines*
