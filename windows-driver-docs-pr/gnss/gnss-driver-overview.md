---
title: Global Navigation Satellite System (GNSS) Driver Overview
description: Use this guide to learn how to implement the DeviceIoControl APIs with the Global Navigation Satellite System (GNSS) driver so that a HLOS like the GNSS adapter can access GNSS functionality.
ms.date: 03/21/2023
---

# Global Navigation Satellite System (GNSS) driver overview

Use the Global Navigation Satellite System (GNSS) driver design guide to learn how to implement the **DeviceIoControl** APIs with the GNSS driver so that a high level operating system component (HLOS) like the GNSS adapter can access the desired GNSS functionality.

The GNSS functionality can be augmented by an IHV to provide positions at lower power cost or to provide better performance when needed.

The new GNSS drivers are fully owned and delivered by IHVs, with no Microsoft-owned code running in kernel mode.

IHVs must not add filter drivers to the GNSS/Location stack. Filter drivers are hard to debug and maintain so in general they aren't recommended. In addition to this, in the future, Microsoft may need to add filter drivers in the GNSS device stack for extending functionality and having additional filter drivers from the IHVs will make the architecture more complex unnecessarily.

The driver follows the generic UMDF 2.0 model (User Mode Driver Framework) for function drivers. KMDF (Kernel Mode Driver Framework) drivers could be used but they're strongly discouraged as they bring higher risk of instability to the platform, they're harder to debug, and they can't make direct use of user mode OS components.
This design guide assumes basic familiarity with UMDF 2.0, Windows kernel-mode programming, kernel I/O management, power management, and the PnP device stack.

## Related articles

[Global Navigation Satellite System (GNSS) driver requirements](gnss-driver-requirements.md)  

[Global Navigation Satellite System (GNSS) driver architecture](gnss-driver-architecture.md)  
