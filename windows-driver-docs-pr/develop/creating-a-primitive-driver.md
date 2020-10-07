---
title: Creating a primitive driver
description: Use a primitive driver to handle and manage software that uses INF-based installation but are not necessarily tied to a particular hardware device.
ms.date: 04/16/2019
ms.localizationpriority: medium
ms.custom: 19H1
---

# Creating a new primitive driver

Use a primitive driver to handle and manage software that uses INF-based installation but are not necessarily tied to a particular hardware device.

## Background and benefits of primitive drivers

Prior to Windows 10 version 1903, certain types of software that used INF-based installation but were not necessarily tied to a particular hardware device were not fully supported by the OS. While these pieces of software used INF files as a manifest for installation, the OS was not directly aware of this scenario and did not have support to handle it natively.

Because these pieces of software were not tied to a hardware device, they would install on the whole system regardless of hardware. As a result, there was no guarantee that these pieces of software were properly installed, uninstalled, or handled on OS upgrade.

To improve reliability and guarantee proper behavior of these types of software, especially during OS upgrade and reset scenarios, the Plug and Play platform--starting with Windows 10 version 1903--now handles and manages this type of software package as a top-level entity.

The types of software that leverage this new platform support are called **primitive drivers.** Primitive drivers continue to use INF-based installation and the underlying platform makes use of the [Driver Store](../install/driver-store.md) to keep track of all relevant files.

The underlying Plug and Play platform then gracefully installs, uninstalls, and maintains driver state on OS upgrade.

Conceptually, these INFs are managed differently. Previously, \[DefaultInstall\] (and often, \[DefaultUninstall\]) were processed by [SetupAPI](../install/setupapi.md) in a script-like fashion, where the INF was used as a manifest and [SetupAPI](../install/setupapi.md) executed the instructions in the relevant sections on the caller's behalf.

Undoing the changes (to perform an uninstallation) required specifying an INF section that performed the opposite set of instructions as the installation section. INF-leveraging primitive drivers, however, do not require an uninstallation section.

Primitive drivers use the same installation and uninstallation APIs as device drivers, where the uninstallation API will perform the inverse set of operations as the install operation, and the act of installing or uninstalling the driver package will process those sections.

## INF requirements to access primitive driver functionality

* The **Version** section must be complete, just like PnP drivers.

  * The **Provider** directive must be filled in.

  * The **Class** directive must be filled in.

  * The **ClassGuid** directive must be filled in.

* The driver must be [DCH-Compliant](dch-principles-best-practices.md).

* No \[Manufacturer\] section may be present.

* \[DefaultInstall\] sections must be architecture decorated, and no undecorated versions may be present.

  * **Correct:** \[DefaultInstall.amd64\]

  * **Incorrect:** \[DefaultInstall\]

* \[DefaultUninstall\] may not be present in the INF (see [legacy compatibility](#legacy-compatibility) for an exception).

## Primitive drivers targeting only Windows 10 version 1903 and later

Primitive drivers targeted only for Windows 10 version 1903 and later should use [DiInstallDriver](/windows/win32/api/newdev/nf-newdev-diinstalldriverw) and [DiUninstallDriver](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw) to properly install and uninstall their software in/from the driver store.

Drivers should also use Dirid 13 to properly specify the Driver Store as the desired destination to be installed. For more information about Dirids, see [Using Dirids](../install/using-dirids.md).

## Legacy Compatibility

While \[DefaultUninstall\] is prohibited in Primitive Drivers, an exception is made for the sake of down-level OS compatibility. Windows introduces an INF directive that causes an OS version that supports Primitive Drivers to ignore the \[DefaultUninstall\] section. If your driver package needs to support down-level OS versions, include the following syntax to ensure that the platform will appropriately handle such cases:

```INF
[DefaultUninstall.NTamd64]
LegacyUninstall=1
```

The \[DefaultInstall\] and \[DefaultUninstall\] sections **must still be architecture decorated**; however, by including the `LegacyUninstall=1`, Windows ignores the \[DefaultUninstall\] section (in Windows 10 version 1903 and later). By doing so, you can include that section in your INF, where it can be used down-level with a legacy install/uninstall application in order to uninstall the primitive driver package.

Beginning with Windows 10 version 1903, if you pass an architecture-decorated \[DefaultInstall\] or
\[DefaultUninstall\] section in to the [InstallHInfSection](/windows/win32/api/setupapi/nf-setupapi-installhinfsectionw) API in setupapi.dll, the driver package will be checked to determine if it supports primitive driver functionality. If it does support primitive driver functionality, rather than process the specified section in the legacy way, the INF is passed to [DiInstallDriver](/windows/win32/api/newdev/nf-newdev-diinstalldrivera) or [DiUninstallDriver](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw), as appropriate. 
This way, a single installer can make use of primitive drivers on compatible OS versions and maintain support for previous OS versions.

## Converting from a device driver INF

Converting an INF that uses \[Manufacturer\] to one that uses \[DefaultInstall\] requires minor changes to the INF. Unlike a \[Manufacturer\] section, a \[DefaultInstall\] section is both an entry point and an install section. This conceptually combines the \[Manufacturer\], \[Models\], and \[DDInstall\] section into one.

Consider the following device driver INF:

```ini
[Manufacturer]
%Company% = Driver, NTx86, NTamd64

[Driver.NTx86]
%DeviceDesc% = InstallSection_32,

[Driver.NTamd64]
%DeviceDesc% = InstallSection_64,

[InstallSection_64]
CopyFiles = MyCopyFiles_64
AddReg = MyAddReg

[InstallSection_64.Services]
AddService = MyService,, MyService_Install

[InstallSection_32]
CopyFiles = MyCopyFiles_x86
AddReg = MyAddReg

[InstallSection_32.Services]
AddService = MyService,, MyService_Install
```

This INF will receive an 1297 error in [InfVerif](../devtest/infverif.md) because it doesn't install on any hardware. This INF can be converted to a \[DefaultInstall\]-based INF, as shown below.

```ini
[DefaultInstall.NTamd64]
CopyFiles = MyCopyFiles_64
AddReg = MyAddReg

[DefaultInstall.NTamd64.Services]
AddService = MyService,, MyService_Install

[DefaultInstall.NTx86]
CopyFiles = MyCopyFiles_x86
AddReg = MyAddReg

[DefaultInstall.NTx86.Services]
AddService = MyService,, MyService_Install
```