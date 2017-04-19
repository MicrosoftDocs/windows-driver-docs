---
title: Configure PnP Serial Devices to an RS-232 Port
author: windows-driver-content
description: Configuration of Plug and Play Serial Device Connected to an RS-232 Port
ms.assetid: b6a851e2-0fcf-4d64-80ac-51928b823077
keywords: ["Plug and Play serial devices WDK", "serial devices WDK , Plug and Play", "RS-232 ports WDK serial devices"]
---

# Configuration of Plug and Play Serial Device Connected to an RS-232 Port


## <a href="" id="ddk-configuration-of-plug-and-play-serial-device-connected-to-an-rs-23"></a>


This section describes the typical configuration of hardware, drivers, and device stacks for Plug and Play serial devices and legacy pointer devices that are connected to an RS-232 port. This configuration can be used to support serial devices, such as mouse devices, pointing devices, graphic tablets, modems, and digital cameras.

The following diagram shows the typical configuration for a Plug and Play Toaster device.

![diagram illustrating hardware and drivers-and-device-stacks configurations for a plug and play toaster device](images/ser2.png)

Serial and Serenum are used in the previous configurations. Serial creates and attaches a function device object (FDO) to the RS-232 port stack, and Serenum creates and attaches an upper-level filter device object (DO) to the RS-232 port stack. Serenum enumerates the device attached to the RS-232 port after the Plug and Play manager sends an IRP\_MN\_QUERY\_RELATIONS request of type **BusRelations** to the RS-232 device stack.

After Serenum detects a supported device, it creates a physical device object (PDO) and reports the device to the Plug and Play manager. The configuration manager uses the INF file and installers for the Toaster device to complete the Toaster device installation. A Toaster driver creates an FDO and attaches it to the Toaster device stack. Filter DOs can also be added to the Toaster device stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Configuration%20of%20Plug%20and%20Play%20Serial%20Device%20Connected%20to%20an%20RS-232%20Port%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


