---
title: Introduction to PSHED Plug-Ins
description: Introduction to PSHED Plug-Ins
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , about platform-specific hardware error driver plug-ins
- PSHED plug-ins WDK WHEA , about platform-specific hardware error driver plug-ins
ms.date: 03/03/2023
---

# Introduction to PSHED Plug-Ins


Platform vendors can supplement the default PSHED functionality by providing PSHED plug-ins that take advantage of platform-specific capabilities. A PSHED plug-in is a special-purpose Windows device driver that implements a callback interface that is called by the PSHED. The purpose of a PSHED plug-in is to augment or override the default behavior of the PSHED provided by Microsoft.

A PSHED plug-in is implemented as a [Windows Driver Model](../kernel/writing-wdm-drivers.md) (WDM) device driver that is loaded by the Plug and Play (PnP) manager when a specific hardware identifier is enumerated during system startup. The platform vendor specifies the hardware identifier that initiates loading of the PSHED plug-in. This hardware identifier can be in the ACPI namespace or it can be in another device namespace.

PSHED plug-ins do not handle any I/O requests that are initiated by a user-mode application or by a higher level driver. Therefore, a PSHED plug-in is only required to implement driver dispatch routines (see [**DRIVER_DISPATCH**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch)) to handle [IRP_MJ_PNP](../kernel/irp-mj-pnp.md) and [IRP_MJ_POWER](../kernel/irp-mj-power.md) IRPs. PSHED plug-ins do not have to register device interfaces or create symbolic links for their device objects.

A PSHED plug-in participates in one or more of the following [functional areas](functional-areas.md) that are associated with the handling of hardware errors:

-   [Error Source Discovery](error-source-discovery.md)

-   [Error Source Control](error-source-control.md)

-   [Error Record Persistence](error-record-persistence.md)

-   [Error Information Retrieval](error-information-retrieval.md)

-   [Error Recovery](error-recovery.md)

-   [Error Injection](error-injection.md)

For each of these functional areas, a PSHED plug-in implements callback functions that are called by the PSHED. A PSHED plug-in specifies the functional areas in which it participates and provides pointers to the associated callback functions when it [registers](registering-a-pshed-plug-in.md) itself with the PSHED. Multiple PSHED plug-ins can be registered with the PSHED at the same time. However, if more than one registered PSHED plug-in specifies that it participates in a particular functional area, only the last one to register itself will actually participate in that functional area.

A PSHED plug-in is intended to be implemented by platform vendors as a software interface to the hardware platform's hardware error reporting and recovery capabilities. A PSHED plug-in can interface with the platform firmware using whatever private interfaces or mechanisms are defined by the platform vendor. This allows the platform vendor to continue using existing firmware for hardware error handling. In time, Microsoft expects that more hardware error reporting and recovery capabilities will be standardized. At that point, the need for PSHED plug-ins for general error handling and reporting will diminish such that PSHED plug-ins will only be required for supporting vendor-specific features that provide additional value beyond the standard hardware error handling functionality.

