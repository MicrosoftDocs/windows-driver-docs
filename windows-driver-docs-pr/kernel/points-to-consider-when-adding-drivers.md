---
title: Points to Consider When Adding Drivers
description: Points to Consider When Adding Drivers
ms.assetid: bcbaa842-03b6-4311-9b93-1a4af165020b
keywords: ["WDM drivers WDK kernel , configurations", "WDM drivers WDK kernel , layered drivers", "layered drivers WDK kernel", "driver layers WDK WDM", "replacing drivers", "adding kernel-mode drivers"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Points to Consider When Adding Drivers





Keep the following points in mind when designing a kernel-mode driver:

-   The system-supplied SCSI and video port drivers cannot be replaced.

-   A replacement lowest-level driver must implement the same functionality as the driver it replaces. For example, a replacement keyboard or mouse port driver must use the system-defined interface between itself and a system-supplied class driver that it reuses, and vice versa.

-   A new intermediate driver, inserted between any pair of system-supplied drivers, must interoperate with those drivers so that the functionality of the upper and lower drivers is not reduced.

 

 




