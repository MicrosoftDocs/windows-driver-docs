---
title: Setting a Device Instance Property Value
description: Setting a Device Instance Property Value
ms.assetid: 45f63ee3-278e-4b8c-a666-c860074fa172
---

# Setting a Device Instance Property Value


To set the value of a device instance property on Windows Vista and later versions of Windows, call [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) and supply the following parameters values:

-   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to set the property.

-   Set *DeviceInfoData* to a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to set the property.

-   Set *PropertyKey* to a pointer to the [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property to set.

-   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed variable that supplies the property-data-type identifier for the property to set.

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value.

-   Set *RequiredSize* to a DWORD-typed variable.

-   Set *Flags* to zero.

If this call to [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163) succeeds, **SetupDiSetDeviceProperty** sets the device instance property and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Setting%20a%20Device%20Instance%20Property%20Value%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




