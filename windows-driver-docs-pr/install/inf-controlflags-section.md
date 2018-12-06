---
title: INF ControlFlags Section
description: A ControlFlags section identifies devices for which Windows should take certain unique actions during installation.
ms.assetid: 529060b6-ee4b-49a8-b723-5eda47e9f561
keywords:
- INF ControlFlags Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF ControlFlags Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF ControlFlags Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **ControlFlags** section identifies devices for which Windows should take certain unique actions during installation.

```cpp
[ControlFlags]

ExcludeFromSelect=* | 
ExcludeFromSelect=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.nt=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.ntx86=device-identification-string[,device-identification-string] ...] | 
[ExcludeFromSelect.ntia64=device-identification-string[,device-identification-string] ...]  |  (Windows XP and later versions of Windows)
[ExcludeFromSelect.ntamd64=device-identification-string[,device-identification-string] ...]  |  (Windows XP and later versions of Windows)
[CopyFilesOnly=device-identification-string[,device-identification-string] ...]
[InteractiveInstall=device-identification-string[,device-identification-string] ... ]
[RequestAdditionalSoftware=*] | 
[RequestAdditionalSoftware=device-identification-string[,device-identification-string] ...]  (Windows 7 and later versions of Windows)
```

## Entries


<a href="" id="device-identification-string"></a>*device-identification-string*  
Identifies a [hardware ID](hardware-ids.md) or [compatible ID](compatible-ids.md) that was specified in a per-manufacturer [**INF Models section**](inf-models-section.md). Each string must be separated from the next with a comma (,).

<a href="" id="excludefromselect"></a>**ExcludeFromSelect**  
Removes all (if \* is specified) or the specified list of devices from certain user interface displays, from which a user is expected to select a particular device for installation.

For Windows 2000 and later versions of Windows, the specified devices are displayed by the Found New Hardware Wizard and the Hardware Update Wizard.

To exclude a set of OS-incompatible or platform-incompatible devices from this display, one or more **ExcludeFromSelect** entries can have the following case-insensitive extensions appended:

<a href="" id="-nt"></a>**.nt**  
Do not display these devices on computers that are running Windows 2000 or later versions of Windows.

<a href="" id="-ntx86-"></a>**.ntx86**   
Do not display these devices on x86-based computers that are running Windows 2000 or later versions of Windows.

<a href="" id="-ntia64--"></a>**.ntia64**   
Do not display these devices on Itanium-based computers that are running Windows XP or later versions of Windows.

<a href="" id="-ntamd64"></a>**.ntamd64**  
Do not display these devices on x64-based computers that are running Windows XP or later versions of Windows.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

<a href="" id="copyfilesonly"></a>**CopyFilesOnly**  
Installs only the INF-specified files for the given devices because the device hardware is not accessible or available yet.

This entry is rarely used. However, it can be used to preinstall the drivers of a device for which the card will later be seated in a particular slot that is currently in use. For example, if a device currently seated in the particular slot is necessary to transfer INF-specified files to the target, the INF would have this entry.

<a href="" id="interactiveinstall"></a>**InteractiveInstall**  
Forces the specified list of devices to be installed in a user's context. Each line can specify one or more hardware IDs or compatible IDs, and there can be one or more lines.

This entry is optional. The preferred way to install devices is to omit this entry and allow Windows to install the device in the context of a trusted system thread, if possible. However, if a device absolutely requires a user to be logged in when the device is installed, include this entry in the device INF.

<a href="" id="requestadditionalsoftware"></a>**RequestAdditionalSoftware**  
Specifies that all (if **\\*** is specified) or the specified list of devices may require additional software than what was installed through the [driver package](driver-packages.md) for the device. For example, the **RequestAdditionalSoftware** entry can be used to install new or updated device-specific software that was not included in the driver package.

**Note**  If **\\*** is not specified, each device specified by a **RequestAdditionalSoftware** entry must be defined within the [**INF Models section**](inf-models-section.md).

 

This entry is optional, and is supported in Windows 7 and later versions of Windows operating system.

After Windows installs the [driver package](driver-packages.md) for the device, the Plug and Play (PnP) manager performs the following steps if the **RequestAdditionalSoftware** entry is specified within the INF file:

1.  The PnP manager generates a Problem Report and Solution (PRS) error report with the type of **RequestAddtionalSoftware**. This report contains information about the specific hardware ID of the device and the system architecture of the computer.
2.  If there is a solution provided by the independent hardware vendor (IHV) for the device-specific software, the solution is downloaded to the computer.

    **Note**  The download of the solution does not install the software itself.

     

3.  If the device-specific software is not installed on the computer, the PnP manager presents the solution to the user and provides a link for downloading the software. The user can then choose to download and install this software by following the instructions presented in the solution.

Remarks
-------

Typically, a **ControlFlags** section has one or more **ExcludeFromSelect** entries to identify devices that are listed in the per-manufacturer [**INF Models section**](inf-models-section.md), but which should not be displayed to the end-user as options during manual installations.

Listing a device's [hardware ID](hardware-ids.md) or [compatible ID](compatible-ids.md) in an **ExcludeFromSelect** entry removes it from the display shown to the end-user. Specifying an asterisk (\*) for the **ExcludeFromSelect** value removes all devices/models defined in the INF file from this user-visible list.

An INF writer should use the **InteractiveInstall** directive sparingly and only in the following situations:

-   To install drivers for devices that have corrupted or otherwise incorrectly defined hardware IDs. For example, when two or more different devices share the same Hardware ID. This case is strictly forbidden by the Plug and Play standard, but some hardware vendors have made this error in hardware.
-   To install drivers for devices that require their own driver and absolutely cannot use the generic class driver or another driver supplied with the operating system. The **InteractiveInstall** entry forces Device Manager to ask the user for confirmation for compatible ID matches.

**Note**  In the future, WHQL might not grant the Windows Logo to devices whose INF files include **InteractiveInstall** entries.

 

INF files that exclusively install PnP devices can have a **ControlFlags** section unless they set the **NoInstallClass** value entry in their respective *SetupClassGUID* registry keys to **TRUE**. For more information about these registry keys, see [**INF ClassInstall32 Section**](inf-classinstall32-section.md).

Examples
--------

This example of the **ControlFlags** section in the system mouse class installer INF suppresses the display of devices/models that cannot be installed on x86 platforms.

```cpp
[ControlFlags]
; Exclude all bus mice and InPort mice for x86 platforms
ExcludeFromSelect.ntx86=*PNP0F0D,*PNP0F11,*PNP0F00,*PNP0F02,*PNP0F15
; Hide this entry always
ExcludeFromSelect=UNKNOWN_MOUSE
```

The following INF file fragment shows two devices: one that is fully PnP-capable and requires no user intervention during installation and another that requires its own driver and cannot use any other driver. Specifying **InteractiveInstall** for the second device forces Windows to install this device in a user's context (a user who has administrative rights). This includes prompting the user for the location of the driver files (INF file, driver file, and so on) as required.

```cpp
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

[***Models***](inf-models-section.md)

 

 






