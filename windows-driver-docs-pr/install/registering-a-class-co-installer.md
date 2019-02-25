---
title: Registering a Class Co-installer
description: Registering a Class Co-installer
ms.assetid: a86a4302-ec37-4117-aa5c-4fa84fbb7902
keywords:
- class co-installers WDK
- registering class co-installers
- setup-class-GUID WDK device installations
- CoDeviceInstallers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a Class Co-installer





To register a co-installer for every device of a particular setup class, create a registry entry like the following under the **HKLM\\System\\CurrentControlSet\\Control\\CoDeviceInstallers** subkey:

```cpp
{setup-class-GUID}: REG_MULTI_SZ : "XyzCoInstall.dll,XyzCoInstallEntryPoint\0\0"
```

The system creates the **CoDeviceInstallers** key. *Setup-class-GUID* specifies the GUID for the [device setup class](device-setup-classes.md). If the co-installer applies to more than one class of devices, create a separate value entry for each setup class.

You must not overwrite other co-installers that have been previously written to the *setup-class-GUID* key. Read the key, append your co-installer string to the [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) list, and write the key back to the registry.

If you omit the *CoInstallEntryPoint*, the default is CoDeviceInstall.

The co-installer DLL must also be copied to the system directory.

The class co-installer is available to be called for relevant devices and services once the file has been copied and the registry entry is made.

Rather than manually creating the registry entry to register a class co-installer, you can register it using an INF file like the following:

```cpp
[version]
signature = "$Windows NT$"
 
[DestinationDirs]
DefaultDestDir = 11    // DIRID_SYSTEM
 
[DefaultInstall]
CopyFiles = @classXcoinst.dll
AddReg = CoInstaller_AddReg
 
[CoInstaller_AddReg]
HKLM,System\CurrentControlSet\Control\CoDeviceInstallers, \
 {setup-class-GUID},0x00010008, "classXcoinst.dll,classXCoInstaller"
; above line uses the line continuation character ()
```

This sample INF copies the file *classXcoinst.dll* to the system directory and makes an entry for the *setup-class-GUID* class under the **CoDeviceInstallers** key. The entry in the *Xxx*_AddReg section specifies two flags: the "00010000" flag specifies that the entry is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), and the "00000008" flag specifies that the new value is to be appended to any existing value (if the new value is not already present in the string).

Such an INF that registers a class co-installer can be activated by a right-click install or through an application that calls **SetupInstallFromInfSection**.

 

 





