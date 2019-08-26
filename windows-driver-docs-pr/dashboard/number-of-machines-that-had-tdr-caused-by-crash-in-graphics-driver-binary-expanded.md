---
title: Number of machines that had a TDR caused by a crash in the graphics driver binary
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines that experienced a TDR caused by a crash in the graphics driver binary
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Number of machines that had a TDR caused by a crash in the graphics driver binary

## Description

During a user’s session, a crash in the graphics driver binary can cause the machine’s screen to hang or appear completely frozen. A Timeout Detection and Recovery (TDR) event attempts to detect these hangs and dynamically recover to unfreeze the display. Users that have encountered a TDR will be unable to use their computer until the TDR is successful, which causes the screen to flicker. 

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Expanded|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|10,000|
|**Passing criteria**|<= 130/10,000 machines experience a TDR|
|**Measure ID**|20574707|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **myriad** of **distinct machines that experienced a TDR caused by a crash in the graphics driver binary, over the population**.
2. *Machines with a TDR = count(machines with the driver that had a TDR)*
3. *Total machines = count(machines with the driver)*
4. *Ratio of machines with a TDR = Machines with a TDR / Total machines*

### Final calculation

5. *Percent of machines with TDR hits = Ratio of machines with TDR * 10,000*
6. The result is normalized to 10,000 machines and the final calculation can be read as:  

   i. [Percent of machines with TDR hits] distinct machines out of 10,000 machines hit a bluescreen due to a crash in the graphics driver binary