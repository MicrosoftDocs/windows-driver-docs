---
title: Named Device Objects
author: windows-driver-content
description: Named Device Objects
ms.assetid: 4e24f0c1-57b2-4e06-a7f5-9a93d365ac8c
keywords: ["device objects WDK kernel , named", "named device objects WDK kernel"]
ms.author: windowsdriverdev
ms.date: 09/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Named Device Objects


## <a href="" id="ddk-named-device-objects-kg"></a>


A device object, like all object manager objects, can be named or unnamed. When a user-mode application makes an I/O request, it specifies the target of the operation by name. The object manager resolves the name to determine the destination of the I/O request.

> [!IMPORTANT]
> To help increase driver security name device objects only when necessary. Named device objects are generally only necessary for legacy reasons, for example if you have an application that expects to open the device using a particular name or if you’re using a non-PNP device/control device.  Note that WDF drivers do not need to name their PnP device in order to create a symbolic link using [WdfDeviceCreateSymbolicLink](https://msdn.microsoft.com/library/windows/hardware/ff545939.aspx).

A driver can specify a name for a device object when it calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create the device object. For more information about when and how to name a device object, see [NT Device Names](nt-device-names.md).
  
A named device object can also have an MS-DOS device name, which is a symbolic link created by [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) or [**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050). WDM drivers do not in general require an MS-DOS device name. For more information, see [MS-DOS Device Names](ms-dos-device-names.md).

> [!IMPORTANT]
> If you use a named device object you can use [IoCreateDeviceSecure](https://msdn.microsoft.com/library/windows/hardware/ff548407.aspx) and specify a SDDL to help secure it. When you implement [IoCreateDeviceSecure](https://msdn.microsoft.com/library/windows/hardware/ff548407.aspx) always specify a custom class GUID for DeviceClassGuid. You should not specify an existing class GUID here. Doing so has the potential to break security settings or compatibility for other devices belonging to that class. For more information, see [WdmlibIoCreateDeviceSecure](https://msdn.microsoft.com/library/windows/hardware/mt800803.aspx).
> 
> In order to allow applications or other WDF drivers to access your PnP device, you should use device interfaces. For more information, see [Using Device Interfaces](https://docs.microsoft.com/windows-hardware/drivers/wdf/using-device-interfaces). A device interface serves as a symbolic link to your device stack’s PDO. Once way to control access to the PDO is by specifying an SDDL string in your INF. If the SDDL string is not in the INF file, Windows will apply a default security descriptor. For more information, see [Securing Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/securing-device-objects) and [SDDL for Device Objects](https://docs.microsoft.com/windows-hardware/drivers/kernel/sddl-for-device-objects).


This section contains the following subsections:

[NT Device Names](nt-device-names.md)

[MS-DOS Device Names](ms-dos-device-names.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Named%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


