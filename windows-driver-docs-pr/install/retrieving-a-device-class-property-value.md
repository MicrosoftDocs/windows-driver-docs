---
title: Retrieving a Device Class Property Value
description: Retrieving a Device Class Property Value
ms.assetid: 50b16bd9-7f38-4128-af8f-8b39b099931f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving a Device Class Property Value


The following topics describe how to retrieve a device class property value in Windows Vista and later versions of Windows:

[Retrieving a Device Class Property Value on a Local Computer](#retrieving-a-device-class-property-value-on-a-local-computer)

[Retrieving a Device Class Property Value on a Remote Computer](#retrieving-a-device-class-property-value-on-a-remote-computer)

### <a href="" id="retrieving-a-device-class-property-value-on-a-local-computer"></a> Retrieving a Device Class Property Value on a Local Computer

To retrieve the value of a device class property on a local computer, follow these steps:

1.  Call [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086) to determine the data type and the size, in bytes, of the property value. Supply the following parameter values:

    -   Set *ClassGuid* to a pointer to a GUID that identifies the [device setup class](device-setup-classes.md) or [device interface class](device-interface-classes.md) for which to retrieve a class property that is set for the device class.
    -   Set *PropertyKey* to a pointer to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544) structure that represents the property.
    -   Set *PropertyType* to a pointer to a [**DEVPROPTYPE**](https://msdn.microsoft.com/library/windows/hardware/ff543546)-typed variable.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a DWORD-typed variable.
    -   If the device class is a device setup class, set *Flags* to DICLASSPROP_INSTALLER. Otherwise, if the device class is a device interface class, set *Flags* to DICLASSPROP_INTERFACE.

    In response to this first call to [**SetupDiGetClassProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551086), **SetupDiGetClassProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetClassProperty** again and supply the same parameters that were supplied in the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the required size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetClassProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetClassProperty** succeeds, **SetupDiGetClassProperty** sets \**PropertyType* to the property-data-type identifier for the property, sets the *PropertyBuffer* buffer to the property value, sets \**RequiredSize* to the size, in bytes, of the property value that was retrieved, and returns **TRUE**. If the function call fails, **SetupDiGetDeviceProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### <a href="" id="retrieving-a-device-class-property-value-on-a-remote-computer"></a> Retrieving a Device Class Property Value on a Remote Computer

To retrieve a device class property value on a remote computer, follow the same procedure as is described in [Retrieving a Device Class Property Value on a Local Computer](#retrieving-a-device-class-property-value-on-a-local-computer) with the following modifications:

-   Call [**SetupDiGetClassPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/ff551090) instead of **SetupDiGetClassProperty**.

-   In addition to supplying the parameter values that **SetupDiGetDevicePropertyEx** and **SetupDiGetClassProperty** both require, supply the *MachineName* parameter, which must be set to a pointer to a NULL-terminated string that contains the UNC name, including the \\\\ prefix, of a computer.

 

 





