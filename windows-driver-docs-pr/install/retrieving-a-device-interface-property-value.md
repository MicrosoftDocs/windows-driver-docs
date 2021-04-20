---
title: Retrieving a Device Interface Property Value
description: Retrieving a Device Interface Property Value
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving a Device Interface Property Value


Starting with Windows Vista, follow these steps to retrieve the value of a [device interface property](/previous-versions/ff541409(v=vs.85)):

1.  Call [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) to determine the data type and the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains a device interface for which to retrieve a list of device interface property keys.
    -   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_data) structure that represents the device interface for which to retrieve a list of device property keys.
    -   Set *PropertyKey* to a pointer to a [**DEVPROPKEY**](./devpropkey.md) structure that represents the property.
    -   Set *PropertyType* to a pointer to a [**DEVPROPKEY**](./devpropkey.md)-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a DWORD-typed variable.
    -   Set Flags to zero.

    In response to the first call to [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw), **SetupDiGetDeviceInterfaceProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the most recently logged error code.

2.  Call **SetupDiGetDeviceInterfaceProperty** again and supply the same parameter values that were supplied to the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the required size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetDeviceInterfaceProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetDeviceInterfaceProperty** succeeds, **SetupDiGetDeviceInterfaceProperty** sets \**PropertyType* to the property-data-type identifier for the property, sets the *PropertyBuffer* buffer to the property value, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceInterfaceProperty** returns **FALSE** and a call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the logged error code.

