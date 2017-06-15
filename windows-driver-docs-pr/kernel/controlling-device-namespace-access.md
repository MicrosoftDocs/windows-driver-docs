---
title: Controlling Device Namespace Access
author: windows-driver-content
description: Controlling Device Namespace Access
MS-HAID:
- 'DevObjts\_65ddffe3-ce3d-47ed-a7e7-dd2a7ff18a7b.xml'
- 'kernel.controlling\_device\_namespace\_access'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e5312297-849f-4b4e-835d-0ce5295c7ce2
keywords: ["device objects WDK kernel , security", "security WDK device objects", "device namespace access WDK kernel", "namespaces WDK device objects", "file open requests WDK device objects", "open requests WDK device objects"]
---

# Controlling Device Namespace Access


## <a href="" id="ddk-controlling-device-namespace-access-kg"></a>


In the Windows Driver Model (WDM), every device object has an associated *namespace*. Names in the device's namespace are paths that begin with the device's name. For a device named "\\*Device*\\*DeviceName*", its namespace consists of any name of the form "\\*Device*\\*DeviceName*\\*FileName*". (For a file system, *FileName* is an actual name of a file on the file system.)

A WDM driver receives open requests for all names in the device's namespace. The driver treats an open request for "\\*Device*\\*DeviceName*" as an open of the device object itself. If the driver implements support for open requests into the device's namespace, then it treats an open request for "\\*Device*\\*DeviceName*\\*FileName*" as an open of a "file" within the device object's namespace (where the notion of "file" for the device is driver-determined).

Most drivers do not implement support for open operations into the device's namespace, but all drivers must provide security checks to prevent unauthorized access to the device's namespace. By default, security checks for file open requests within the device's namespace, (for example, "\\*Device*\\*DeviceName*\\*FileName*") are left entirely up to the driver—the device object ACL is not checked by the operating system.

If a device object's FILE\_DEVICE\_SECURE\_OPEN characteristic is set, the system applies the device object's security descriptor to all file open requests in the device's namespace. Drivers can set FILE\_DEVICE\_SECURE\_OPEN when they create the device object with [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407). For WDM drivers, FILE\_DEVICE\_SECURE\_OPEN can also be set in the registry. It can also be set in the registry for device objects of non-WDM drivers that are created by **IoCreateDeviceSecure**. For more information about setting device object properties, such as the device characteristics, in the registry, see [Setting Device Object Properties in the Registry](setting-device-object-properties-in-the-registry.md). For more information about device characteristics, see [Specifying Device Characteristics](specifying-device-characteristics.md).

Drivers for devices that do not support namespaces must use one of two methods to ensure that file open requests within the device's namespace are handled correctly:

-   The driver's device objects have the FILE\_DEVICE\_SECURE\_OPEN device characteristic set. The driver can then treat any open request into the device's namespace as an open request for the device object.

-   The driver can fail any [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) requests that specify an **IrpSp-&gt;FileObject-&gt;FileName** parameter whose length is nonzero. In this case, open requests for the device are subject to the system's ACL check, while all file open requests within the device's namespace are failed by the driver. (Drivers that support exclusive opens must use this option.)

Drivers for devices that do support namespaces can also use two methods to secure file open requests into the device's namespace:

-   The driver's device objects have the FILE\_DEVICE\_SECURE\_OPEN device characteristic set. This ensures that the security settings for the device apply uniformly to the device's namespace. (The driver is responsible for implementing support for the namespace in its [*DispatchCreate*](https://msdn.microsoft.com/library/windows/hardware/ff543266) routine.)

-   The driver checks any ACLs for the file name in its *DispatchCreate* routine. (Even in this case the driver should set the FILE\_DEVICE\_SECURE\_OPEN characteristic unless opens into the device's namespace can have weaker security settings than the device object.)

The FILE\_DEVICE\_SECURE\_OPEN characteristic is checked at the top of the stack, so filter device objects must copy the **Characteristics** member of the next-lower device object after attaching.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Controlling%20Device%20Namespace%20Access%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


