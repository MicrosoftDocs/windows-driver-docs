---
title: Operating System Upgrades
description: Operating System Upgrades
ms.assetid: f985967e-e6cf-431a-bb7e-7b6d8486709c
keywords:
- audio adapters WDK , operating system upgrades
- adapter drivers WDK audio , operating system upgrades
- Port Class audio adapters WDK , operating system upgrades
- preserving audio settings WDK audio
- migration DLL WDK audio
- migrating settings WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operating System Upgrades


## <span id="operating_system_upgrades"></span><span id="OPERATING_SYSTEM_UPGRADES"></span>


An audio device's driver and registry settings can frequently be preserved across operating system upgrades. The discussion below presents some guidelines for accomplishing this.

### <span id="Preserving_Audio_Settings"></span><span id="preserving_audio_settings"></span><span id="PRESERVING_AUDIO_SETTINGS"></span>Preserving Audio Settings

An audio adapter driver can keep track of its current device settings--chiefly volume levels and mute settings--in the system registry. The driver typically stores these settings in the system-supplied driver key (represented by the INF keyword HKR) under the subkey "Settings". When the user alters these settings through a control panel or other audio application, the driver updates the appropriate registry entries. Each time the system boots, the driver restores the device settings from the registry.

When upgrading from Windows Me/98 to Windows XP or Windows 2000, the Windows installation program is unable to preserve these settings.

However, when upgrading from Windows 98 to Windows Me, or from one NT-based operating system to another (for example, from Windows 2000 to Windows XP), the installation program leaves the driver's existing registry settings intact. Users largely prefer this behavior because it preserves the adjustments they have made to the system over time instead of forcing them to try to restore their settings manually each time they upgrade the operating system.

Some proprietary drivers, however, blindly overwrite these registry settings with defaults each time they are installed. A better approach is for a driver to determine at installation time whether certain driver-specific registry entries already exist. If they do exist, the driver should preserve the settings that are contained in these entries instead of overwriting them.

The directives in the add-registry section of the driver's INF file specify whether existing registry entries should be overwritten. For more information, see the description of the FLG\_ADDREG\_NOCLOBBER flag in [**INF AddReg Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320).

### <span id="Migration_DLL"></span><span id="migration_dll"></span><span id="MIGRATION_DLL"></span>Migration DLL

During an upgrade from Windows Me/98 to an NT-based operating system (Windows 2000 and later), the Windows installation program treats a device driver that was installed under Windows Me/98 as incompatible and discards both the driver and its registry settings.

In addition, if the Windows 2000 setup program finds no in-box driver support for the device, the program immediately prompts the user to provide the driver software. In Windows XP and later, if the setup program is unable to find a suitable driver either in-box or at the Windows Update site, it waits until the upgrade has completed to inform the user of the missing driver.

Although a driver cannot avoid the loss of its registry settings during such an upgrade, Microsoft recommends the use of a migration DLL to reinstall a compatible driver transparently to the user. For this purpose, Microsoft provides the Devupgrd migration DLL, which is included in the Setup Plug and Play samples in the Windows Driver Kit (WDK). The sample includes a help file that describes the migration DLL.

The migration DLL should be used only with WDM drivers that are initially installed under Windows Me/98 but are also capable of running on Windows 2000 or Windows XP. Note that the migration DLL cannot upgrade drivers from Windows Me/98 to Windows Server 2003, Windows Vista, or later. It can only upgrade drivers from Windows Me/98 to Windows XP or Windows 2000.

During the upgrade from Windows Me/98 to Windows XP or Windows 2000, the migration DLL does the following:

-   Reads the device driver's migration information from its location in the Windows Me/98 registry.

-   Adds the necessary information to the driver's INF file to ensure that the device installs properly under Windows XP or Windows 2000.

To make the migration information available later to the Windows XP or Windows 2000 setup program, the INF file that installs the device under Windows Me/98 should do the following:

-   Copy the migration DLL to an INF-specified backup directory and add that directory's path name to the Windows Me/98 registry.

-   Add to the registry the device IDs that identify the devices that can migrate.

-   Save backup copies of the device driver files (.sys and .inf) into INF-specified backup directories and add those directories' path names to the registry.

During the upgrade, the Windows XP or Windows 2000 setup program adds the backup directory names to the INF search path for the registered device IDs.

As discussed above, the setup program discards the driver's registry settings during an upgrade from Windows Me/98 to Windows XP or Windows 2000. The driver reinstallation that is performed with the help of a migration DLL is a "clean install" in which the driver's volume, mute, and other settings assume their initial, default values.

The Ac97 audio adapter sample in the Windows Driver Kit (WDK) contains an example of an INF file (Ac97smpl.inf) that migrates an audio driver from Windows Me/98 to Windows XP or Windows 2000.

 

 




