---
title: Accessing the Friendly Name and Class Name of a Device Setup Class
description: Accessing the Friendly Name and Class Name of a Device Setup Class
ms.assetid: 52775fc6-1c52-4bed-a943-1afcee67e7e9
---

# Accessing the Friendly Name and Class Name of a Device Setup Class


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes [device setup class properties](accessing-device-setup-class-properties.md) that represent the friendly name and class name of a device setup class. The unified device property model uses the [**DEVPKEY\_DeviceClass\_Name**](https://msdn.microsoft.com/library/windows/hardware/ff542315) [property key](property-keys.md) and the [**DEVPKEY\_DeviceClass\_ClassName**](https://msdn.microsoft.com/library/windows/hardware/ff542272) property key to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to retrieve the corresponding property information:

-   Call [**SetupDiGetClassDescriptionEx**](https://msdn.microsoft.com/library/windows/hardware/ff551058) to retrieve the friendly name of a device setup class.

-   Call [**SetupDiClassNameFromGuid**](https://msdn.microsoft.com/library/windows/hardware/ff550947) to retrieve the class name of a device setup class.

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these mechanisms to access the friendly name and class name of a device setup class. However, you should use the property keys to access these properties in Windows Vista and later versions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Accessing%20the%20Friendly%20Name%20and%20Class%20Name%20of%20a%20Device%20Setup%20Class%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




