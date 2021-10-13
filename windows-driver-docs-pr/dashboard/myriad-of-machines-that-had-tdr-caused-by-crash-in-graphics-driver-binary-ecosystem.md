---
title: Myriad of machines that had a TDR caused by a graphics driver crash (ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with discrete GPU that experienced a TDR caused by a crash in the graphics driver binary (Ecosystem)
ms.topic: article
ms.date: 09/03/2021
ms.localizationpriority: medium
---

# Myriad of machines that had a TDR caused by a graphics driver crash (ecosystem)

## Description

During a user's session, a crash in the graphics driver binary may cause the machine's screen to hang or appear completely frozen. A timeout detection and recovery (TDR) event attempts to detect these hangs and dynamically recover to unfreeze the display. Users that have encountered a TDR will be unable to use their computer until the TDR is successful, which causes the screen to flicker. This measure evaluates myriad (out of 10,000) of machines with discrete GPUs having the driver, encountering TDR due to a crash in graphics driver binary.

This is the ecosystem counterpart of [Myriad of machines that had a TDR caused by a graphics driver crash](./myriad-of-machines-that-had-tdr-caused-by-crash-in-graphics-driver-binary-standard.md) measure.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum population** | 20,000 machines |
| **Passing criteria** | <= 65/10,000 machines experience a TDR |
| **Measure ID** | 20350972 |

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with discrete GPU that experienced a TDR caused by a crash in the graphics driver binary.

1. Machines that experienced a TDR = count(machines having discrete GPU with the driver that experienced a TDR)
1. Total machines = count(machines with discrete GPU having the driver)
1. Ratio of machines that experienced a TDR = machines that experienced a TDR / total machines

### Final calculation

Distinct device hits over population (DHoP) = ratio of machines that experienced a TDR * 10,000

In above calculation, the result is normalized to 10,000 machines and the final result can be read as:

Distinct device hits over population (DHoP): distinct machines out of 10,000 machines with discrete GPU experienced a TDR due to a crash in the graphics driver binary
