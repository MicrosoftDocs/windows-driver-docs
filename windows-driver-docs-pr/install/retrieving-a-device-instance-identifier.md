---
title: Retrieving a Device Instance Identifier
description: Retrieving a Device Instance Identifier
ms.assetid: 6382fdf6-109a-430a-b6b5-322d3eebc4a1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving a Device Instance Identifier


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports a device property that represents the device instance identifier. The unified device property model uses the [**DEVPKEY_Device_InstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff542532) [property key](property-keys.md) to represent this property.

Windows Server 2003, Windows XP, and Windows 2000 also support this property. However, these earlier Windows versions do not support the property key of the unified device property model. Instead, you can retrieve a device instance identifier on these earlier versions of Windows by calling [**SetupDiGetDeviceInstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff551106). To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support **SetupDiGetDeviceInstanceId**. However, you should use the corresponding property key to access this property on Windows Vista and later.

For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To retrieve a device instance identifier on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call **SetupDiGetDeviceInstanceId** to retrieve the size, in bytes, of the device instance identifier. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to the device information set that contains the device information element for which to retrieve the requested device instance identifier.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device information element for which to retrieve a device instance identifier.
    -   Set *DeviceInstanceId* to **NULL**.
    -   Set *DeviceInstanceIdSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable that receives the number of characters required to store the NULL-terminated device instance identifier.

    In response to the first call to [**SetupDiGetDeviceInstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff551106), **SetupDiGetDeviceInstanceId** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) returns the most recently logged error code.

2.  Call **SetupDiGetDeviceInstanceId** again and supply the same parameter values that were supplied in the first call, except for the following changes:
    -   Set *DeviceInstanceId* to a pointer to a string buffer that receives the NULL-terminated device instance identifier that is associated with the device information element.
    -   Set *DeviceInstanceIdSize* to the size, in characters, of the *DeviceInstanceId* buffer. The first call to **SetupDiGetDeviceInstanceId** retrieved the required size of the *DeviceInstanceId* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceInstanceId** succeeds, **SetupDiGetDeviceInstanceId** sets the *DeviceInstanceId* buffer to the device instance identifier, sets \**RequiredSize* to the size, in characters, of the device instance identifier that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceInstanceId** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) returns the logged error code.

 

 





