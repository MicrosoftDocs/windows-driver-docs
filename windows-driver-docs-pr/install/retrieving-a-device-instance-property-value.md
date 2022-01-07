---
title: Retrieving A Device Instance Property Value
description: Retrieving A Device Instance Property Value
ms.date: 04/20/2017
---

# Retrieving A Device Instance Property Value


To retrieve the value of a device instance property on Windows Vista and later versions of Windows, follow these steps:

1.  Call [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to determine the data type and the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to retrieve a property.
    -   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that represents the device instance for which to retrieve a property.
    -   Set *PropertyKey* to a pointer to a [**DEVPROPKEY**](./devpropkey.md) structure that represents the property.
    -   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](/previous-versions/ff543546(v=vs.85))-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable.
    -   Set *Flags* to zero.

    In response to the first call to [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw), **SetupDiGetDeviceProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceProperty** again and supply the same parameter values that were supplied in the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the required size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetDeviceProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceProperty** succeeds, **SetupDiGetDeviceProperty** sets \**PropertyType* to the property-data-type identifier for the property, returns the property value in the *PropertyBuffer* buffer, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the logged error code.

