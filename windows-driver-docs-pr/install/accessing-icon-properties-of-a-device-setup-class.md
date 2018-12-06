---
title: Accessing Icon Properties of a Device Setup Class
description: Accessing Icon Properties of a Device Setup Class
ms.assetid: 082b23ee-8f5c-41ad-9bb1-1437b71aa921
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing Icon Properties of a Device Setup Class


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes [device setup class properties](accessing-device-setup-class-properties.md) that represent icon properties of a device setup class. The unified device property model uses the [**DEVPKEY_DeviceClass_Icon**](https://msdn.microsoft.com/library/windows/hardware/ff542299) [property key](property-keys.md) and the [**DEVPKEY_DeviceClass_IconPath**](https://msdn.microsoft.com/library/windows/hardware/ff542303) property key to represent these properties.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support these device setup class properties. However, these earlier versions of Windows do support the following mechanisms to retrieve information about device setup class icons:

-   Call [**SetupDiLoadClassIcon**](https://msdn.microsoft.com/library/windows/hardware/ff552053) to retrieve the index of the mini-icon for a device setup class in the *MiniIconIndex* output parameter. You can then pass the retrieved mini-icon index to [**SetupDiDrawMiniIcon**](https://msdn.microsoft.com/library/windows/hardware/ff551005) to draw a mini-icon of the retrieved class icon in a specified device context.

-   Call SetupDiLoadClassIcon to load the large icon for a device setup class in the context of the caller and return a handle to the large icon to the caller.

To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support these mechanisms to access the icons of a device setup class. However, you should use the property keys to access the icon properties in Windows Vista and later versions.

 

 





