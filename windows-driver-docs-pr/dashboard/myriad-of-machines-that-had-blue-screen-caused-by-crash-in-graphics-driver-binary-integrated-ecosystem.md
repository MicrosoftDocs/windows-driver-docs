---
title: Myriad of machines that had a stop error caused by an integrated graphics driver crash (ecosystem)
description: The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with integrated GPU that experienced a stop error caused by a crash in the graphics driver binary (Ecosystem)
ms.topic: article
ms.date: 09/03/2021
ms.localizationpriority: medium
---

# Myriad of machines that had a stop error caused by an integrated graphics driver crash (ecosystem)

## Description

During a user's session, crash in graphics driver binary may cause a stop error resulting in machine restart which can interrupt user's workflow. This measure evaluates myriad (out of 10,000) of machines with integrated GPUs having the driver, encountering a stop error due to a crash in graphics driver binary.

This is the ecosystem counterpart of [Myriad of machines that had a stop error caused by a graphics driver crash](./myriad-of-machines-that-had-blue-screen-caused-by-crash-in-graphics-driver-binary-integrated-standard.md) measure.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Ecosystem |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum population** | 20,000 machines |
| **Passing criteria** | <= 3/10,000 machines experience a stop error |
| **Measure ID** | 23253402 |

## Calculation

The measure aggregates telemetry from a 7-day sliding window into a myriad of distinct machines with integrated GPU that experienced a stop error due to a crash in the graphics driver binary.

1. Machines that stopped = count(machines having integrated GPU with the driver that experienced a stop error)
1. Total machines = count(machines having integrated GPU with the driver)
1. Ratio of stopped machines = machines that stopped / total machines

### Final calculation

Distinct device hits over population (DHoP) = ratio of stopped machines * 10,000

In above calculation, the result is normalized to 10,000 machines and the final result can be read as:

Distinct device hits over population (DHoP): distinct machines out of 10,000 machines hit a stop error due to a crash in the graphics driver binary
