---
title: INF ControlFlags Section
description: A ControlFlags section identifies devices for which Windows should take certain unique actions during installation.
keywords:
- INF ControlFlags Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF ControlFlags Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF ControlFlags section

A **ControlFlags** section identifies devices for which Windows should take certain unique actions during installation.

```inf
[ControlFlags]

ExcludeFromSelect=* | 
ExcludeFromSelect=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.nt=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.ntx86=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.ntia64=device-identification-string[,device-identification-string] ...]  |  (Windows XP and later versions of Windows)
[ExcludeFromSelect.ntamd64=device-identification-string[,device-identification-string] ...]  |  (Windows XP and later versions of Windows)
[ExcludeFromSelect.ntarm=device-identification-string[,device-identification-string] ...]  |  (Windows 8 and later versions of Windows)
[ExcludeFromSelect.ntarm64=device-identification-string[,device-identification-string] ...]  |  (Windows 10 version 1709 and later versions of Windows)

[CopyFilesOnly=device-identification-string[,device-identification-string] ...]
[InteractiveInstall=device-identification-string[,device-identification-string] ... ]
[RequestAdditionalSoftware=*] | 
[RequestAdditionalSoftware=device-identification-string[,device-identification-string] ...]  (Windows 7 through Windows 10 version 1709)
```

## Entries

_device-identification-string_  
Identifies a [hardware ID](hardware-ids.md) or [compatible ID](compatible-ids.md) that was specified in a per-manufacturer [**INF Models section**](inf-models-section.md). Each string must be separated from the next with a comma (,).

**ExcludeFromSelect**  
Removes all (if * is specified) or the specified list of devices from certain user interface displays, from which a user is expected to select a particular device for installation.

For Windows 2000 and later versions of Windows, the specified devices are displayed by the Found New Hardware Wizard and the Hardware Update Wizard.

To exclude a set of OS-incompatible or platform-incompatible devices from this display, one or more **ExcludeFromSelect** entries can have the following case-insensitive extensions appended:

**.nt**  
Do not display these devices on computers that are running Windows 2000 or later versions of Windows.

**.ntx86**  
Do not display these devices on x86-based computers that are running Windows 2000 or later versions of Windows.

**.ntia64**  
Do not display these devices on Itanium-based computers that are running Windows XP or later versions of Windows.

**.ntamd64**  
Do not display these devices on x64-based computers that are running Windows XP or later versions of Windows.

**.ntarm**  
Do not display these devices on Arm-based computers that are running Windows 8 or later versions of Windows.

**.ntarm64**  
Do not display these devices on Arm64-based computers that are running Windows 10 version 1709 or later versions of Windows.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

**CopyFilesOnly**  
Installs only the INF-specified files for the given devices because the device hardware is not accessible or available yet.

This entry is rarely used. However, it can be used to preinstall the drivers of a device for which the card will later be seated in a particular slot that is currently in use. For example, if a device currently seated in the particular slot is necessary to transfer INF-specified files to the target, the INF would have this entry.

**InteractiveInstall**  
Forces the specified list of devices to be installed in a user's context. Each line can specify one or more hardware IDs or compatible IDs, and there can be one or more lines.

This entry is optional. The preferred way to install devices is to omit this entry and allow Windows to install the device in the context of a trusted system thread, if possible. However, if a device absolutely requires a user to be logged in when the device is installed, include this entry in the device INF.

**RequestAdditionalSoftware**  
Specifies that all (if * is specified) or the specified list of devices may require additional software than what was installed through the [driver package](driver-packages.md) for the device. For example, the **RequestAdditionalSoftware** entry can be used to install new or updated device-specific software that was not included in the driver package.

> [!NOTE]
> If * is not specified, each device specified by a **RequestAdditionalSoftware** entry must be defined within the [**INF Models section**](inf-models-section.md).

This entry is optional, and is supported in Windows 7 through Windows 10 version 1709.

After Windows installs the [driver package](driver-packages.md) for the device, the Plug and Play (PnP) manager performs the following steps if the **RequestAdditionalSoftware** entry is specified within the INF file:

1. The PnP manager generates a Problem Report and Solution (PRS) error report with the type of **RequestAdditionalSoftware**. This report contains information about the specific hardware ID of the device and the system architecture of the computer.

1. If there is a solution provided by the independent hardware vendor (IHV) for the device-specific software, the solution is downloaded to the computer.

    > [!NOTE]
    > The download of the solution does not install the software itself.

1. If the device-specific software is not installed on the computer, the PnP manager presents the solution to the user and provides a link for downloading the software. The user can then choose to download and install this software by following the instructions presented in the solution.

## Remarks

Typically, a **ControlFlags** section has one or more **ExcludeFromSelect** entries to identify devices that are listed in the per-manufacturer [**INF Models section**](inf-models-section.md), but which should not be displayed to the end-user as options during manual installations.

Listing a device's [hardware ID](hardware-ids.md) or [compatible ID](compatible-ids.md) in an **ExcludeFromSelect** entry removes it from the display shown to the end-user. Specifying an asterisk (\*) for the **ExcludeFromSelect** value removes all devices/models defined in the INF file from this user-visible list.

An INF writer should use the **InteractiveInstall** directive sparingly and only in the following situations:

- To install drivers for devices that have corrupted or otherwise incorrectly defined hardware IDs. For example, when two or more different devices share the same Hardware ID. This case is strictly forbidden by the Plug and Play standard, but some hardware vendors have made this error in hardware.
- To install drivers for devices that require their own driver and absolutely cannot use the generic class driver or another driver supplied with the operating system. The **InteractiveInstall** entry forces Device Manager to ask the user for confirmation for compatible ID matches.

> [!NOTE]
> In the future, WHQL might not grant the Windows Logo to devices whose INF files include **InteractiveInstall** entries.

INF files that exclusively install PnP devices can have a **ControlFlags** section unless they set the **NoInstallClass** value entry in their respective device setup class GUID settings to **TRUE**. For more information about these settings, see [**INF ClassInstall32 Section**](inf-classinstall32-section.md).

## Examples

This example of the **ControlFlags** section in the system mouse class INF suppresses the display of devices/models that cannot be installed on x86 platforms.

```inf
[ControlFlags]
; Exclude all bus mice and InPort mice for x86 platforms
ExcludeFromSelect.ntx86=*PNP0F0D,*PNP0F11,*PNP0F00,*PNP0F02,*PNP0F15
; Hide this entry always
ExcludeFromSelect=UNKNOWN_MOUSE
```

The following INF file fragment shows two devices: one that is fully PnP-capable and requires no user intervention during installation and another that requires its own driver and cannot use any other driver. Specifying **InteractiveInstall** for the second device forces Windows to install this device in a user's context (a user who has administrative rights). This includes prompting the user for the location of the driver files (INF file, driver file, and so on) as required.

```inf
; ...
[Manufacturer]
%Mfg% = ModelsSection

[ModelsSection]
; Models section, with two entries
%Device1.DeviceDesc% = Device1.Install, \
    PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_01
%Device2.Device.Desc%= Device2.Install, \
    PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02

[ControlFlags]
InteractiveInstall = \
  PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02
; ...
```

## See also

[**ClassInstall32**](inf-classinstall32-section.md)

[**Manufacturer**](inf-manufacturer-section.md)

[**_Models_**](inf-models-section.md)
