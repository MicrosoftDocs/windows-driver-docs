---
title: Access Co-installers Registry Entry Value of Device Setup Class
description: Accessing the Co-installers Registry Entry Value of a Device Setup Class
ms.assetid: 731d29df-6fdd-4f25-9758-d7306fef7ec0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Co-installers Registry Entry Value of a Device Setup Class


In Windows Vista and later versions of Windows, the [unified device property model](unified-device-property-model--windows-vista-and-later-.md) includes a [device setup class property](accessing-device-setup-class-properties.md) that represents the co-installers that are installed for the class. The unified device property model uses the [**DEVPKEY_DeviceClass_ClassCoInstallers**](https://msdn.microsoft.com/library/windows/hardware/ff542264) [property key](property-keys.md) to represent this property.

Windows Server 2003, Windows XP, and Windows 2000 also support this property. However, these earlier versions of Windows do not support the property key of the unified device property model. Instead, these versions of Windows represent this property by using a corresponding system-defined registry entry value. To maintain compatibility with these earlier versions of Windows, Windows Vista and later versions also support this system-defined registry entry value. However, you should use the property key to access these properties on Windows Vista and later versions.

For information about how to use property keys to access device setup class properties on Windows Vista and later versions, see [Accessing Device Class Properties (Windows Vista and Later)](accessing-device-class-properties--windows-vista-and-later-.md).

On Windows Server 2003, Windows XP, and Windows 2000, you can set or retrieve this property by using the Windows registry functions to access the following registry entry value for a device setup class:

**HLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers\\{**<em>device-setup-class-guid</em>**}**.

For information about registering a class co-installer, see [Registering a Class Co-installer](registering-a-class-co-installer.md).

 

 





