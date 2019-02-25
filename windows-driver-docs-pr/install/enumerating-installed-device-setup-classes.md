---
title: Enumerating Installed Device Setup Classes
description: Enumerating Installed Device Setup Classes
ms.assetid: 24F7600B-AA61-484a-83E9-E4C3FD2EAF17
keywords:
- enumerating installed device setup classes WDK
- installed device setup classes WDK
- installed device setup classes WDK , enumerating
- device setup classes WDK device installations , enumerating
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Installed Device Setup Classes


To discover the [device setup classes](device-setup-classes.md) that are installed in a system, do not enumerate the device setup classes by directly accessing registry keys. As with any registry key, the location and format of these keys might change between different versions of Windows.

To safely discover the installed device setup classes, and to query and modify the properties of a setup class, follow these steps:

1.  Use [**SetupDiBuildClassInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550909) or [**SetupDiBuildClassInfoListEx**](https://msdn.microsoft.com/library/windows/hardware/ff550911) to retrieve the set of device setup classes that are currently installed on the system.

2.  Use [**SetupDiGetClassDescription**](https://msdn.microsoft.com/library/windows/hardware/ff551053) or [**SetupDiGetClassDescriptionEx**](https://msdn.microsoft.com/library/windows/hardware/ff551058) to retrieve the description of an installed setup class.

3.  Use [**SetupDiGetClassRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551097) to query the setup class properties and [**SetupDiSetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552169) to set the setup class properties.

4.  Use [**SetupDiOpenClassRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552065) or [**SetupDiOpenClassRegKeyEx**](https://msdn.microsoft.com/library/windows/hardware/ff552067) to access the persistent registry storage for custom device setup class settings.

 

 





