---
title: Debugging Device Installations
description: Debugging Device Installations
ms.assetid: bc7105f6-8ba7-49da-8c02-ceda69066daa
---

# Debugging Device Installations


On Windows Vista and later versions of Windows, the core stages of device installation are always run in a non-interactive context known as *server-side installations*. The host process for device installation (*DrvInst.exe*) runs under the security context of the LocalSystem account.

Because the server-side installations run non-interactively and must complete without any user input, it provides some challenges to the driver package developer who wants to debug the actions of the [driver package's](driver-packages.md) class-installer and co-installer DLLs. For the developer of a driver package, it is usually most desirable to debug the actions of a co-installer DLL during the installation of a device.

This section contains the following topics, which describe techniques that are used to debug co-installers during the core stages of device installation:

[Enabling Support for Debugging Device Installations](enabling-support-for-debugging-device-installations.md)

[Debugging Device Installations with a User-mode Debugger](debugging-device-installations-with-a-user-mode-debugger.md)

[Debugging Device Installations with the Kernel Debugger (KD)](debugging-device-installations-with-the-kernel-debugger--kd-.md)

For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Debugging%20Device%20Installations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




