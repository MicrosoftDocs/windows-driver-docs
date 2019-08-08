---
title: Percent of machines that had a blue screen caused by a crash in the graphics driver binary
description: The measure aggregates telemetry from a 14-day sliding window into a percentage of machines that haven’t experienced a kernel mode crash 
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines that had a blue screen caused by a crash in the graphics driver binary

## Description

During a user’s session, a crash in the graphics driver binary causes a blue screen, which restarts the machines and can interrupt a user’s workflow. This measure is evaluating how many machines with the driver are encountering blue screens due to a crash in the graphics driver binary.

There are two versions of this measure, one with a standard audience and the other with an expanded audience. 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard, Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|<= 30 / 10,000 machines experience a blue screen|
|**Passing criteria**|5,000|
|**Measure ID**|7802933, 20574588|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced a blue screen caused by a crash in the graphics driver binary**
2. *Machines that blue screened = count(machines with the driver that had a blue screen)*
3. *Total machines = count(machines with the flighted driver)*
4. *Ratio of blue screened machines = machines that blue screened / total machines*

### Final calculation

5.  *Blue screen machine hits over population = ratio of blue screened machines * 10,000*
6.  The result is normalized to 10,000 machines and the final calculation can be read as:

    i. [Final calculation] distinct machines out of 10,000 machines hit a blue screen
