---
title: PSHED Plug-In Guidelines
author: windows-driver-content
description: PSHED Plug-In Guidelines
ms.assetid: 2d17ebef-9474-4825-be09-c924ebd60c44
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , guidelines
- PSHED plug-ins WDK WHEA , guidelines
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PSHED Plug-In Guidelines


The following is a list of guidelines that must be followed by PSHED plug-ins.

-   For corrected errors, the error handling flow is subject to the same restrictions that are imposed on all device drivers. Interrupt service routines (ISRs) must not execute for more than 25 microseconds and deferred procedure calls (DPCs) must not execute for more than 100 microseconds. Therefore, a PSHED plug-in's callback functions, as well as any firmware routines that the PSHED plug-in's callback functions might call, must not execute for arbitrary periods of time. For uncorrected errors, the error handling flow can ignore these restrictions because the system is in a state where data loss might occur if priority is not given to handling the error condition.

-   A PSHED plug-in should only interact directly with hardware that it has asserted control over. This means that a PSHED plug-in should do the following:
    -   Claim ownership of any hardware resources that it interacts with that are architecturally visible to the operating system.
    -   Support Plug and Play (PnP) if any of the hardware resources that it interacts with can be relocated.
    -   Coordinate all interactions with any hardware resources that are not architecturally visible to the operating system with all other software or firmware that interacts with the same hardware resources.
    -   Only interact with hardware resources that are not already manipulated by the PSHED or by a low-level hardware error handler (LLHEH). A PSHED plug-in should only manipulate chipset-specific registers that are not part of the standard chipset registers that are manipulated by the LLHEH.

**Note**   The platform firmware should not assume absolute control over all machine resources, as is generally the case for system management mode error handling code, because in a virtualized or partitioned system, the hardware might be partitioned in such a way that this assumption is false.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20PSHED%20Plug-In%20Guidelines%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


