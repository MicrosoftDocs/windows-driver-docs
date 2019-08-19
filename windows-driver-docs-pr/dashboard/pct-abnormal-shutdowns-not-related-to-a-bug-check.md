---
title: Percent of abnormal shutdowns not related to a bug-check
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines that attempted to install the firmware, then experienced any ABS not related to a bug-check
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of abnormal shutdowns not related to a bug-check

## Description

During the firmware installation process, a machine reboots to apply the firmware; a bug in the package can cause a machine to spontaneously reset without the user initiating the power down sequence – this is an abnormal shutdown (ABS). An ABS can interrupt the user workflow and cause data loss. This measure calculates how many machines attempted to install the firmware and had an ABS not attributed to firmware like a blue screen and a user holding down the power button.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|14 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<= 10% of machines experience an ABS that is not a bug check|
|**Measure ID**|16745758|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines that attempted to install the firmware, then experienced any ABS not related to a bug-check**.
2. *Machines that hit an ABS = count(machines that installed firmware,rebooted,then encountered an ABS that was not a bug check)*
3. *Total machines = count(machines that downloaded the firmware and started the install process)*

### Final calculation

*Percent of machines with an ABS that isn't related to a bug check =  machines that hit an ABS / total machines*
