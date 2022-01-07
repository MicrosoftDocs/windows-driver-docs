---
title: Setting a Device Interface Property Value
description: Setting a Device Interface Property Value
ms.date: 04/20/2017
---

# Setting a Device Interface Property Value


To set the value of a [device interface property](/previous-versions/ff541409(v=vs.85)) in Windows Vista and later versions of Windows, call [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to a device information set that contains the device interface for which to set a device interface property.

-   Set *DeviceInterfaceData* to a pointer to an [**SP_DEVICE_INTERFACE_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_device_interface_data) structure that represents the device interface for which to set a device interface property.

-   Set *PropertyKey* to a pointer to the [**DEVPROPKEY**](./devpropkey.md) structure that represents the property to set.

-   Set *PropertyType* to a pointer to a [**DEVPROPKEY**](./devpropkey.md)-typed variable that supplies the property-data-type identifier for the property to set.

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value.

-   Set *RequiredSize* to a DWORD-typed variable.

-   Set *Flags* to zero.

If the call to [**SetupDiSetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdeviceinterfacepropertyw) succeeds, **SetupDiSetDeviceInterfaceProperty** sets the device class property and returns **TRUE**. If the function call fails, **SetupDiSetDeviceInterfaceProperty** returns **FALSE** and a call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the logged error code.

