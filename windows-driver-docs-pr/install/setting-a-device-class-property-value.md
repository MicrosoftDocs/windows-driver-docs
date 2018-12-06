---
title: Setting a Device Class Property Value
description: Setting a Device Class Property Value
ms.assetid: a1d6908d-e43a-413d-965b-3af226d5c26f
ms.date: 04/20/2017
ms.localizationpriority: medium
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

-   If the device class is a device setup class, set *Flags* to DICLASSPROP_INSTALLER. Otherwise, if the device class is a device interface class, set *Flags* to DICLASSPROP_INTERFACE.

If a call to [**SetupDiSetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552128) succeeds, **SetupDiSetClassProperty** sets the device class property and returns **TRUE**. If the function call fails, **SetupDiSetClassProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### <a href="" id="setting-a-device-class-property-value-on-a-remote-computer"></a> Setting a Device Class Property Value on a Remote Computer

To set a device class property value on a remote computer, follow the procedure that is described in [Setting a Device Class Property Value on a Local Computer](#setting-a-device-class-property-value-on-a-local-computer) with the following modifications:

-   Call [**SetupDiSetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552132) instead of **SetupDiSetClassProperty**.

-   In addition to supplying the parameter values that both **SetupDiSetClassPropertyEx** and **SetupDiSetClassProperty** require, supply the *MachineName* parameter, which must be set to a pointer to a NULL-terminated string that contains the UNC name, including the \\\\ prefix, of a computer.

 

 





