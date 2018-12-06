---
title: Creating a New Device Setup Class
description: Creating a New Device Setup Class
ms.assetid: 3235d1e9-f6f7-4efe-a50c-5ea7a9956e7e
keywords:
- device setup classes WDK device installations
- setup classes WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating a New Device Setup Class





You should only create a new device setup class if absolutely necessary. It is usually possible to assign your device to one of the [system-defined device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff553419).

If your device meets both of the following criteria, you should assign it to an existing device setup class:

-   Your device's installation and configuration requirements match those of an existing class.

-   Your device's capabilities match those of an existing class.

Under the either of following circumstances, you should consider providing a device co-installer:

-   Your device has installation requirements that are not supported by an existing device type-specific INF file.

-   Installation of your device requires device property pages that are not provided by an existing class.

If your device provides capabilities that are significantly different from the capabilities that are provided by devices that belong to existing classes, it might merit a new device setup class. However, you must never create a new setup class for a device that belongs to one of the system-supplied classes. If you do, you will bypass the system-supplied class installer and your device will not be correctly integrated into the system.

If you think a new device setup class is needed, your new class should be based on new device capabilities, and not on the device's location. For example, supporting an existing device on a new bus should not require a new setup class.

Before creating a new device setup class, contact Microsoft to find out if a new system-supplied device setup class is being planned for your device type

You can create a new device setup class by using an INF file. In addition to installing support for a device, an INF file can initialize a new device setup class for the device. Such an INF file has an [**INF ClassInstall32 section**](inf-classinstall32-section.md).

 

 





