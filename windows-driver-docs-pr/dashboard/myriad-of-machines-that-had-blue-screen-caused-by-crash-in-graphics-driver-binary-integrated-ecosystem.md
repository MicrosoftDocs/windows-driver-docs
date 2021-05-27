---
title: Myriad of machines with integrated GPU that had a blue screen caused by a crash in the graphics driver binary (Ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with integrated GPU that experienced a bluescreen caused by a crash in the graphics driver binary (Ecosystem)
ms.topic: article
ms.date: 10/28/2019
ms.localizationpriority: medium
---

# Myriad of machines with integrated GPU that had a blue screen caused by a crash in the graphics driver binary (Ecosystem)

## Description

During a user’s session, crash in graphics driver binary may cause bluescreen resulting in machine restart which can interrupt user’s workflow. This measure evaluates myriad (out of 10,000) of machines with integrated GPUs having the driver, encountering bluescreen due to a crash in graphics driver binary. 

This is the ecosystem counterpart of [Myriad of machines with integrated GPU that had a blue screen caused by a crash in the graphics driver binary](./myriad-of-machines-that-had-blue-screen-caused-by-crash-in-graphics-driver-binary-integrated-standard.md)  measure.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|20,000 machines|
|**Passing criteria**|<= 3/10,000 machines experience a blue screen|
|**Measure ID**|23253402|

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines with integrated GPU that experienced a blue screen due to a crash in the graphics driver binary.**
1. *Machines that bluescreened = count(machines having integrated GPU with the driver that experienced a blue screen)*
2. *Total machines = count(machines having integrated GPU with the driver)*
3. *Ratio of bluescreened machines = Machines that bluescreened / Total machines*

### Final calculation

*Distinct device Hits over Population (DHoP) = Ratio of blue screened machines * 10,000*

In above calculation, the result is normalized to 10,000 machines and the final result can be read as:       
[Distinct device Hits over Population (DHoP)] distinct machines out of 10,000 machines hit a blue screen due to a crash in the graphics driver binary
