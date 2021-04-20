---
title: Number of machines that had a blue screen caused by a crash in the graphics kernel
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that experienced a blue screen caused crash in the graphics kernel
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Number of machines that had a blue screen caused by a crash in the graphics kernel

## Description

During a user’s session, a crash in the display kernel causes a blue screen, which restarts the machines and can interrupt a user’s workflow. This measure is evaluating how many machines with the driver are encountering a crash in the graphics kernel.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|5,000 machines|
|**Passing criteria**|<=10/10,000 machines have a crash in the display kernel|
|**Measure ID**|7533022 or 26590240|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced a blue screen caused crash in the graphics kernel, over the population**.
2. *Machines that blue screened = count(machines with the driver that had a blue screen)*
3. *Total machines = count(machines with the driver)*
4. *Ratio of blue screened machines = Machines that blue screened / Total machines*

### Final calculation

5. *Blue screen machine hits over population = Ratio of blue screened machines * 10,000*
6. The result is normalized to 10,000 machines and the final calculation can be read as:

   i. [Blue screen machine hits over population] distinct machines out of 10,000 machines hit a blue screen due to a crash in the graphics driver binary