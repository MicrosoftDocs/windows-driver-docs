---
title: Percent of machines with at least one audio stream initialization failure
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have at least one unexpected initialization failure
ms.topic: article
ms.date: 11/18/2022
---

# Percent of machines with at least one audio stream initialization failure

## Description

See the "Audio stream initialization" section at [Audio measures](audio-measures.md)

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|50 machines|
|**Passing criteria**|<=8 % of machines with at least 1 audio steam initialization failure|
|**Measure ID**| *12111510 (Legacy*), 39415055|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have at least one unexpected initialization failure**
2. *Machines With nitialization failure = Count(machines with at least 1 unexpected initialization failure)*
3. *Total machines = Count(machines that attempted to initalizate an audio stream)*

### Final calculation

*Percent of machines with at least 1 stream initialization failure = Machines with initialization failure / Total machines*
