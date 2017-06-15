---
title: Named Device Objects
author: windows-driver-content
description: Named Device Objects
MS-HAID:
- 'DevObjts\_0c6afdea-cf68-4579-bff2-7c88b580febc.xml'
- 'kernel.named\_device\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4e24f0c1-57b2-4e06-a7f5-9a93d365ac8c
keywords: ["device objects WDK kernel , named", "named device objects WDK kernel"]
---

# Named Device Objects


## <a href="" id="ddk-named-device-objects-kg"></a>


A device object, like all object manager objects, can be named or unnamed. When a user-mode application makes an I/O request, it specifies the target of the operation by name. The object manager resolves the name to determine the destination of the I/O request.

A driver can specify a name for a device object when it calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create the device object. For more information about when and how to name a device object, see [NT Device Names](nt-device-names.md).

A named device object can also have an MS-DOS device name, which is a symbolic link created by [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) or [**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050). WDM drivers do not in general require an MS-DOS device name. For more information, see [MS-DOS Device Names](ms-dos-device-names.md).

This section contains the following subsections:

[NT Device Names](nt-device-names.md)

[MS-DOS Device Names](ms-dos-device-names.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Named%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


