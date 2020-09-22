---
title: Other Policies
description: Other policies for publishing drivers
ms.topic: article
ms.date: 09/22/2020
ms.localizationpriority: medium
---

# Overview of Driver Policies
Driver Flighting and Gradual Rollout works to ensure that drivers being published are high quality and assists in limiting the chance a driver will negatively impact Windows customers.  To accomplish this, there aer a set of measures that are used to ensure quality. There are also policies that are put in place that ensures success in the ecosystem.

Some existing policies that lead to the driver submission being rejected include:
* Previous versions of Windows and Windows 10 can not both be targeted in the same submission.
* Some device class have specific CHID targeting requirements. Some device classes require CHID like Firmware and other classes forbid the use of CHID like Display. 
* OEMs can only target hardware IDs that target their own systems.

## Other Policies
* [Extension INF targeting evaluation rules defined](https://docs.microsoft.com/windows-hardware/drivers/dashboard/extension-inf-targeting-rules)

