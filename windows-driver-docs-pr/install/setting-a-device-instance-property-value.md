---
title: Setting a Device Instance Property Value
description: Setting a Device Instance Property Value
ms.assetid: 45f63ee3-278e-4b8c-a666-c860074fa172
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting a Device Instance Property Value


To set the value of a device instance property on Windows Vista and later versions of Windows, call [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to set the property.

-   Set *DeviceInfoData* to a pointer to an [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to set the property.

-   Set *PropertyKey* to a pointer to the [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property to set.

-   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed variable that supplies the property-data-type identifier for the property to set.

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value.

-   Set *RequiredSize* to a DWORD-typed variable.

-   Set *Flags* to zero.

If this call to [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) succeeds, **SetupDiSetDeviceProperty** sets the device instance property and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





