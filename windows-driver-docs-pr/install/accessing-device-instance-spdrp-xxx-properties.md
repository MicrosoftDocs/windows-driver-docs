---
title: Accessing Device Instance SPDRP_Xxx Properties
description: Accessing Device Instance SPDRP_Xxx Properties
ms.assetid: 15ee51f8-1904-43ee-8bc2-311688c860e0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Device Instance SPDRP_Xxx Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the device instance properties that correspond to the SPDRP_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize the configuration of a device instance. The unified device property model uses [property keys](property-keys.md) to represent these properties. Windows Server 2003, Windows XP, and Windows 2000 also support these device driver properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these earlier Windows versions use the SPDRP_*Xxx* identifiers to represent and access the device instance properties.

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support using SPDRP_Xxx identifiers to access device instance properties. However, you should use the corresponding property keys to access these properties on Windows Vista and later versions of Windows.

For a list of the system-defined device instance properties that have corresponding SPDRP_Xxx identifiers, see [Device Properties That Have Corresponding SPDRP_Xxx Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff541469). The device instance properties are listed by the property keys that you use to access the properties in Windows Vista and later versions of Windows. The information that is provided with each property key includes the corresponding SPDRP_*Xxx* identifiers that you can use to access the property on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device instance properties in Windows Vista and later versions of Windows, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

### Accessing a Device Property

To access device instance properties that correspond to the SPDRP_*Xxx* identifiers on Windows Server 2003, Windows XP, and Windows 2000, use the following SetupAPI functions:

-   [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967)

    This function retrieves a device property that is specified by a SPDRP_*Xxx* identifier.

-   [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169)

    This function sets the device property that is specified by a SPDRP_*Xxx* identifier.

### Retrieving a Device Property

To retrieve a device property on Windows Server 2003, Windows XP, and Microsoft Windows 2000, follow these steps:

1.  Call **SetupDiGetDeviceRegistryProperty** to retrieve the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to retrieve the requested property value.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to retrieve the requested property value.
    -   Set *Property* to an SPDRP_*Xxx* identifier. For a list of these identifiers and a description of the corresponding device properties, see the description of the *Property* parameter that is included with [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169).
    -   Set *PropertyRegDataType* to a pointer to a DWORD-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable that receives, the size, in bytes of the property value.

    In response to the call to [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169), **SetupDiGetDeviceRegistryProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceRegistryProperty** again and supply the same parameter values that were supplied in the first call, except for the following changes:

    -   Set *PropertyBuffer* to a pointer to a BYTE-typed buffer that receives the requested property value.
    -   Set *PropertyBufferSize* to the size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetDeviceRegistryProperty** retrieved the required size of the PropertyBuffer buffer in \**RequiredSize*.

    If the second call to **SetupDiGetDeviceRegistryProperty** succeeds, **SetupDiGetDeviceRegistryProperty** sets \**PropertyRegDataType* to the registry data type of the property value, sets the *PropertyBuffer* buffer to the property value, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceRegistryProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### Setting a Device Property

To set a device property on Windows Server 2003, Windows XP, and Windows 2000, call [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169) and supply the following parameter values:

-   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to set property value.

-   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to set property value.

-   Set *Property* to an SPDRP_*Xxx* identifier.

-   Set *PropertyBuffer* to a pointer to a BYTE-typed buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value that is supplied in the *PropertyBuffer* buffer.

If this call to **SetupDiSetDeviceRegistryProperty** succeeds, **SetupDiSetDeviceRegistryProperty** sets the device instance property and returns **TRUE**. If the function call fails, **SetupDiSetDeviceRegistryProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





