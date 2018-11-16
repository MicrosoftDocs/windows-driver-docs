---
title: Setting Device Object Properties in the Registry
description: Setting Device Object Properties in the Registry
ms.assetid: a2cfe098-0d5d-42fb-bbdc-25376ce50a9b
keywords: ["device objects WDK kernel , registry", "registry WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting Device Object Properties in the Registry





Properties of device objects can be set in the registry as follows:

-   For WDM drivers, properties can be set for each model of a device, or for a whole device setup class. (For more information about device setup classes, see [Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff541509).)

-   For non-WDM drivers, properties can be set for a named device object's device setup class. The driver specifies the device setup class when it creates the device object with **IoCreateDeviceSecure**. For more information about how to specify a device setup class, see [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407).

Any settings in the registry override the properties supplied when the driver created the device object.

Registry settings are specified by an INF file that is used during device installation, or they can be specified after installation by an application that calls the [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299).

This section contains the following subsections:

[Setting Device Object Registry Properties During Installation](setting-device-object-registry-properties-during-installation.md)

[Setting Device Object Registry Properties After Installation](setting-device-object-registry-properties-after-installation.md)

 

 




