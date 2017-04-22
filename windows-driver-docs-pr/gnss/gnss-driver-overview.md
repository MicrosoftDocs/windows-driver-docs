---
title: GNSS driver overview
author: windows-driver-content
description: Use this guide to learn how to implement the DeviceIoControl APIs with the GNSS driver so that a HLOS like the GNSS adapter can access GNSS functionality.
ms.assetid: 1887097A-C495-4295-9904-B2964F46A81D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GNSS driver overview


Use the GNSS driver design guide to learn how to implement the **DeviceIoControl** APIs with the GNSS driver so that a high level operating system component (HLOS) like the GNSS adapter can access the desired GNSS functionality.

The GNSS functionality can be augmented by an IHV to provide positions at lower power cost or to provide better performance when needed.

The new GNSS drivers are fully owned and delivered by IHVs, with no Microsoft-owned code running in kernel mode .

**Note**  IHVs must not add filter drivers to the GNSS/Location stack. Filter drivers are hard to debug and maintain so in general they are not recommended. In addition to this, in the future, Microsoft may need to add filter drivers in the GNSS device stack for extending functionality and having additional filter drivers from the IHVs will make the architecture more complex unnecessarily.

 

The driver follows the generic UMDF 2.0 model (User Mode Driver Framework) for function drivers. KMDF (Kernel Mode Driver Framework) drivers could be used but they are strongly discouraged as they bring higher risk of instability to the platform, they are harder to debug, and they cannot make directly use of user mode OS components.
This design guide assumes basic familiarity with UMDF 2.0, Windows kernel-mode programming, kernel I/O management, power management, and the PnP device stack.

## Related topics
[GNSS driver requirements](gnss-driver-requirements.md)  
[GNSS driver architecture](gnss-driver-architecture.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20GNSS%20driver%20overview%20%20RELEASE:%20%281/9/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


