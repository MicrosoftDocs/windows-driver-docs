---
title: Setting SPCRP_Xxx Properties
description: Setting SPCRP_Xxx Properties
ms.assetid: efb0d02e-ec4c-4c1b-900b-c81f504d2919
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting SPCRP_Xxx Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the [device setup class properties](https://msdn.microsoft.com/library/windows/hardware/ff542239) that correspond to the SPCRP_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize a device setup class. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the SPCRP_*Xxx* identifiers to represent the device setup class properties. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support using SPCRP_*Xxx* identifiers to access device setup class properties. However, you should use the property keys of the unified device property model to access device setup class properties.

For a list of the system-defined device setup class properties, see [Device Setup Class Properties That Correspond to SPCRP_Xxx Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff542245). The device setup class properties are listed by the property key identifiers that you use to access the properties in Windows Vista and later versions. The information that is provided with the property keys also includes the corresponding SPCRP_*Xxx* identifiers that you can use to access the properties on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

To set device setup class properties on Windows Server 2003, Windows XP, and Windows 2000, call [**SetupDiSetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552135) and supply the following parameter values:

-   Set *ClassGuid* to a pointer to a GUID that represents the device setup class for which to set a property.

-   Set *Property* to the identifier of the property to set with prefix "SPCRP_" .

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the properly data.

-   Set *MachineName* to the computer name.

-   Set *Reserved* to **NULL**.

If this call to [**SetupDiSetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552135) succeeds, **SetupDiSetClassRegistryProperty** sets the device setup class property and returns **TRUE**. If the function call fails, **SetupDiSetClassRegistryProperty** will return **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

 

 





