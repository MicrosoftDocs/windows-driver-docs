---
title: Determining Which Properties Are Set for a Device Instance
description: Determining Which Properties Are Set for a Device Instance
ms.date: 04/20/2017
---

# Determining Which Properties Are Set for a Device Instance


To determine which properties are set for a device instance on Windows Vista and later versions of Windows, follow these steps:

1.  Call [**SetupDiGetDevicePropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys) to determine how many properties are set for a device instance. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to retrieve a list of property keys.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that represents the device instance for which to retrieve the list of property keys.
    -   Set *PropertyKeyArray* to **NULL**.
    -   Set *PropertyKeyCount* to zero.
    -   Set *RequiredPropertyKeyCount* to a pointer to a DWORD-typed variable.
    -   Set *Flags* to zero.

    In response to the call to [**SetupDiGetDevicePropertyKeys**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertykeys), **SetupDiGetDevicePropertyKeys** sets \**RequiredPropertyKeyCount* to the number of properties that are set for the device instance, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the most recently logged error code.

2.  Call **SetupDiGetDevicePropertyKeys** again and supply the same parameter values that were supplied in the first call, except for the following changes:

    -   Set *PropertyKeyArray* as a [**DEVPROPKEY**](./devpropkey.md)-typed pointer to the buffer that receives the requested property key array.
    -   Set *PropertyKeyCount* to the size, in DEVPROPKEY-typed values, of the *PropertyKeyArray* buffer. The first call to **SetupDiGetDevicePropertyKeys** retrieved the required size of the *PropertyKeyArray* buffer in \**RequiredPropertyKeyCount*.

If the second call to **SetupDiGetDevicePropertyKeys** succeeds, **SetupDiGetDevicePropertyKeys** returns the requested property key array in the *PropertyKeyArray* buffer, sets \**RequiredPropertyKeyCount* to the number of property keys in the buffer, and returns **TRUE**. If the function call fails, **SetupDiGetDevicePropertyKeys** returns **FALSE** and calling [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the logged error code.

