---
title: Specifying Exclusive Access to Device Objects
description: Specifying Exclusive Access to Device Objects
ms.assetid: b492251b-55b0-4323-a508-b395bb3da0ef
keywords: ["exclusive access WDK device objects", "device objects WDK kernel , exclusive access", "single access WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Specifying Exclusive Access to Device Objects





If exclusive access to a device is enabled, only one handle to the device can be open at a time. For the I/O manager to enforce exclusive access to the device, the exclusive property must be set for the named device object in the device stack.

For a WDM device stack that has a both a PDO and an FDO, the exclusive property can be set only by the INF file, by using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320). The PDO is the named object in the stack, but the bus driver (not the function driver itself) creates the PDO, on behalf of the function driver. The only way to direct the bus driver to set the exclusive flag for the PDO is by the class or device INF files. (The call to the [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) routine creates the FDO; setting the exclusive flag for the FDO has no effect.)

Drivers whose device objects are not stacked, such as non-WDM drivers and devices that operate in raw mode, can use the [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) routine to set the exclusive property for their named device object.

The I/O manager enforces exclusivity on a per name basis on named device objects, regardless of the trailing name. For example, suppose the device object has the name "\\Device\\DeviceName". Then, the I/O manager enforces exclusivity for a request to open "\\Device\\DeviceName\\*Filename1*" followed by "\\Device\\DeviceName\\*Filename2*". If two objects in the device stack are named (which is not recommended), the I/O manager allows a single handle to be opened for each object. In such a situation, drivers must enforce exclusivity themselves within their [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback functions. The I/O manager also does not enforce exclusivity for opens relative to another file handle. For more information about file open requests in the device's namespace, see [Controlling Device Namespace Access](controlling-device-namespace-access.md).

 

 




