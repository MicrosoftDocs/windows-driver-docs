---
title: INF DDInstall.Interfaces Section
description: A per-Models DDInstall.Interfaces section can have one or more AddInterface directives, depending on how many device interfaces a particular device/driver supports.
ms.assetid: 16904119-00a4-45d7-a32e-24ba4c8a3416
keywords:
- INF DDInstall.Interfaces Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.Interfaces Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.Interfaces Section


Each per-Models <em>DDInstall</em>**.Interfaces** section can have one or more [**AddInterface**](inf-addinterface-directive.md) directives, depending on how many device interfaces a particular device/driver supports.

```cpp
[install-section-name.Interfaces] |
[install-section-name.nt.Interfaces] | 
[install-section-name.ntx86.Interfaces] |
[install-section-name.ntarm.Interfaces] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.Interfaces] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.Interfaces] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.Interfaces]  (Windows XP and later versions of Windows)
 
AddInterface={InterfaceClassGUID} [, [reference string] [,[add-interface-section] [,flags]]] ...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

To support existing device interfaces, such as any of the system's predefined kernel-streaming interfaces, specify the appropriate *InterfaceClassGUID* values in this section.

To install a component, such as a class driver, that exports a new class of device interfaces, an INF must also have an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

For more information about device interfaces, see [Device Interface Classes](device-interface-classes.md).

## Entries


<a href="" id="addinterface--interfaceclassguid------reference-string-----add-interface-section----flags-------"></a>**AddInterface={**<em>InterfaceClassGUID</em>**}** \[**,** \[*reference string*\] \[**,**\[*add-interface-section*\] \[**,**<em>flags</em>\]\]\] ...  
This directive installs support for a device interface class, designated by the specified *InterfaceClassGUID* value that the driver exports to higher level components. Usually, it also references an INF-writer-defined *add-interface-section* elsewhere in the INF file. For detailed information about how to specify this directive, see [**INF AddInterface Directive**](inf-addinterface-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to register the interface classes supported by this device/driver. If this entry is specified, usually so is a **Needs** entry.

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
This optional entry specifies the particular sections that must be processed during the installation of this device. Typically, such a named section is a <em>DDInstall</em>**.Interfaces** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a <em>DDInstall</em>**.Interfaces** section of the included INF.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

Remarks
-------

The *DDInstall* section name must be referenced by a device/models-specific entry under the per-manufacturer *Models* section of the INF file. For information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions in cross-platform INF files, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

If a specified **{**<em>InterfaceClassGUID</em>**}** is not installed already, the operating system's setup code installs that device interface class in the system. If an INF file installs one or more new device interface classes, it also has an **\[InterfaceInstall32\]** section identifying the GUID for the new class..

For more information about how to create a GUID, see [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392). For the system-defined interface class GUIDs, see the appropriate system-supplied header, such as *Ks.h* for the kernel-streaming interface class GUIDS.

When a driver is loaded, it must call [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700) once for each **{**<em>InterfaceClassGUID</em>**}** value specified in the INF's <em>DDInstall</em>**.Interfaces** section that the driver supports on the underlying device, to enable the interface for run-time use by higher level components. Instead of registering support for a device interface in an INF, a device driver can call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) before making its initial call to **IoSetDeviceInterfaceState**. Usually, a PnP function or filter driver makes this call from its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.

Examples
--------

This example shows the <em>DDInstall</em>**.nt.Interfaces** section in the INF file for the system-supplied WDM audio device/driver shown as examples for the [**INF *DDInstall* section**](inf-ddinstall-section.md) and the [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md) .

```cpp
;
; following AddInterface= are all single lines (without 
; backslash line continuators) in the system-supplied INF file
;
[WDMPNPB003_Device.NT.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Wave%,\
  WDM_SB16.Interface.Wave
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Topology%,\
  WDM_SB16.Interface.Topology
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_UART%,\
  WDM_SB16.Interface.UART
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_FMSynth%,\
  WDM_SB16.Interface.FMSynth
; ...

[Strings] ; only immediately preceding %strkey% tokens shown here
%KSCATEGORY_AUDIO% = "{6994ad04-93ef-11d0-a3cc-00a0c9223196}"
KSNAME_Wave = "Wave"
KSNAME_UART = "UART"
KSNAME_FMSynth = "FMSynth" 
KSNAME_Topology = "Topology"
; ...
```

## See also


[**AddInterface**](inf-addinterface-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)

[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)

[***Models***](inf-models-section.md)

 

 






