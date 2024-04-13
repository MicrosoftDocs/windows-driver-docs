---
title: Myriad of machines with integrated GPU that had a TDR caused by a graphics driver crash
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of machines with integrated GPU that had a TDR caused by a crash in the graphics driver 
ms.topic: article
ms.date: 09/02/2021
---

# Myriad of machines with integrated GPU that had a TDR caused by a graphics driver crash

## Description

During a user's session, crash in the graphics driver binary may cause the machine's screen to hang or appear completely frozen. A Timeout Detection and Recovery (TDR) event attempts to detect these hangs and dynamically recover to unfreeze the display. Users that have encountered a TDR will be unable to use their computer until the TDR is successful, which causes the screen to flicker. This measure evaluates myriad (out of 10,000) of machines with integrated GPUs having the driver, encountering TDR due to a crash in graphics driver binary.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum instances**|20,000 machines|
|**Passing criteria**|<= 60/10,000 of machines encountering TDR|
|**Measure ID**|26647961|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with integrated GPU that experienced a TDR caused by a crash in the graphics driver binary.

Machines that experienced a TDR = Count(machines having integrated GPU with the driver that experienced a TDR)

Total machines = Count (machines with integrated GPU having the driver)

Ratio of machines that experienced TDR = Machines that experienced a TDR/ Total machines

### Final calculation

Distinct device Hits over Population (DHoP) = Ratio of machines that experienced a TDR * 10,000

In above calculation, the result is normalized to 10,000 machines and the final result can be read as:
[Distinct device Hits over Population (DHoP)] distinct machines out of 10,000 machines with integrated GPU experienced a TDR due to a crash in the graphics driver binary
