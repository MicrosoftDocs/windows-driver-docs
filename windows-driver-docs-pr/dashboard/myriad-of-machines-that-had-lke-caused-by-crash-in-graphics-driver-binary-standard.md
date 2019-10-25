---
title:  Myriad of machines that had an LKE caused by a crash in the graphics driver binary
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that experienced an LKE due to a crash in the graphics driver binary 
ms.topic: article
ms.date: 10/28/2019
ms.localizationpriority: medium
---

# Myriad of machines that had an LKE caused by a crash in the graphics driver binary

## Description

During a user’s session, crash in the graphics driver binary may cause a live kernel event (LKE), which can restart the machine and can interrupt a user’s workflow. This measure is evaluating how many machines with the driver are encountering LKEs due to a crash in the graphics driver binary.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|10,000 machines|
|**Passing criteria**|<=130/10,000 machines experience an LKE event|
|**Measure ID**|20574653|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced an LKE due to a crash in the graphics driver binary**.
1. *Machines that experienced an LKE = count(machines with the driver that experienced an LKE)*
2. *Total machines = count(machines with the driver)*
3. *Ratio of machines that experienced an LKE = Machines that experienced an LKE / Total machines*

### Final calculation

*Distinct device Hits over Population (DHoP) = Ratio of machines that experienced an LKE * 10,000*
    
In above calculation, the result is normalized to 10,000 machines and the final result can be read as:  
[Distinct device Hits over Population (DHoP)] distinct machines out of 10,000 machines experienced an LKE due to a crash in the graphics driver binary