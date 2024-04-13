---
title: Registering a Co-installer
description: Registering a Co-installer
keywords:
- co-installers WDK device installations , registering
- registering co-installers
ms.date: 04/20/2017
---

# Registering a Co-installer

> [!NOTE]
> Features described in this section are not supported and driver packages containing them will no longer receive a Microsoft signature. See [Using a Universal INF File](using-a-universal-inf-file.md).

A co-installer can be registered for a single device or for all the devices in a particular setup class. A device-specific co-installer is registered dynamically through the INF file when one of its devices is installed. A class co-installer is registered manually or by a Custom Device Installation Application and an INF.

For more information, see

[Registering a Device-Specific Co-installer](registering-a-device-specific-co-installer.md)

[Registering a Class Co-installer](registering-a-class-co-installer.md)

To update a co-installer, each new version of the DLL should have a new filename because the DLL is typically in use when the user clicks the Update Driver button on the device property page.

 

 





