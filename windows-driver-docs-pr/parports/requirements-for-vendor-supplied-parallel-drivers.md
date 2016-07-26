---
title: Requirements for Vendor-Supplied Parallel Drivers
author: windows-driver-content
description: Requirements for Vendor-Supplied Parallel Drivers
MS-HAID:
- 'vspd\_5287f4de-5caa-44ed-99a6-a65e0ccc261b.xml'
- 'parports.requirements\_for\_vendor\_supplied\_parallel\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2194ad1a-3548-4b67-9268-4245389cf264
keywords: ["vendor-supplied parallel drivers WDK , about vendor-supplied parallel drivers"]
---

# Requirements for Vendor-Supplied Parallel Drivers


## <a href="" id="ddk-requirements-for-vendor-supplied-parallel-drivers-kg"></a>


This section describes Microsoft Windows requirements for vendor-supplied drivers for parallel ports and devices attached to parallel ports.

Vendor-supplied function drivers and bus drivers for parallel ports are not required because the [system-supplied parallel drivers](system-supplied-parallel-drivers.md) provide these functions. The system-supplied parallel drivers provide extensive support for operating parallel ports and devices attached to parallel ports.

Vendor-supplied function drivers for parallel devices attached to parallel ports are optional. The system-supplied parallel drivers provide extensive support for directly controlling a parallel device as a raw device, and for operating a device's parent parallel port.

If a vendor provides a function driver for a parallel device, the driver must support Plug and Play and power management. Microsoft recommends that the driver be a WDM driver.

The following topics describe how a vendor-supplied function driver for a parallel device operates a device and the device's parent parallel port:

[Operating a Parallel Port](operating-a-parallel-port.md)

[Operating a Parallel Device Attached to a Parallel Port](operating-a-parallel-device-attached-to-a-parallel-port.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Requirements%20for%20Vendor-Supplied%20Parallel%20Drivers%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


