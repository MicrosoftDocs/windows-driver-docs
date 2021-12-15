---
title: Percent of machines with subpar stream initialization success rate
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have a subpar initialization rate
ms.topic: article
ms.date: 05/20/2019
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
|**Audience**|Standard|
|**Time period**|Daily, averaged over 7 days|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|Dynamic, uses confidence intervals|
|**Passing criteria**|<=1 % of machines an Initialization Success Rate below 90% |
|**Measure IDs**|11458866 - all audio hardware on the flighted machines|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have a subpar initialization rate**.
1. *For each machine, calculate the:*

   a. *Machine's initialization success rate = count (Failed Initializations) / count (total attempted initializations)*

   b. *Failing machine = machine's initialization success rate < 90%*

1. *Machines with subpar initialization = count (failing machines)*
1. *Total machines = count (all machines that attempted initialization)*

### Final calculation

*Percent of machines with subpar initialization rates = Machines with subpar initialization / Total machines*
