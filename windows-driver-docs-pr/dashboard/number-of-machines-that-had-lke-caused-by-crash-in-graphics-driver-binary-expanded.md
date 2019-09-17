---
title:  Number of machines that had an LKE caused by a crash in the graphics driver binary
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that experienced an LKE due to a crash in the graphics driver binary 
ms.topic: article
ms.date: 08/08/2019
ms.localizationpriority: medium
---

# Number of machines that had an LKE caused by a crash in the graphics driver binary

## Description

During a user’s session, a crash in the driver binary causes a live kernel event (LKE), which can restart the machine and can interrupt a user’s workflow. This measure is evaluating how many machines with the driver are encountering LKEs due to a crash in the graphics binary.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|10,000 machines|
|**Passing criteria**|<=130/10,000 machines experience an LKE event|
|**Measure ID**|20574653|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced an LKE due to a crash in the graphics driver binary, over the population**.
2. *Machines with a LKE = count(machines with the driver that had a LKE)*
3. *Total machines = count(machines with the driver)*
4. *Ratio of machines that had a LKE = Machines with a LKE / Total machines*

### Final calculation

5. *LKE machine hits over population = Ratio of machines that had a LKE * 10,000*
6. The result is normalized to 10,000 machines and the Final Calculation is read as:

   i. [LKE machine hits over population] distinct machines out of 10,000 machines encountered an LKE due to a crash in the graphics driver binary