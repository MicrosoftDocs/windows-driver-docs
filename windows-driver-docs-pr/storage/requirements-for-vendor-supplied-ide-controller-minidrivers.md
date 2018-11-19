---
title: Requirements for Vendor-Supplied IDE Controller Minidrivers
description: Requirements for Vendor-Supplied IDE Controller Minidrivers
ms.assetid: a1584665-8788-49a4-b86f-50c265e7ce7a
keywords:
- IDE controller minidrivers WDK storage , vendor-supplied
- storage IDE controller minidrivers WDK , vendor-supplied
- vendor-supplied IDE controller minidrivers WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for Vendor-Supplied IDE Controller Minidrivers


## <span id="ddk_requirements_for_vendor_supplied_ide_controller_minidrivers_kg"></span><span id="DDK_REQUIREMENTS_FOR_VENDOR_SUPPLIED_IDE_CONTROLLER_MINIDRIVERS_KG"></span>


This section describes Microsoft Windows requirements for vendor-supplied IDE controller minidrivers.

The Microsoft-supplied IDE port driver, *atapi.sys*, and controller driver, *pciidex.sys*, are hardware-independent and can be used with almost all IDE controllers. Thus, vendor-supplied port drivers and controller drivers are not required.

Microsoft also supplies a native controller minidriver, *pciide.sys*, which handles the hardware-dependent aspects of the controller driver-minidriver pair and which can be used with most IDE controller hardware. Vendors can elect to supply their own controller minidriver instead of using *pciide.sys*.

A vendor-supplied controller minidriver does not need to support Plug and Play (PnP) or power management. PnP and power management operations are handled by the Microsoft-supplied controller driver, *pciidex.sys*.

A vendor-supplied controller minidriver does not need to register any particular interface to comply with system requirements.

A vendor-supplied controller minidriver should not attempt to access the registry, nor should it call kernel-mode routines other than those provided by the PciIdeX library.

A vendor-supplied controller minidriver must provide a set of standard minidriver routines that permit the system-supplied controller driver to do hardware-dependent operations transparently.

For more information about the PciIdeX library and a description of the minidriver routine interface between the system-supplied controller driver and a vendor-supplied controller minidriver, see [Initializing and Calling IDE Minidriver Routines](initializing-and-calling-ide-minidriver-routines.md).

 

 




