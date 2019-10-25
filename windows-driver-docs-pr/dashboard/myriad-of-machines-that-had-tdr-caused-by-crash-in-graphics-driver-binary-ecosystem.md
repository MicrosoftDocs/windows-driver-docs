---
title: Myriad of machines that had a TDR caused by a crash in the graphics driver binary
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that experienced a TDR caused by a crash in the graphics driver binary
ms.topic: article
ms.date: 10/28/2019
ms.localizationpriority: medium
---

# Myriad of machines that had a TDR caused by a crash in the graphics driver binary

## Description

During a user’s session, crash in the graphics driver binary may cause the machine’s screen to hang or appear completely frozen. A Timeout Detection and Recovery (TDR) event attempts to detect these hangs and dynamically recover to unfreeze the display. Users that have encountered a TDR will be unable to use their computer until the TDR is successful, which causes the screen to flicker. 

This is the ecosystem counterpart of [Myriad of machines that had a TDR caused by a crash in the graphics driver binary](https://docs.microsoft.com/en-us/windows-hardware/drivers/dashboard/myriad-of-machines-that-had-tdr-caused-by-crash-in-graphics-driver-binary-standard)  measure.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|20,000 machines|
|**Passing criteria**|<= 130/10,000 machines experience a TDR|
|**Measure ID**|20350972|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced a TDR caused by a crash in the graphics driver binary**.
1. *Machines that experieced a TDR = count(machines with the driver that experienced a TDR)*
2. *Total machines = count(machines with the driver)*
3. *Ratio of machines that experienced a TDR = Machines that experienced a TDR / Total machines*

### Final calculation

*Distinct device Hits over Population (DHoP) = Ratio of machines that experienced a TDR * 10,000*

In above calculation, the result is normalized to 10,000 machines and the final result can be read as:  
[Distinct device Hits over Population (DHoP)] distinct machines out of 10,000 machines experienced a TDR due to a crash in the graphics driver binary