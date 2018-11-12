---
title: Retrieving SPCRP_Xxx Properties
description: Retrieving SPCRP_Xxx Properties
ms.assetid: a5d52da9-a593-42bd-aeaf-8ab203bc3d21
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retrieving SPCRP_Xxx Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the device instance properties that correspond to the SPCRP_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize a [device setup class](device-setup-classes.md). The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows versions use the SPCRP_*Xxx* identifiers to represent and access the device setup class properties. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support using SPCRP_*Xxx* identifiers to access device setup class properties. However, you should use the property keys of the unified device property model to access device setup class properties.

For a list of the system-defined device setup class properties, see [Device Setup Class Properties That Correspond to SPCRP_Xxx Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff542245). The device setup class properties are listed by the property key identifiers that you use to access the properties in Windows Vista and later versions. The information that is provided with the property keys also includes the corresponding SPCRP_*Xxx* identifiers that you can use to access the properties on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

To retrieve device setup class properties on Windows Server 2003, Windows XP, and Windows 2000, use the [**SetupDiGetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551097) function.

To use SetupDiGetClassRegistryProperty to retrieve a property that corresponds to an SPCRP_Xxx identifier, follow these steps:

1.  Call **SetupDiGetClassRegistryProperty** and supply the following parameter values:

    -   Set *ClassGuid* to a pointer to a GUID that represents the device setup class for which to retrieve a property.
    -   Set *Property* to the property identifier with prefix "SPCRP_" for which to retrieve the size of the property value.
    -   Set *PropertyRegDataType* to **NULL**.
    -   Set *PropertyBuffer* to **NULL**.
    -   Set *PropertyBufferSize* to zero.
    -   Set *RequiredSize* to a pointer to a DWORD-typed variable that receives the size, in bytes, of the requested property.
    -   Set *MachineName* to the name of the computer.
    -   Set Reserved to **NULL**.

    In response to the call to [**SetupDiGetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551097), **SetupDiGetClassRegistryProperty** sets \**RequiredSize* to the size, in bytes, of the buffer that is required to retrieve the property value, logs the error code ERROR_INSUFFICIENT_BUFFER, and returns **FALSE**. A subsequent call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

2.  Call **SetupDiGetClassRegistryProperty** again to retrieve the property value and supply the same parameters that were supplied in the first call, except for the following changes:
    -   Set *PropertyBuffer* to a pointer to the buffer that receives the property value.
    -   Set *PropertyBufferSize* to the size, in bytes, of the *PropertyBuffer* buffer. The first call to **SetupDiGetClassRegistryProperty** retrieved the required size of the *PropertyBuffer* buffer in \**RequiredSize*.

If the second call to **SetupDiGetClassRegistryProperty** succeeds, **SetupDiGetClassRegistryProperty** sets \**PropertyRegDataType* to the registry data type, sets the *PropertyBuffer* buffer to the property value, sets \**PropertyBufferSize* to the size, in bytes, of the property value, and returns **TRUE**. If the function call fails, **SetupDiGetClassRegistryProperty** returns **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the logged error code.

 

 





