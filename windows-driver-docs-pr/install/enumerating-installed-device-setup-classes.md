---
title: Enumerating Installed Device Setup Classes
description: Enumerating Installed Device Setup Classes
ms.assetid: 24F7600B-AA61-484a-83E9-E4C3FD2EAF17
keywords: ["enumerating installed device setup classes WDK", "installed device setup classes WDK", "installed device setup classes WDK , enumerating", "device setup classes WDK device installations , enumerating"]
---

# Enumerating Installed Device Setup Classes


To discover the [device setup classes](device-setup-classes.md) that are installed in a system, do not enumerate the device setup classes by directly accessing registry keys. As with any registry key, the location and format of these keys might change between different versions of Windows.

To safely discover the installed device setup classes, and to query and modify the properties of a setup class, follow these steps:

1.  Use [**SetupDiBuildClassInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550909) or [**SetupDiBuildClassInfoListEx**](https://msdn.microsoft.com/library/windows/hardware/ff550911) to retrieve the set of device setup classes that are currently installed on the system.

2.  Use [**SetupDiGetClassDescription**](https://msdn.microsoft.com/library/windows/hardware/ff551053) or [**SetupDiGetClassDescriptionEx**](https://msdn.microsoft.com/library/windows/hardware/ff551058) to retrieve the description of an installed setup class.

3.  Use [**SetupDiGetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551097) to query the setup class properties and [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169) to set the setup class properties.

4.  Use [**SetupDiOpenClassRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552065) or [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) to access the persistent registry storage for custom device setup class settings.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Enumerating%20Installed%20Device%20Setup%20Classes%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




