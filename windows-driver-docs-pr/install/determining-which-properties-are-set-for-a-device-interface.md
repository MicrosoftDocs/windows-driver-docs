---
title: Determining Which Properties are Set for a Device Interface
description: Determining Which Properties are Set for a Device Interface
ms.assetid: ef261c1d-0715-4501-b2db-fab270cee010
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Determining Which Properties are Set for a Device Interface


To determine which properties are set for a device interface in Windows Vista and later versions of Windows, follow these steps:

1.  Call [**SetupDiGetDeviceInterfacePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551959) to determine how many properties are set for a device class. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains a device interface instance for which to retrieve a list of device interface property keys.
    -   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552342) structure that represents the device interface instance for which to retrieve a list of device property keys.
    -   Set *PropertyKeyArray* to **NULL**.
    -   Set *PropertyKeyCount* to zero.
    -   Set *RequiredPropertyKeyCount* to a pointer to a DWORD-typed variable.
    -   Set Flags to zero.

    In response to this call to [**SetupDiGetDeviceInterfacePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551959), **SetupDiGetDeviceInterfacePropertyKeys** sets \**RequiredPropertyKeyCount* to the number of properties that are set for the device interface, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceInterfacePropertyKeys** again and supply the same parameter values that were supplied in the first call, except for the following changes:
    -   Set *PropertyKeyArray* to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)-typed pointer to the buffer that receives the requested property key array.
    -   Set *PropertyKeyCount* to the size, in DEVPROPKEY-typed values, of the *PropertyKeyArray* buffer. The first call to **SetupDiGetDeviceInterfacePropertyKeys** retrieved the required size of the *PropertyKeyArray* buffer in \**RequiredPropertyKeyCount*.

If the second call to **SetupDiGetDeviceInterfacePropertyKeys** succeeds, **SetupDiGetDeviceInterfacePropertyKeys** returns the requested property key array in the *PropertyKeyArray* buffer, sets \**RequiredPropertyKeyCount* to the number of property keys in the buffer, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceInterfacePropertyKeys** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





