---
title: Requirements for Vendor-Supplied IDE Controller Minidrivers
description: Requirements for Vendor-Supplied IDE Controller Minidrivers
ms.assetid: a1584665-8788-49a4-b86f-50c265e7ce7a
keywords: ["IDE controller minidrivers WDK storage , vendor-supplied", "storage IDE controller minidrivers WDK , vendor-supplied", "vendor-supplied IDE controller minidrivers WDK storage"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Requirements%20for%20Vendor-Supplied%20IDE%20Controller%20Minidrivers%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




