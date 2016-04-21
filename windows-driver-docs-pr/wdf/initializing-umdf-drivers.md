---
title: Initializing UMDF Drivers
author: windows-driver-content
description: Initializing UMDF Drivers
ms.assetid: b21ec019-1a80-4219-8aa8-3545ec3383b9
keywords: ["User-Mode Driver Framework WDK , initializing drivers", "UMDF WDK , initializing drivers", "user-mode drivers WDK UMDF , initializing", "initializing drivers WDK UMDF", "reflectors WDK UMDF", "loading reflectors WDK UMDF", "driver host process WDK UMDF"]
---

# Initializing UMDF Drivers


\[This topic applies to UMDF 1.*x*.\]

Before a UMDF driver for a device is initialized, the driver manager and the reflector are loaded by the operating system and the driver host process is created. To ensure that a device starts successfully, the driver manager is loaded and fully initialized by the time the reflector initializes.

When the device is installed, the Plug and Play (PnP) subsystem loads the reflector, if not already loaded. The reflector then contacts the driver manager to create the driver host process. The framework within the newly created driver host process then calls the [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) method to initialize the UMDF driver, if not already initialized.

The framework adds a new device object for each device loaded in the driver host process. The following sections show an overview and provide details on how the framework adds a new device:

-   [Adding a Device Overview](adding-a-device-overview.md)
-   [Adding a Device](adding-a-device.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Initializing%20UMDF%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




