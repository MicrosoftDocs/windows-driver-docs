---
title: Retrieving a Device Instance Identifier
description: Retrieving a Device Instance Identifier
ms.assetid: 6382fdf6-109a-430a-b6b5-322d3eebc4a1
---

# Retrieving a Device Instance Identifier


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports a device property that represents the device instance identifier. The unified device property model uses the [**DEVPKEY\_Device\_InstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff542532) [property key](property-keys.md) to represent this property.

Windows Server 2003, Windows XP, and Windows 2000 also support this property. However, these earlier Windows versions do not support the property key of the unified device property model. Instead, you can retrieve a device instance identifier on these earlier versions of Windows by calling [**SetupDiGetDeviceInstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff551106). To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support **SetupDiGetDeviceInstanceId**. However, you should use the corresponding property key to access this property on Windows Vista and later.

For information about how to use property keys to access device driver properties on Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To retrieve a device instance identifier on Windows Server 2003, Windows XP, and Windows 2000, follow these steps:

1.  Call **SetupDiGetDeviceInstanceId** to retrieve the size, in bytes, of the device instance identifier. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to the device information set that contains the device information element for which to retrieve the requested device instance identifier.
    -   Set *DeviceInfoData* to a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device information element for which to retrieve a device instance identifier.
    -   Set *DeviceInstanceId* to **NULL**.
    -   Set *DeviceInstanceIdSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable that receives the number of characters required to store the NULL-terminated device instance identifier.

    In response to the first call to [**SetupDiGetDeviceInstanceId**](https://msdn.microsoft.com/library/windows/hardware/ff551106), **SetupDiGetDeviceInstanceId** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR\_INSUFFICIENT\_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) returns the most recently logged error code.

2.  Call **SetupDiGetDeviceInstanceId** again and supply the same parameter values that were supplied in the first call, except for the following changes:
    -   Set *DeviceInstanceId* to a pointer to a string buffer that receives the NULL-terminated device instance identifier that is associated with the device information element.
    -   Set *DeviceInstanceIdSize* to the size, in characters, of the *DeviceInstanceId* buffer. The first call to **SetupDiGetDeviceInstanceId** retrieved the required size of the *DeviceInstanceId* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceInstanceId** succeeds, **SetupDiGetDeviceInstanceId** sets the *DeviceInstanceId* buffer to the device instance identifier, sets \**RequiredSize* to the size, in characters, of the device instance identifier that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceInstanceId** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) returns the logged error code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Retrieving%20a%20Device%20Instance%20Identifier%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




