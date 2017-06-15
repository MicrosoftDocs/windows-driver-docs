---
title: Specifying Exclusive Access to Device Objects
author: windows-driver-content
description: Specifying Exclusive Access to Device Objects
MS-HAID:
- 'DevObjts\_8482b40f-9993-4d39-b88b-0c02a9b3e460.xml'
- 'kernel.specifying\_exclusive\_access\_to\_device\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b492251b-55b0-4323-a508-b395bb3da0ef
keywords: ["exclusive access WDK device objects", "device objects WDK kernel , exclusive access", "single access WDK device objects"]
---

# Specifying Exclusive Access to Device Objects


## <a href="" id="ddk-specifying-exclusive-access-to-device-objects-kg"></a>


If exclusive access to a device is enabled, only one handle to the device can be open at a time. For the I/O manager to enforce exclusive access to the device, the exclusive property must be set for the named device object in the device stack.

For a WDM device stack that has a both a PDO and an FDO, the exclusive property can be set only by the INF file, by using an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320). The PDO is the named object in the stack, but the bus driver (not the function driver itself) creates the PDO, on behalf of the function driver. The only way to direct the bus driver to set the exclusive flag for the PDO is by the class or device INF files. (The call to the [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) routine creates the FDO; setting the exclusive flag for the FDO has no effect.)

Drivers whose device objects are not stacked, such as non-WDM drivers and devices that operate in raw mode, can use the [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) routine to set the exclusive property for their named device object.

The I/O manager enforces exclusivity on a per name basis on named device objects, regardless of the trailing name. For example, suppose the device object has the name "\\Device\\DeviceName". Then, the I/O manager enforces exclusivity for a request to open "\\Device\\DeviceName\\*Filename1*" followed by "\\Device\\DeviceName\\*Filename2*". If two objects in the device stack are named (which is not recommended), the I/O manager allows a single handle to be opened for each object. In such a situation, drivers must enforce exclusivity themselves within their [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266) routines. The I/O manager also does not enforce exclusivity for opens relative to another file handle. For more information about file open requests in the device's namespace, see [Controlling Device Namespace Access](controlling-device-namespace-access.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Specifying%20Exclusive%20Access%20to%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


