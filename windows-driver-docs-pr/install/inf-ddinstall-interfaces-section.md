---
title: INF DDInstall.Interfaces Section
description: A per-Models DDInstall.Interfaces section can have one or more AddInterface directives, depending on how many device interfaces a particular device/driver supports.
keywords:
- INF DDInstall.Interfaces Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DDInstall.Interfaces section
api_type:
- NA
ms.date: 06/02/2022
---

# INF DDInstall.Interfaces Section

Each per-Models ,DDInstall_**.Interfaces** section can have one or more [**AddInterface**](inf-addinterface-directive.md) directives, depending on how many device interfaces a particular device/driver supports.

```inf
[install-section-name.Interfaces] |
[install-section-name.nt.Interfaces] | 
[install-section-name.ntx86.Interfaces] |
[install-section-name.ntia64.Interfaces] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64.Interfaces] | (Windows XP and later versions of Windows)
[install-section-name.ntarm.Interfaces] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.Interfaces] (Windows 10 version 1709 and later versions of Windows)
 
AddInterface={InterfaceClassGUID} [, [reference string] [,[add-interface-section] [,flags]]] ...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

To support existing device interfaces, such as any of the system's predefined kernel-streaming interfaces, specify the appropriate *InterfaceClassGUID* values in this section.

To install a component, such as a class driver, that exports a new class of device interfaces, an INF must also have an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

For more information about device interfaces, see [Device Interface Classes](./overview-of-device-interface-classes.md).

## Entries

**AddInterface={**_InterfaceClassGUID_**}** [,[_reference string_] [,[_add-interface-section_] [,,flags_]]]...  
This directive installs support for a device interface class, designated by the specified *InterfaceClassGUID* value that the driver exports to higher level components. Usually, it also references an INF-writer-defined *add-interface-section* elsewhere in the INF file. For detailed information about how to specify this directive, see [**INF AddInterface Directive**](inf-addinterface-directive.md).

**Include=**,_filename_.**inf**[,_filename2_.**inf**]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to register the interface classes supported by this device/driver. If this entry is specified, usually so is a **Needs** entry.

**Needs=**,_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies the particular sections that must be processed during the installation of this device. Typically, such a named section is a ,DDInstall_**.Interfaces** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a ,DDInstall_**.Interfaces** section of the included INF.

## Remarks

The _DDInstall_ section name must be referenced by a device/models-specific entry under the per-manufacturer _Models_ section of the INF file. For information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions in cross-platform INF files, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

If a specified **{**,InterfaceClassGUID_**}** is not installed already, the operating system's setup code installs that device interface class in the system. If an INF file installs one or more new device interface classes, it can also have an **[InterfaceInstall32]** section identifying the GUID for the new class.

For more information about how to create a GUID, see [Using GUIDs in Drivers](../kernel/using-guids-in-drivers.md). For the system-defined interface class GUIDs, see the appropriate system-supplied header, such as *Ks.h* for the kernel-streaming interface class GUIDS.

When a driver is loaded, it must call [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) with the same **{**,InterfaceClassGUID_**}** and *reference string* used in an **AddInterface** directive in order to get the full *SymbolicLinkName* for the device interface. It must do this for each device interface in the INF's ,DDInstall_**.Interfaces** section that the driver supports on the underlying device.  For each *SymbolicLinkName*, the driver must call [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate) to enable the device interface. Usually, a PnP function or filter driver makes these calls from its [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine.

## Examples

This example shows the _DDInstall_.**nt.Interfaces** section in the INF file for the system-supplied WDM audio device/driver.

```inf
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

[**_DDInstall_**](inf-ddinstall-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface)

[**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate)

[**_Models_**](inf-models-section.md)
