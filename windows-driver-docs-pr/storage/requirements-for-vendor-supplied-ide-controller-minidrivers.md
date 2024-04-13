---
title: Introduction to Vendor-Supplied IDE Controller Minidrivers
description: Requirements for Vendor-Supplied IDE Controller Minidrivers
keywords:
- IDE controller minidrivers WDK storage , vendor-supplied
- storage IDE controller minidrivers WDK , vendor-supplied
- vendor-supplied IDE controller minidrivers WDK storage
ms.date: 12/15/2019
---

# Introduction to Vendor-Supplied IDE Controller Minidrivers

The Microsoft-supplied IDE port driver, *atapi.sys*, and controller driver, *pciidex.sys*, are hardware-independent and can be used with almost all IDE controllers. Thus, vendor-supplied port drivers and controller drivers are not required.

Microsoft also supplies a native controller minidriver, *pciide.sys*, which handles the hardware-dependent aspects of the controller driver-minidriver pair and which can be used with most IDE controller hardware. Vendors can elect to supply their own controller minidriver instead of using *pciide.sys*.

A vendor-supplied controller minidriver:

- Does not need to support Plug and Play (PnP) or power management. PnP and power management operations are handled by the Microsoft-supplied controller driver, *pciidex.sys*.

- Does not need to register any particular interface to comply with system requirements.

- Should not attempt to access the registry or call kernel-mode routines other than those provided by the *PciIdeX* library.

- Must provide a set of standard minidriver routines that permit the system-supplied controller driver to do hardware-dependent operations transparently.

For more information about the *PciIdeX* library and a description of the minidriver routine interface between the system-supplied controller driver and a vendor-supplied controller minidriver, see [Initializing and Calling IDE Minidriver Routines](initializing-and-calling-ide-minidriver-routines.md).

 

 




