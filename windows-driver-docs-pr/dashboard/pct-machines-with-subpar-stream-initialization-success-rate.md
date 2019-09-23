---
title: Percent of machines with subpar stream initialization success rate
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have a subpar initialization rate
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Percent of Machines with Subpar Stream Initialization Success Rate

## Description

See the "Audio stream initialization" section at [Audio measures](audio-measures.md)

These measures determine an *audio stream initialization success rate* for each machine and calculates a percentage of machines with less than 90% stream initialization rate. When an application is unable to initialize an audio stream, the user will not have access to the application’s audio experience.

Some machines have multiple audio drivers on them. Some audio drivers work together to power the same audio hardware; some audio drivers work separately to power different audio hardware on the same machine.

Measure 11458866 looks at the audio stream initialization success rate for *all* audio hardware on the machine where the driver flight landed.

Measure 21271062 looks at the audio stream initialization success rate for audio hardware on the flighted machine where there is a KSCATEGORY_AUDIO interface exposed by the driver in flight.
* If this is the kind of audio driver which exposes a KSCATEGORY_AUDIO interface (either directly or via an intermediate DDI such as WaveRT) then it will be specific to the driver being flighted, and will filter out failures from other, unrelated audio drivers that happen to be in use from the same system.
* If this is the kind of audio driver which does not expose a KSCATEGORY_AUDIO interface (for example, a bus driver, or an Audio Processing Object plugin for audiodg.exe) then this measure will return no data and will not be used in release or throttling decisions.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|Daily, averaged over 7 days|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|Dynamic, uses confidence intervals|
|**Passing criteria**|<=1 % of machines an Initialization Success Rate below 90% |
|**Measure IDs**|11458866 - all audio hardware on the flighted machines<br/>21271062 - only audio hardware associated with a KSCATEGORY_AUDIO interface powered by the flighted driver|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have a subpar initialization rate**.
1. *For each machine, calculate the:*

   a. *Machine's initialization success rate = count (Failed Initializations) / count (total attempted initializations)*

   b. *Failing machine = machine's initialization success rate < 90%*

1. *Machines with subpar initialization = count (failing machines)*
1. *Total machines = count (all machines that attempted initialization)*

### Final calculation

*Percent of machines with subpar initialization rates = Machines with subpar initialization / Total machines*
