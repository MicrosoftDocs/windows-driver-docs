---
title: Controlling Device Namespace Access
description: Controlling Device Namespace Access
ms.assetid: e5312297-849f-4b4e-835d-0ce5295c7ce2
keywords: ["device objects WDK kernel , security", "security WDK device objects", "device namespace access WDK kernel", "namespaces WDK device objects", "file open requests WDK device objects", "open requests WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Controlling Device Namespace Access





In the Windows Driver Model (WDM), every device object has an associated *namespace*. Names in the device's namespace are paths that begin with the device's name. For a device named "\\*Device*\\*DeviceName*", its namespace consists of any name of the form "\\*Device*\\*DeviceName*\\*FileName*". (For a file system, *FileName* is an actual name of a file on the file system.)

A WDM driver receives open requests for all names in the device's namespace. The driver treats an open request for "\\*Device*\\*DeviceName*" as an open of the device object itself. If the driver implements support for open requests into the device's namespace, then it treats an open request for "\\*Device*\\*DeviceName*\\*FileName*" as an open of a "file" within the device object's namespace (where the notion of "file" for the device is driver-determined).

Most drivers do not implement support for open operations into the device's namespace, but all drivers must provide security checks to prevent unauthorized access to the device's namespace. By default, security checks for file open requests within the device's namespace, (for example, "\\*Device*\\*DeviceName*\\*FileName*") are left entirely up to the driver—the device object ACL is not checked by the operating system.

If a device object's FILE\_DEVICE\_SECURE\_OPEN characteristic is set, the system applies the device object's security descriptor to all file open requests in the device's namespace. Drivers can set FILE\_DEVICE\_SECURE\_OPEN when they create the device object with [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407). For WDM drivers, FILE\_DEVICE\_SECURE\_OPEN can also be set in the registry. It can also be set in the registry for device objects of non-WDM drivers that are created by **IoCreateDeviceSecure**. For more information about setting device object properties, such as the device characteristics, in the registry, see [Setting Device Object Properties in the Registry](setting-device-object-properties-in-the-registry.md). For more information about device characteristics, see [Specifying Device Characteristics](specifying-device-characteristics.md).

Drivers for devices that do not support namespaces must use one of two methods to ensure that file open requests within the device's namespace are handled correctly:

-   The driver's device objects have the FILE\_DEVICE\_SECURE\_OPEN device characteristic set. The driver can then treat any open request into the device's namespace as an open request for the device object.

-   The driver can fail any [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) requests that specify an **IrpSp-&gt;FileObject-&gt;FileName** parameter whose length is nonzero. In this case, open requests for the device are subject to the system's ACL check, while all file open requests within the device's namespace are failed by the driver. (Drivers that support exclusive opens must use this option.)

Drivers for devices that do support namespaces can also use two methods to secure file open requests into the device's namespace:

-   The driver's device objects have the FILE\_DEVICE\_SECURE\_OPEN device characteristic set. This ensures that the security settings for the device apply uniformly to the device's namespace. (The driver is responsible for implementing support for the namespace in its [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) callback function.)

-   The driver checks any ACLs for the file name in its *DispatchCreate* routine. (Even in this case the driver should set the FILE\_DEVICE\_SECURE\_OPEN characteristic unless opens into the device's namespace can have weaker security settings than the device object.)

The FILE\_DEVICE\_SECURE\_OPEN characteristic is checked at the top of the stack, so filter device objects must copy the **Characteristics** member of the next-lower device object after attaching.

 

 




