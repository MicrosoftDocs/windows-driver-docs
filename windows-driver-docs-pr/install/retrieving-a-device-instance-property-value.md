---
title: Retrieving A Device Instance Property Value
description: Retrieving A Device Instance Property Value
ms.assetid: 4cec9132-5a28-492d-bbb1-39e388413ad0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving A Device Instance Property Value


To retrieve the value of a device instance property on Windows Vista and later versions of Windows, follow these steps:

1.  Call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to determine the data type and the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to retrieve a property.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to retrieve a property.
    -   Set *PropertyKey* to a pointer to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property.
    -   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable.
    -   Set *Flags* to zero.

    In response to the first call to [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963), **SetupDiGetDeviceProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceProperty** again and supply the same parameter values that were supplied in the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the required size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetDeviceProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceProperty** succeeds, **SetupDiGetDeviceProperty** sets \**PropertyType* to the property-data-type identifier for the property, returns the property value in the *PropertyBuffer* buffer, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





