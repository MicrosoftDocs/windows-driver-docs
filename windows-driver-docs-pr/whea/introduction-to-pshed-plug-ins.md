---
title: Introduction to PSHED Plug-Ins
author: windows-driver-content
description: Introduction to PSHED Plug-Ins
ms.assetid: 31c540ec-c1d0-48e3-9eab-b458a5213f7e
keywords:
- platform-specific hardware error driver plug-ins WDK WHEA , about platform-specific hardware error driver plug-ins
- PSHED plug-ins WDK WHEA , about platform-specific hardware error driver plug-ins
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to PSHED Plug-Ins


Platform vendors can supplement the default PSHED functionality by providing PSHED plug-ins that take advantage of platform-specific capabilities. A PSHED plug-in is a special-purpose Windows device driver that implements a callback interface that is called by the PSHED. The purpose of a PSHED plug-in is to augment or override the default behavior of the PSHED provided by Microsoft.

A PSHED plug-in is implemented as a [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM) device driver that is loaded by the Plug and Play (PnP) manager when a specific hardware identifier is enumerated during system startup. The platform vendor specifies the hardware identifier that initiates loading of the PSHED plug-in. This hardware identifier can be in the ACPI namespace or it can be in another device namespace.

PSHED plug-ins do not handle any I/O requests that are initiated by a user-mode application or by a higher level driver. Therefore, a PSHED plug-in is only required to implement the following two driver dispatch routines: [**DispatchPnP**](https://msdn.microsoft.com/library/windows/hardware/ff543341) and [**DispatchPower**](https://msdn.microsoft.com/library/windows/hardware/ff543354). PSHED plug-ins do not have to register device interfaces or create symbolic links for their device objects.

A PSHED plug-in participates in one or more of the following [functional areas](functional-areas.md) that are associated with the handling of hardware errors:

-   [Error Source Discovery](error-source-discovery.md)

-   [Error Source Control](error-source-control.md)

-   [Error Record Persistence](error-record-persistence.md)

-   [Error Information Retrieval](error-information-retrieval.md)

-   [Error Recovery](error-recovery.md)

-   [Error Injection](error-injection.md)

For each of these functional areas, a PSHED plug-in implements callback functions that are called by the PSHED. A PSHED plug-in specifies the functional areas in which it participates and provides pointers to the associated callback functions when it [registers](registering-a-pshed-plug-in.md) itself with the PSHED. Multiple PSHED plug-ins can be registered with the PSHED at the same time. However, if more than one registered PSHED plug-in specifies that it participates in a particular functional area, only the last one to register itself will actually participate in that functional area.

A PSHED plug-in is intended to be implemented by platform vendors as a software interface to the hardware platform's hardware error reporting and recovery capabilities. A PSHED plug-in can interface with the platform firmware using whatever private interfaces or mechanisms are defined by the platform vendor. This allows the platform vendor to continue using existing firmware for hardware error handling. In time, Microsoft expects that more hardware error reporting and recovery capabilities will be standardized. At that point, the need for PSHED plug-ins for general error handling and reporting will diminish such that PSHED plug-ins will only be required for supporting vendor-specific features that provide additional value beyond the standard hardware error handling functionality.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Introduction%20to%20PSHED%20Plug-Ins%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


