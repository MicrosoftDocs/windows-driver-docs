---
title: Percent of machines that successfully installed firmware within the last 14 days and rebooted
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines where firmware is installed without PNP errors and is successfully applied after a reboot
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines that successfully installed firmware within the last 14 days and rebooted

## Description

During the firmware installation process, the package must be delivered, and the machine must reboot before being able to apply the updated firmware. If a machine is unable to successfully apply the firmware, the user will have to use their machine with a previous version of the firmware.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|14 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|>= 90% of machines successfully install firmware after a reboot|
|**Measure ID**|15421173|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines where firmware is installed without PNP errors and is successfully applied after a reboot**.
2. *Machines with successful firmware install = count(machines that installed firmware without PNP errors and applied after a reboot)*
3. *Total machines = count(all machines that attempted to install firmware)*

### Final calculation

*Percent of successful firmware installs = machines with successful firmware install / total machines*
