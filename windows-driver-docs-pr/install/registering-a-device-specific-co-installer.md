---
title: Registering a Device-Specific Co-installer
description: Registering a Device-Specific Co-installer
ms.assetid: 7a80bc60-e2f0-4447-bd73-4ce12fcfc2e3
keywords:
- device-specific co-installers WDK device installations
- registering device-specific co-installers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering a Device-Specific Co-installer





To register a device-specific co-installer, add the following sections to the device's INF file:

```cpp
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

The entry in the **DestinationDirs** section specifies that files listed in the *Xxx*CopyFilesSection will be copied to the system directory. The *Xxx* prefix identifies the driver, the device, or a group of devices (for example, cdrom_CopyFilesSection). The *Xxx* prefix should be unique.

The *install-section-name* entry for the co-installer can be decorated with an optional OS/architecture extension (for example, cdrom_install.NTx86.CoInstallers). For more information, see [**INF *DDInstall* Section**](inf-ddinstall-section.md).

The entry in the <em>Xxx</em>**_AddReg** section creates a **CoInstallers32** value entry in the device's [*driver key*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-key). The entry contains the co-installer DLL and, optionally, a specific entry point. If you omit the entry point, the default is CoDeviceInstall. The hexadecimal flags parameter (0x00010000) specifies that this is a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) value entry.

To register more than one device-specific co-installer for a device, copy the files for each co-installer and include more than one string in the registry entry. For example, to register two co-installers, create INF sections like the following:

```cpp
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

Device-specific co-installers are registered during the process of installing a device, when the Coinstallers INF section is processed. SetupAPI then calls the co-installers at each subsequent step of the installation process. If more than one co-installer is registered for a device, SetupAPI calls them in the order in which they are listed in the registry.

 

 





