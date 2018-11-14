---
title: Determining Which Properties Are Set for a Device Class
description: Determining Which Properties Are Set for a Device Class
ms.assetid: a8016b04-ae52-47d9-b3ef-74e0896aa825
ms.date: 04/20/2017
ms.localizationpriority: medium
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
    -   If the device class is a device setup class, set *Flags* to DICLASSPROP_INSTALLER; otherwise, if the device class is a device interface class, set *Flags* to DICLASSPROP_INTERFACE.

    In response to this first call to [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091), **SetupDiGetClassPropertyKeys** sets \**RequiredPropertyKeyCount* to the number of properties that are set for the device setup class, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetDevicePropertyKeys** again and supply the same parameters that were supplied in the first call, except for the following changes:
    -   Set *PropertyKeyArray* to a [**DEVPROPKEY**](https://msdn.microsoft.com/library/windows/hardware/ff543544)-typed pointer to the buffer that receives the requested property key array.
    -   Set *PropertyKeyCount* to the size, in DEVPROPKEY-typed values, of the *PropertyKeyArray* buffer. The first call to **SetupDiGetClassPropertyKeys** returned the required size of the *PropertyKeyArray* buffer in \**RequiredPropertyKeyCount*.

If the second call to **SetupDiGetClassPropertyKeys** succeeds, the function returns the requested property key array in the *PropertyKeyArray* buffer, sets \**RequiredPropertyKeyCount* to the number of property keys in the buffer, and returns **TRUE**. If the function call fails, **SetupDiGetClassPropertyKeys** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

### <a href="" id="determining-which-class-properties-are-set-for-a-device-class-on-a-rem"></a> Determining Which Class Properties Are Set for a Device Class on a Remote Computer

To determine the class properties that are set for a device class on a remote computer, follow the procedure that is described in [Determining Which Class Properties Are Set for a Device Class on a Local Computer](#determining-which-class-properties-are-set-for-a-device-class-on-a-loc) with the following modifications:

-   Call [**SetupDiGetClassPropertyKeysEx**](https://msdn.microsoft.com/library/windows/hardware/ff551093) instead of [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091).

-   In addition to supplying the parameter values that are required for both [**SetupDiGetClassPropertyKeysEx**](https://msdn.microsoft.com/library/windows/hardware/ff551093) and [**SetupDiGetClassPropertyKeys**](https://msdn.microsoft.com/library/windows/hardware/ff551091), supply the *MachineName* parameter, which must be set to a pointer to a NULL-terminated string that contains the UNC name, including the \\\\ prefix, of a computer.

 

 





