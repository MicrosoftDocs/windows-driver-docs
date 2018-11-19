---
title: Retrieving the Status and Problem Code for a Device Instance
description: Retrieving the Status and Problem Code for a Device Instance
ms.assetid: 22ca9ac2-fe67-427d-a6e4-f1d9cbbede52
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving the Status and Problem Code for a Device Instance


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes a [device status property and a problem code property](https://msdn.microsoft.com/library/windows/hardware/ff542254). The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 do not support the property keys of the unified property model, nor do they support corresponding registry entry values that represent these properties. However, the corresponding information can be retrieved by calling the [**CM_Get_DevNode_Status**](https://msdn.microsoft.com/library/windows/hardware/ff538514) function. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support **CM_Get_DevNode_Status**. However, you should use the property keys of the unified device property model to access the device driver properties.

The device driver properties are listed by the property key identifiers that you use to access the property in Windows Vista and later versions.

For information about how to use property keys to access device driver properties in Windows Vista and later versions, see [Accessing Device Instance Properties (Windows Vista and Later)](accessing-device-instance-properties--windows-vista-and-later-.md).

To access the status and problem code for a device instance on Windows Server 2003, Windows XP, and Windows 2000, call **CM_Get_DevNode_Status** and supply the following parameters:

-   Set *pulStatus* to a pointer to a ULONG-typed value that receives the status bit flags that are set for a device instance. The status value can be any combination of the bit flags with prefix "DN_" that are defined in *Cfg.h*.

-   Set *pulProblemNumber* to a pointer to a ULONG-typed value that receives the problem number that is set for a device instance. The problem number is one of the constants with the prefix "CM_PROB_" that are defined in *Cfg.h*. **CM_Get_DevNode_Status** sets the problem number only if DN_HAS_PROBLEM is set in *pulStatus*.

-   Set *dnDevInst* to a device instance handle to the device for which to retrieve the status and problem code.

-   Set *ulFlags* to zero.

If the call to **CM_Get_DevNode_Status** succeeds, **CM_Get_DevNode_Status** retrieves the requested status and problem code for the device instance and returns CR_SUCCESS. If the function call fails, **CM_Get_DevNode_Status** returns one of the error codes with prefix "CR_" that are defined in *Cfgmgr32.h*.

 

 





