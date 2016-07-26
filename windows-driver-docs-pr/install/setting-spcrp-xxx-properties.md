---
title: Setting SPCRP\_Xxx Properties
description: Setting SPCRP\_Xxx Properties
ms.assetid: efb0d02e-ec4c-4c1b-900b-c81f504d2919
---

# Setting SPCRP\_Xxx Properties


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) supports the [device setup class properties](https://msdn.microsoft.com/library/windows/hardware/ff542239) that correspond to the SPCRP\_Xxx identifiers that are defined in *Setupapi.h*. These properties characterize a device setup class. The unified device property model uses [property keys](property-keys.md) to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support most of these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the SPCRP\_*Xxx* identifiers to represent the device setup class properties. To maintain compatibility with earlier versions of Windows, Windows Vista and later versions also support using SPCRP\_*Xxx* identifiers to access device setup class properties. However, you should use the property keys of the unified device property model to access device setup class properties.

For a list of the system-defined device setup class properties, see [Device Setup Class Properties That Correspond to SPCRP\_Xxx Identifiers](https://msdn.microsoft.com/library/windows/hardware/ff542245). The device setup class properties are listed by the property key identifiers that you use to access the properties in Windows Vista and later versions. The information that is provided with the property keys also includes the corresponding SPCRP\_*Xxx* identifiers that you can use to access the properties on Windows Server 2003, Windows XP, and Windows 2000.

For information about how to use property keys to access device setup class properties in Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

To set device setup class properties on Windows Server 2003, Windows XP, and Windows 2000, call [**SetupDiSetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552135) and supply the following parameter values:

-   Set *ClassGuid* to a pointer to a GUID that represents the device setup class for which to set a property.

-   Set *Property* to the identifier of the property to set with prefix "SPCRP\_" .

-   Set *PropertyBuffer* to a pointer to the buffer that contains the property value.

-   Set *PropertyBufferSize* to the size, in bytes, of the properly data.

-   Set *MachineName* to the computer name.

-   Set *Reserved* to **NULL**.

If this call to [**SetupDiSetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552135) succeeds, **SetupDiSetClassRegistryProperty** sets the device setup class property and returns **TRUE**. If the function call fails, **SetupDiSetClassRegistryProperty** will return **FALSE** and a call to [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) will return the most recently logged error code.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Setting%20SPCRP_Xxx%20Properties%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




