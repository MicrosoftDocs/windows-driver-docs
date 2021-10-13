---
title: Registering a Device-Specific Co-installer
description: Registering a Device-Specific Co-installer
keywords:
- device-specific co-installers WDK device installations
- registering device-specific co-installers
ms.date: 10/01/2021
ms.localizationpriority: medium
---

# Registering a Device-Specific Co-installer

To register a device-specific co-installer, add the following sections to the device's INF file:

```inf
;  :
;  :
[DestinationDirs]
XxxCopyFilesSection = 11                \\DIRID_SYSTEM
                                        \\ Xxx = driver or dev. prefix
;  :
;  :
[XxxInstall.OS-platform.CoInstallers]   \\ OS-platform is optional
CopyFiles = XxxCopyFilesSection
AddReg = Xxx.OS-platform.CoInstallers_AddReg
 
[XxxCopyFilesSection]
XxxCoInstall.dll
 
[Xxx.OS-platform.CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,"XxxCoInstall.dll, \
 XxxCoInstallEntryPoint"
```

The entry in the [**DestinationDirs**](./inf-destinationdirs-section.md) section specifies that files listed in the *Xxx*CopyFilesSection will be copied to the system directory.
The *Xxx* prefix should be a unique identifier for the driver, the device, or a group of devices (for example, `cdrom_CopyFilesSection`).

The next section, in the above example `XxxInstall.OS-platform.CoInstallers`, is the [***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md) section.
The name of this section can have an optional OS/architecture extension (for example, `cdrom_install.NTx86.CoInstallers`).
It contains a [**CopyFiles directive**](./inf-copyfiles-directive.md) that specifies a *file-list-section* called `XxxCopyFilesSection`, and an [**AddReg directive**](./inf-addreg-directive.md) that specifies an *add-registry section* called `Xxx.OS-platform.CoInstallers_AddReg`.

The entry in the *add-registry section* creates a **CoInstallers32** value entry in the device's *driver key*.
The entry contains the co-installer DLL and, optionally, a specific entry point.
If you omit the entry point, the default is CoDeviceInstall.
The hexadecimal flags parameter (0x00010000) specifies that this is a [REG_MULTI_SZ](/windows/desktop/SysInfo/registry-value-types) value entry.

To register more than one device-specific co-installer for a device, copy the files for each co-installer and include more than one string in the registry entry.
For example, to register two co-installers, create INF sections like the following:

```inf
;   :
;   :
[DestinationDirs]
XxxCopyFilesSection = 11                \\DIRID_SYSTEM
                                        \\ Xxx = driver or dev. prefix
;   :
;   :
[XxxInstall.OS-platform.CoInstallers]   \\ OS-platform is optional
CopyFiles = XxxCopyFilesSection
AddReg = Xxx.OS-platform.CoInstallers_AddReg
 
[XxxCopyFilesSection]
XxxCoInstall.dll                         \\ copy 1st coinst. file
YyyCoInstall.dll                         \\ copy 2nd coinst. file
 
[Xxx.OS-platform.CoInstallers_AddReg]
HKR,,CoInstallers32,0x00010000,                 \
    "XxxCoInstall.dll, XxxCoInstallEntryPoint", \
    "YyyCoInstall.dll, YyyCoInstallEntryPoint"
                                         \\ add both to registry
```

Device-specific co-installers are registered during the process of installing a device, when the Coinstallers INF section is processed.
[SetupAPI](./setupapi.md) then calls the co-installers at each subsequent step of the installation process.
If more than one co-installer is registered for a device, SetupAPI calls them in the order in which they are listed in the registry.
