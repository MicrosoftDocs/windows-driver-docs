---
title: Setting a Device Class Property Value
description: Setting a Device Class Property Value
ms.assetid: a1d6908d-e43a-413d-965b-3af226d5c26f
---

# Setting a Device Class Property Value


The following topics describe how to set a device class property value in Windows Vista and later versions of Windows:

[Setting a Device Class Property Value on a Local Computer](#setting-a-device-class-property-value-on-a-local-computer)

[Setting a Device Class Property Value on a Remote Computer](#setting-a-device-class-property-value-on-a-remote-computer)

### <a href="" id="setting-a-device-class-property-value-on-a-local-computer"></a> Setting a Device Class Property Value on a Local Computer

To set the value of a device class property, call [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128) and supply the following parameters values:

-   Set *ClassGuid* to a pointer to a GUID that identifies the [device setup class](device-setup-classes.md) or [device interface class](device-interface-classes.md) for which to set a class property.

-   Set *PropertyKey* to a pointer to the [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property to set.

-   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed variable that supplies the property-data-type identifier for the property to set.

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the property value.

-   Set *RequiredSize* to a DWORD-typed variable.

-   If the device class is a device setup class, set *Flags* to DICLASSPROP\_INSTALLER. Otherwise, if the device class is a device interface class, set *Flags* to DICLASSPROP\_INTERFACE.

If a call to [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128) succeeds, **SetupDiSetClassProperty** sets the device class property and returns **TRUE**. If the function call fails, **SetupDiSetClassProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### <a href="" id="setting-a-device-class-property-value-on-a-remote-computer"></a> Setting a Device Class Property Value on a Remote Computer

To set a device class property value on a remote computer, follow the procedure that is described in [Setting a Device Class Property Value on a Local Computer](#setting-a-device-class-property-value-on-a-local-computer) with the following modifications:

-   Call [**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132) instead of **SetupDiSetClassProperty**.

-   In addition to supplying the parameter values that both **SetupDiSetClassPropertyEx** and **SetupDiSetClassProperty** require, supply the *MachineName* parameter, which must be set to a pointer to a NULL-terminated string that contains the UNC name, including the \\\\ prefix, of a computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Setting%20a%20Device%20Class%20Property%20Value%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




