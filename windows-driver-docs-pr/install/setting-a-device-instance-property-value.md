---
title: Setting a Device Instance Property Value
description: Setting a Device Instance Property Value
ms.date: 04/20/2017
---

# Setting a Device Instance Property Value


To set the value of a device instance property on Windows Vista and later versions of Windows, call [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to set the property.

-   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure that represents the device instance for which to set the property.

-   Set *PropertyKey* to a pointer to the [**DEVPROPKEY**](./devpropkey.md) structure that represents the property to set.

-   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](/previous-versions/ff543546(v=vs.85))-typed variable that supplies the property-data-type identifier for the property to set.

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value.

-   Set *RequiredSize* to a DWORD-typed variable.

-   Set *Flags* to zero.

If this call to [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw) succeeds, **SetupDiSetDeviceProperty** sets the device instance property and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) will return the logged error code.

