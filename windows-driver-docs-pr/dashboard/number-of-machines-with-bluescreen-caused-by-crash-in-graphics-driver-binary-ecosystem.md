---
title: Number of machines with a blue screen caused by a crash in graphics driver binary
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of Distinct Machines that experienced a Bluescreen caused by a crash in the graphics driver binary
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Number of machines with a blue screen caused by a crash in graphics driver binary

## Description

During a user’s session, a crash in the graphics binary causes a blue screen, which restarts the machines and can interrupt a user’s workflow. This measure is evaluating how many machines with the driver are encountering blue screens due to a crash in the graphics binary.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|120,000 machines|
|**Passing criteria**|<=30/10,000 machines experience a blue screen|
|**Measure ID**|16507562|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced a blue screen caused by a crash in the graphics driver binary**.
2. *Machines that blue screened = count(machines with the driver that had a blue screen)*
3. *Total machines = count(machines with the flighted driver)*
4. *Ratio of blue screened machines = machines that blue screened / total machines*

### Final calculation

*Blue screen machine hits over population = ratio of blue screened machines * 10,000*

The result is normalized to 10,000 machines and the Final Calculation can be read as: *[Final Calculation] distinct machines out of 10,000 machines hit a blue screen*.