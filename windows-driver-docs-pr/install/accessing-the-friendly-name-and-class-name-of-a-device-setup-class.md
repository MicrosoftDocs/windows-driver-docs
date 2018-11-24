---
title: Accessing Friendly Name and Class Name of a Device Setup Class
description: Accessing the Friendly Name and Class Name of a Device Setup Class
ms.assetid: 52775fc6-1c52-4bed-a943-1afcee67e7e9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Friendly Name and Class Name of a Device Setup Class


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes [device setup class properties](accessing-device-setup-class-properties.md) that represent the friendly name and class name of a device setup class. The unified device property model uses the [**DEVPKEY_DeviceClass_Name**](https://msdn.microsoft.com/library/windows/hardware/ff542315) [property key](property-keys.md) and the [**DEVPKEY_DeviceClass_ClassName**](https://msdn.microsoft.com/library/windows/hardware/ff542272) property key to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 also support these device setup class properties. However, these earlier versions of Windows do not support the property keys of the unified device property model. Instead, these versions of Windows use the following mechanisms to retrieve the corresponding property information:

-   Call [**SetupDiGetClassDescriptionEx**](https://msdn.microsoft.com/library/windows/hardware/ff551058) to retrieve the friendly name of a device setup class.

-   Call [**SetupDiClassNameFromGuid**](https://msdn.microsoft.com/library/windows/hardware/ff550947) to retrieve the class name of a device setup class.

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these mechanisms to access the friendly name and class name of a device setup class. However, you should use the property keys to access these properties in Windows Vista and later versions.

 

 





