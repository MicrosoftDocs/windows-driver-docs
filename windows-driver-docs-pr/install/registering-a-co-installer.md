---
title: Registering a Co-installer
description: Registering a Co-installer
ms.assetid: a585bb06-d65f-4e14-a205-dc0d6523363e
keywords:
- co-installers WDK device installations , registering
- registering co-installers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Registering a Co-installer


## <a href="" id="ddk-registering-a-co-installer-dg"></a>


A co-installer can be registered for a single device or for all the devices in a particular setup class. A device-specific co-installer is registered dynamically through the INF file when one of its devices is installed. A class co-installer is registered manually or by a Custom Device Installation Application and an INF.

For more information, see

[Registering a Device-Specific Co-installer](registering-a-device-specific-co-installer.md)

[Registering a Class Co-installer](registering-a-class-co-installer.md)

To update a co-installer, each new version of the DLL should have a new filename because the DLL is typically in use when the user clicks the Update Driver button on the device property page.

 

 





