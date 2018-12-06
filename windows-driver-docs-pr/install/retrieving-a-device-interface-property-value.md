---
title: Retrieving a Device Interface Property Value
description: Retrieving a Device Interface Property Value
ms.assetid: 2a845adc-6965-420d-9e0a-20935d20577a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving a Device Interface Property Value


Starting with Windows Vista, follow these steps to retrieve the value of a [device interface property](https://msdn.microsoft.com/library/windows/hardware/ff541409):

1.  Call [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122) to determine the data type and the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains a device interface for which to retrieve a list of device interface property keys.
    -   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure that represents the device interface for which to retrieve a list of device property keys.
    -   Set *PropertyKey* to a pointer to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property.
    -   Set *PropertyType* to a pointer to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a DWORD-typed variable.
    -   Set Flags to zero.

    In response to the first call to [**SetupDiGetDeviceInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551122), **SetupDiGetDeviceInterfaceProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceInterfaceProperty** again and supply the same parameter values that were supplied to the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the required size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetDeviceInterfaceProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceInterfaceProperty** succeeds, **SetupDiGetDeviceInterfaceProperty** sets \**PropertyType* to the property-data-type identifier for the property, sets the *PropertyBuffer* buffer to the property value, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceInterfaceProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





