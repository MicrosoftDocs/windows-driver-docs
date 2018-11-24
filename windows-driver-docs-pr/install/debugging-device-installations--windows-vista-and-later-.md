---
title: Debugging Device Installations
description: Debugging Device Installations
ms.assetid: bc7105f6-8ba7-49da-8c02-ceda69066daa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging Device Installations


On Windows Vista and later versions of Windows, the core stages of device installation are always run in a non-interactive context known as *server-side installations*. The host process for device installation (*DrvInst.exe*) runs under the security context of the LocalSystem account.

Because the server-side installations run non-interactively and must complete without any user input, it provides some challenges to the driver package developer who wants to debug the actions of the [driver package's](driver-packages.md) class-installer and co-installer DLLs. For the developer of a driver package, it is usually most desirable to debug the actions of a co-installer DLL during the installation of a device.

This section contains the following topics, which describe techniques that are used to debug co-installers during the core stages of device installation:

[Enabling Support for Debugging Device Installations](enabling-support-for-debugging-device-installations.md)

[Debugging Device Installations with a User-mode Debugger](debugging-device-installations-with-a-user-mode-debugger.md)

[Debugging Device Installations with the Kernel Debugger (KD)](debugging-device-installations-with-the-kernel-debugger--kd-.md)

For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

 

 





