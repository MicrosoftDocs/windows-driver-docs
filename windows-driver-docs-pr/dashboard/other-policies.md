---
title: Other Policies
description: Other policies for publishing drivers
ms.topic: article
ms.date: 09/22/2020
ms.localizationpriority: medium
---

# Overview of Driver Policies
Driver Flighting and Gradual Rollout works to ensure that drivers being published are high quality and assists in limiting the chance a driver will negatively impact Windows customers.  To accomplish this, there are a set of measures that are used to ensure quality. There are also policies that are put in place that ensure success in the ecosystem.

Some existing policies that lead to the driver submission being rejected include:
* Drivers targeting previous versions of Windows cannot be included in the same submission with drivers for Windows 10.
* Some device class have specific CHID targeting requirements. For example Firmware and Display classes forbid the use of CHID.
* OEMs can only target hardware IDs that target their own systems.

## Other Policies
* [Extension INF targeting evaluation rules defined](./extension-inf-targeting-rules.md)
* [Driver Release Cadence](./driver-release-cadence.md)