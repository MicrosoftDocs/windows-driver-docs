---
title: PSHED Plug-In Guidelines
description: PSHED Plug-In Guidelines
ms.assetid: 2d17ebef-9474-4825-be09-c924ebd60c44
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , guidelines
- PSHED plug-ins WDK WHEA , guidelines
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 

 




