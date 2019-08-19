---
title: Percent of machines with display issues when resume from low power state
description: The measure aggregates telemetry from a 7-day sliding window into a percent of machines that encountered display issues when resuming from a low power state
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines with display issues when resume from low power state

## Description

When a machine is booting from a low power state, an error in the graphics component can cause display issues that impact the users’ experience. This measure is calculating the percent of machines that experienced display issues when resuming in a low power state. For a list of display issues, see the [Appendix](measure-appendix.md#display-issues).

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Ecosystem|
|**Time period**|7-day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines that were in a low power state|
|**Passing criteria**|<= 0.8% of machines in low power states encounter display issues|
|**Measure ID**|19920755|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percent of machines that encountered display issues when resuming from a low power state.**
2. *Number of machines with display issues = count(machines that experienced display issues when resuming from a low power state)*
3. *Total machines = count(machines that performed a low to high power state transition during flight)*

### Final calculation

Percent of machines that experienced display issues when resuming from low power = number of machines with display issues / total machines
