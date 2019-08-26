---
title: Percent of machines with subpar stream initialization success rate
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that have a subpar initialization rate
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of Machines with Subpar Stream Initialization Success Rate

## Description

This measure determines an *initialization success rate* for each machine and calculates a percentage of machines with less than 90% stream initialization rate. When a device is unable to initialize an audio stream, the user will not have access to the application’s audio experience. 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 days|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|50 machines|
|**Passing criteria**|<=1 % of machines an Initialization Success Rate below 90% |
|**Measure ID**|11458866|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that have a subpar initialization rate**.
2. *For each machine, calculate the:*

   a. *Machine's initialization success rate = count (Failed Initializations) / count (total attempted initializations)*

   b. *Failing machine = machine's initialization success rate < 90%*

3. *Machines with subpar initialization = count (failing machines)*
4. *Total machines = count (all machines that attempted initialization)*

### Final calculation

*Percent of machines with supbar initialization rates = Machines with subpar initialization / Total machines*
