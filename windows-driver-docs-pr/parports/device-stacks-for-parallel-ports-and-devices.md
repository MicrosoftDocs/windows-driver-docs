---
title: Device Stacks for Parallel Ports and Devices
author: windows-driver-content
description: Device Stacks for Parallel Ports and Devices
MS-HAID:
- 'sspd\_55bde216-5e17-4441-a30a-5c68b1771e5f.xml'
- 'parports.device\_stacks\_for\_parallel\_ports\_and\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 80222ed9-f900-4d97-b459-2d8ca780e1d1
keywords: ["system-supplied parallel drivers WDK , device stacks", "device stacks WDK parallel drivers", "parallel devices WDK , device stacks"]
---

# Device Stacks for Parallel Ports and Devices


## <a href="" id="ddk-device-stacks-for-parallel-ports-and-devices-kg"></a>


This section describes the device stacks created by the system-supplied parallel drivers for parallel ports and devices that are attached to parallel ports.

The following figure shows the type of device stacks that the system-supplied parallel drivers create for parallel ports and devices attached to parallel ports.

![diagram illustrating windows device and driver stacks for parallel ports and devices](images/parport4.png)

Vendor-supplied function drivers for parallel devices that are attached to parallel ports are optional. The system-supplied parallel drivers provide extensive support for directly controlling a parallel device as a raw device, and for controlling a device's parent parallel port.

For more information about how to operate parallel ports and devices that are attached to parallel ports, see:

[Parallel Device Interfaces, Internal Names, and Symbolic Links](parallel-device-interfaces--internal-names--and-symbolic-links.md)

[IOCTL and Callback Support for Parallel Ports and Devices](ioctl-and-callback-support-for-parallel-ports-and-devices.md)

[Operating a Parallel Port](operating-a-parallel-port.md)

[Operating a Parallel Device Attached to a Parallel Port](operating-a-parallel-device-attached-to-a-parallel-port.md)

[Client Interfaces to System-Supplied Parallel Drivers](https://msdn.microsoft.com/library/windows/hardware/ff543926)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Device%20Stacks%20for%20Parallel%20Ports%20and%20Devices%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


