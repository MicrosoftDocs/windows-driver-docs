---
title: Determining Which Properties Are Set for a Device Class
description: Determining Which Properties Are Set for a Device Class
ms.assetid: a8016b04-ae52-47d9-b3ef-74e0896aa825
---

# Determining Which Properties Are Set for a Device Class


The following topics describe how to determine which class properties are set for a device class in Windows Vista and later versions of Windows:

[Determining Which Class Properties Are Set for a Device Class on a Local Computer](#determining-which-class-properties-are-set-for-a-device-class-on-a-loc)

[Determining Which Class Properties Are Set for a Device Class on a Remote Computer](#determining-which-class-properties-are-set-for-a-device-class-on-a-rem)

### <a href="" id="determining-which-class-properties-are-set-for-a-device-class-on-a-loc"></a> Determining Which Class Properties Are Set for a Device Class on a Local Computer

To determine which properties are set for a device class on a local computer, follow these steps:

1.  Call [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091) to determine how many properties are set for a device class. Supply the following parameter values:

    -   Set *ClassGuid* to a pointer to a GUID that identifies the [device setup class](device-setup-classes.md) or [device interface class](device-interface-classes.md) for which to retrieve a list of the class property keys.
    -   Set *PropertyKeyArray* to **NULL**.
    -   Set *PropertyKeyCount* to zero.
    -   Set *RequiredPropertyKeyCount* to a pointer to a DWORD-typed variable.
    -   If the device class is a device setup class, set *Flags* to DICLASSPROP\_INSTALLER; otherwise, if the device class is a device interface class, set *Flags* to DICLASSPROP\_INTERFACE.

    In response to this first call to [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091), **SetupDiGetClassPropertyKeys** sets \**RequiredPropertyKeyCount* to the number of properties that are set for the device setup class, logs the error code ERROR\_INSUFFICIENT\_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDevicePropertyKeys** again and supply the same parameters that were supplied in the first call, except for the following changes:
    -   Set *PropertyKeyArray* to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)-typed pointer to the buffer that receives the requested property key array.
    -   Set *PropertyKeyCount* to the size, in DEVPROPKEY-typed values, of the *PropertyKeyArray* buffer. The first call to **SetupDiGetClassPropertyKeys** returned the required size of the *PropertyKeyArray* buffer in \**RequiredPropertyKeyCount*.

If the second call to **SetupDiGetClassPropertyKeys** succeeds, the function returns the requested property key array in the *PropertyKeyArray* buffer, sets \**RequiredPropertyKeyCount* to the number of property keys in the buffer, and returns **TRUE**. If the function call fails, **SetupDiGetClassPropertyKeys** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### <a href="" id="determining-which-class-properties-are-set-for-a-device-class-on-a-rem"></a> Determining Which Class Properties Are Set for a Device Class on a Remote Computer

To determine the class properties that are set for a device class on a remote computer, follow the procedure that is described in [Determining Which Class Properties Are Set for a Device Class on a Local Computer](#determining-which-class-properties-are-set-for-a-device-class-on-a-loc) with the following modifications:

-   Call [**SetupDiGetClassPropertyKeysEx**](https://msdn.microsoft.com/library/windows/hardware/ff551093) instead of [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091).

-   In addition to supplying the parameter values that are required for both [**SetupDiGetClassPropertyKeysEx**](https://msdn.microsoft.com/library/windows/hardware/ff551093) and [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091), supply the *MachineName* parameter, which must be set to a pointer to a NULL-terminated string that contains the UNC name, including the \\\\ prefix, of a computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Determining%20Which%20Properties%20Are%20Set%20for%20a%20Device%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




