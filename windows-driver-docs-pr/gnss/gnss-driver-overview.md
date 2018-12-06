---
title: GNSS driver overview
description: Use this guide to learn how to implement the DeviceIoControl APIs with the GNSS driver so that a HLOS like the GNSS adapter can access GNSS functionality.
ms.assetid: 1887097A-C495-4295-9904-B2964F46A81D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GNSS driver overview


Use the GNSS driver design guide to learn how to implement the **DeviceIoControl** APIs with the GNSS driver so that a high level operating system component (HLOS) like the GNSS adapter can access the desired GNSS functionality.

The GNSS functionality can be augmented by an IHV to provide positions at lower power cost or to provide better performance when needed.

The new GNSS drivers are fully owned and delivered by IHVs, with no Microsoft-owned code running in kernel mode .

**Note**  IHVs must not add filter drivers to the GNSS/Location stack. Filter drivers are hard to debug and maintain so in general they are not recommended. In addition to this, in the future, Microsoft may need to add filter drivers in the GNSS device stack for extending functionality and having additional filter drivers from the IHVs will make the architecture more complex unnecessarily.

 

The driver follows the generic UMDF 2.0 model (User Mode Driver Framework) for function drivers. KMDF (Kernel Mode Driver Framework) drivers could be used but they are strongly discouraged as they bring higher risk of instability to the platform, they are harder to debug, and they cannot make direct use of user mode OS components.
This design guide assumes basic familiarity with UMDF 2.0, Windows kernel-mode programming, kernel I/O management, power management, and the PnP device stack.

## Related topics
[GNSS driver requirements](gnss-driver-requirements.md)  
[GNSS driver architecture](gnss-driver-architecture.md)  



