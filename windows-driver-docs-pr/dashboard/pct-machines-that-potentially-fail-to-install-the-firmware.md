---
title: Percent of machines that potentially fail to install the firmware
description: The measure aggregates telemetry from a 7-day sliding window into a percentage of machines where the firmware is downloaded, the machine reboots, but without a successful install
ms.topic: article
ms.date: 05/20/2019
ms.author: paslote
author: parkeratmicrosoft
ms.localizationpriority: medium
---

# Percent of machines that potentially fail to install the firmware

## Description

After downloading new firmware, a machine gracefully reboots to install the firmware, prior to the OS booting. This measure is calculating the percent of machines that received the firmware, rebooted, but potentially failed to install it.

## Measure attributes

|Attribute|Value|
|----|----|
|**Audience**|Standard|
|**Time period**|14 day sliding window|
|**Measurement criteria**|Aggregation of machines|
|**Minimum population**|100 machines|
|**Passing criteria**|<=10% of machines successfully install and apply firmware after reboot|
|**Measure ID**|16745886|

## Calculation

1. The measure aggregates telemetry from a 7-day sliding window into a **percentage of machines where the firmware is downloaded, the machine reboots, but without a successful install**.

    a. A machine can attempt to install firmware 3 times before the measure counts it as a failure
2. *Machines without firmware install = count(machines that download the firmware,reboot, and encounter a PNP Code 10 error)*
3. *Total machines = count(all machines that downloaded the firmware)*

### Final calculation

*Percent of machines that failed to install firmware = machines without firmware install / total machines*
