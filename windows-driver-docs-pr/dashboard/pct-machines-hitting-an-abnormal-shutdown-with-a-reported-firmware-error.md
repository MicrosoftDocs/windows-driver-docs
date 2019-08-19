---
title: Percent of machines hitting an abnormal shutdown with a reported firmware error
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that attempted to install the firmware, then experienced an ABS-related firmware error
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines hitting an abnormal shutdown with a reported firmware error

## Description

During the firmware installation process, a machine reboots to apply the firmware; a bug in the package can cause a machine to spontaneously reset without the user initiating the power down sequence – this is an abnormal shutdown (ABS). An ABS can interrupt the user workflow and cause data loss. This measure is calculating how many machines attempted to install the firmware and had an ABS attributed to firmware.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|7 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<= 20% of machines encounter a firmware related ABS|
|**Measure ID**|16745838|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that attempted to install the firmware, then experienced an ABS-related firmware error**.
2. *Machines that hit a firmware-related ABS = count(machines that installed the firmware,rebooted,then encountered an ABS)*
3. *Total machines = count(machines that downloaded the firmware and started the install process)*

### Final calculation

*Percent of machines with a firwamre-related ABS = machines that hit a firmware-related ABS / total machines*
