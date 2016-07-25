---
title: Determining Which Properties Are Set for a Device Instance
description: Determining Which Properties Are Set for a Device Instance
ms.assetid: aeca4da5-9632-4523-aa2d-8d1c64b1eccc
---

# Determining Which Properties Are Set for a Device Instance


To determine which properties are set for a device instance on Windows Vista and later versions of Windows, follow these steps:

1.  Call [**SetupDiGetDevicePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551965) to determine how many properties are set for a device instance. Supply the following parameter values:

    -   Set *DeviceInfoSet* to a handle to a device information set that contains the device instance for which to retrieve a list of property keys.
    -   Set *DeviceInfoData* to a pointer to an [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure that represents the device instance for which to retrieve the list of property keys.
    -   Set *PropertyKeyArray* to **NULL**.
    -   Set *PropertyKeyCount* to zero.
    -   Set *RequiredPropertyKeyCount* to a pointer to a DWORD-typed variable.
    -   Set *Flags* to zero.

    In response to the call to [**SetupDiGetDevicePropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551965), **SetupDiGetDevicePropertyKeys** sets \**RequiredPropertyKeyCount* to the number of properties that are set for the device instance, logs the error code ERROR\_INSUFFICIENT\_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDevicePropertyKeys** again and supply the same parameter values that were supplied in the first call, except for the following changes:

    -   Set *PropertyKeyArray* as a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)-typed pointer to the buffer that receives the requested property key array.
    -   Set *PropertyKeyCount* to the size, in DEVPROPKEY-typed values, of the *PropertyKeyArray* buffer. The first call to **SetupDiGetDevicePropertyKeys** retrieved the required size of the *PropertyKeyArray* buffer in \**RequiredPropertyKeyCount*.

If the second call to **SetupDiGetDevicePropertyKeys** succeeds, **SetupDiGetDevicePropertyKeys** returns the requested property key array in the *PropertyKeyArray* buffer, sets \**RequiredPropertyKeyCount* to the number of property keys in the buffer, and returns **TRUE**. If the function call fails, **SetupDiGetDevicePropertyKeys** returns **FALSE** and calling [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=74036) will return the logged error code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Determining%20Which%20Properties%20Are%20Set%20for%20a%20Device%20Instance%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




