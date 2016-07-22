---
title: Registering a Device-Specific Co-installer
description: Registering a Device-Specific Co-installer
ms.assetid: 7a80bc60-e2f0-4447-bd73-4ce12fcfc2e3
keywords: ["device-specific co-installers WDK device installations", "registering device-specific co-installers"]
---

# Registering a Device-Specific Co-installer


## <a href="" id="ddk-registering-a-device-specific-co-installer-dg"></a>


To register a device-specific co-installer, add the following sections to the device's INF file:

```
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

The entry in the **DestinationDirs** section specifies that files listed in the *Xxx*CopyFilesSection will be copied to the system directory. The *Xxx* prefix identifies the driver, the device, or a group of devices (for example, cdrom\_CopyFilesSection). The *Xxx* prefix should be unique.

The *install-section-name* entry for the co-installer can be decorated with an optional OS/architecture extension (for example, cdrom\_install.NTx86.CoInstallers). For more information, see [**INF *DDInstall* Section**](inf-ddinstall-section.md).

The entry in the *Xxx***\_AddReg** section creates a **CoInstallers32** value entry in the device's [*driver key*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-key). The entry contains the co-installer DLL and, optionally, a specific entry point. If you omit the entry point, the default is CoDeviceInstall. The hexadecimal flags parameter (0x00010000) specifies that this is a REG\_MULTI\_SZ value entry.

To register more than one device-specific co-installer for a device, copy the files for each co-installer and include more than one string in the registry entry. For example, to register two co-installers, create INF sections like the following:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Registering%20a%20Device-Specific%20Co-installer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




