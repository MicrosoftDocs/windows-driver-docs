---
title: INF DDInstall Section
description: Each per-Models DDInstall section contains an optional DriverVer directive and one or more directives referencing additional named sections in the INF file, shown here with the most frequently specified INF directives, CopyFiles and AddReg, listed first.
keywords:
- INF DDInstall Section Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF DDInstall Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF DDInstall section

Each per-Models _DDInstall_ section contains an optional **DriverVer** directive and one or more directives referencing additional named sections in the INF file, shown here with the most frequently specified INF directives, **CopyFiles** and **AddReg**, listed first.

The sections referenced by these directives contain instructions for installing driver files and writing any device-specific and/or driver-specific information into the registry.

```inf
[install-section-name] | 
[install-section-name.nt] | 
[install-section-name.ntx86] | 
[install-section-name.ntia64] | (Windows XP and later versions of Windows)
[install-section-name.ntamd64] | (Windows XP and later versions of Windows)
[install-section-name.ntarm] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64] (Windows 10 version 1709 and later versions of Windows)

[DriverVer=mm/dd/yyyy[,x.y.v.z]]
[CopyFiles=@filename | file-list-section[,file-list-section] ...]
[CopyINF=filename1.inf[,filename2.inf]...] (Windows XP and later versions of Windows)
[AddReg=add-registry-section[,add-registry-section]...]
[AddProperty=add-property-section[,add-property-section]...] (Windows Vista and later versions of Windows)
[Include=filename1.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[Delfiles=file-list-section[,file-list-section]...]
[Renfiles=file-list-section[,file-list-section]...]
[DelReg=del-registry-section[,del-registry-section]...]
[DelProperty=del-property-section[,del-property-section]...] (Windows Vista and later versions of Windows)
[FeatureScore=featurescore]... (Windows Vista and later versions of Windows)
[BitReg=bit-registry-section[,bit-registry-section]...]
[LogConfig=log-config-section[,log-config-section]...]
[ProfileItems=profile-items-section[,profile-items-section]...] (Windows 2000 and later versions of Windows)
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
[RegisterDlls=register-dll-section[,register-dll-section]...]
[UnregisterDlls=unregister-dll-section[,unregister-dll-section]...]
[ExcludeID=device-identification-string[,device-identification-string]...]... ((Windows XP and later versions of Windows)
[Reboot]
```

## Entries

Not all valid entries are supported in a [Universal INF](using-a-universal-inf-file.md).  The following lists which directives are valid in a universal INF and which are not.

### Supported in a Universal INF

**DriverVer=**_mm/dd/yyyy_[,_x.y.v.z_]  
This optional entry specifies version information for the [driver package](driver-packages.md).

For information about how to specify this entry, see [**INF DriverVer Directive**](inf-driverver-directive.md).

**CopyFiles=@**_filename_ | _file-list-section_[,_file-list-section_] ...  
This directive either specifies one named file to be copied from the source media to the destination or references one or more INF-writer-defined sections in which device-relevant files on the source media are specified for transfer to the destination. The **CopyFiles** directive is optional, but is present in most _DDInstall_ sections.

The **DefaultDestDir** entry in the [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF specifies the destination for any single file to be copied. The [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections, or an additional INF specified in the **LayoutFile** entry of this INF's [**Version**](inf-version-section.md) section, provide the location on the distribution media of the driver files.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

**CopyINF=**_filename1_**.inf**[,_filename2_**.inf**]...  
(Windows XP and later) This directive causes specified INF files to be copied to the target system.

For more information, see [**INF CopyINF Directive**](inf-copyinf-directive.md).

**AddReg=**_add-registry-section_[,_add-registry-section_]...  
This directive references one or more INF-writer-defined sections in which new subkeys, possibly with initial value entries, are specified to be written into the registry or in which the value entries of existing keys are modified.

An **HKR** specification in such an add-registry section designates the ["software key"](opening-a-device-s-software-key.md) registry path of the device being installed.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

**AddProperty=**_add-property-section_[,_add-property-section_]...  
(Windows Vista and later) References one or more INF file sections that modify [device properties](device-properties.md) that are set for a device instance. You should use an [**INF AddProperty directive**](inf-addproperty-directive.md) only to set a device instance property that is new to Windows Vista or later versions of Windows operating systems.

For device instance properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) to set the device instance properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **AddProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

**Include=**_filename1_**.inf**[,_filename2_**.inf**]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device and/or driver. If this entry is specified, usually so is a **Needs** entry.

For example, INF files for device drivers that depend on the system's kernel-streaming support may specify this entry as follows:

```inf
Include= ks.inf, kscaptur.inf, ksfilter.inf
```

**Needs=**_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies sections within system-supplied INF files that must be processed during the installation of this device. Typically, such a named section is a _DDInstall_ (or _DDInstall_**.**_xxx_) section within one of the INF files that are listed in an **Include** entry. However, it can be any section that is referenced within such a _DDInstall_ or _DDInstall_**.**_xxx_ section of the included INF.

For example, INF files for device drivers that have the preceding **Include** entry may specify this entry as follows:

```inf
Needs= KS.Registration, KSCAPTUR.Registration.NT, MSPCLOCK.Installation
```

**FeatureScore=**_featurescore_  

> [!WARNING]
> The **FeatureScore** directive is only processed when specified directly in the **[DDInstall]** section.

(Windows Vista and later) This directive provides an additional ranking criterion for drivers that are based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](./overview-of-device-setup-classes.md) that distinguishes between drivers based on class-specific criteria.

For more information about how drivers are ranked, see [How Windows Ranks Drivers (Windows Vista and Later)](how-setup-ranks-drivers--windows-vista-and-later-.md).

For more information about this directive, see [**INF FeatureScore Directive**](inf-featurescore-directive.md).

> [!NOTE]
> Although a _DDInstall_ section can contain multiple **FeatureScore** entries, only the first entry is processed for the section.

**ExcludeID=**_device-identification-string_[,_device-identification-string_]...  

> [!WARNING]
> The **ExcludeID** directive is only processed when specified directly in the **[DDInstall]** section.

(Windows XP and later) This directive specifies one or more device identification strings (either [hardware IDs](hardware-ids.md) or [compatible IDs](compatible-ids.md)). The _DDInstall_ section does not install devices that have [device IDs](device-ids.md) that match any of the hardware IDs or compatible IDs listed.

**Reboot**  
This directive indicates that the caller should be prompted to reboot the system after installation is complete.

For more information, see [**INF Reboot Directive**](inf-reboot-directive.md).

### Not supported in a Universal INF

**Delfiles=**_file-list-section_[,_file-list-section_]...  
This directive references one or more INF-writer-defined sections listing files on the target to be deleted.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

**Renfiles=**_file-list-section_[,_file-list-section_]...  
This directive references one or more INF-writer-defined sections listing files to be renamed on the destination before device-relevant source files are copied to the target computer.

For more information, see [**INF RenFiles Directive**](inf-renfiles-directive.md).

**DelReg=**_del-registry-section_[,_del-registry-section_]...  
This directive references one or more INF-writer-defined sections in which keys and/or value entries are specified to be removed from the registry during installation of the devices.

Typically, this directive is used to handle upgrades when an INF must clean up old registry entries from a previous installation of this device.

An **HKR** specification in such a delete-registry section designates the ["software key"](opening-a-device-s-software-key.md) registry path of the device being installed.

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

**DelProperty=**_del-property-section_[,_del-property-section_]...  
(Windows Vista and later) References one or more INF file sections that delete [device properties](device-properties.md) that are set for a device instance. You should use an [**INF DelProperty directive**](inf-delproperty-directive.md) only to delete a device instance property that is new to Windows Vista or later versions of Windows.

For device instance properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF DelReg directives**](inf-delreg-directive.md) to delete the device instance properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

**BitReg=**_bit-registry-section_[,_bit-registry-section_]...  
This directive references one or more INF-writer-defined sections in which existing registry value entries of type [REG_BINARY](/windows/desktop/SysInfo/registry-value-types) are modified.

An **HKR** specification in such a bit-registry section designates the ["software key"](opening-a-device-s-software-key.md) registry path of the device being installed.

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

**LogConfig=**_log-config-section_[,_log-config-section_]...  
This directive references one or more INF-writer-defined sections within an INF for a root-enumerated device or for a manually installed device. In these named sections, the INF for such a "detected" or manually installed device specifies one or more logical configurations of bus-relative hardware resources that the device must have to be operational. The INF for such a manually installed device that is not software-configurable should also have a _DDInstall_**.FactDef** section.

The **LogConfig** directive is never used to install Plug and Play (PnP) devices. However, you can use an [**INF DDInstall.LogConfigOverride section**](inf-ddinstall-logconfigoverride-section.md) to provide an override configuration for PnP devices.

This directive is irrelevant to all higher-level (nondevice) drivers and components.

For more information, see [**INF LogConfig Directive**](inf-logconfig-directive.md).

**ProfileItems=**_profile-items-section_[,_profile-items-section_]...  
(Microsoft Windows 2000 and later versions of Windows) This rarely used directive references one or more INF-writer-defined sections that describe items to be added to, or removed from, the Start menu.

For more information, see [**INF ProfileItems Directive**](inf-profileitems-directive.md).

**UpdateInis=**_update-ini-section_[,_update-ini-section_]...  
This rarely used directive references one or more INF-writer-defined sections, specifying a source INI file from which a particular section or line within such a section is to be read into a destination INI file of the same name during installation. Optionally, line-by-line modifications to an existing INI file on the destination from a given source INI file of the same name can be specified in the update-ini section.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

**UpdateIniFields=**_update-inifields-section_[,_update-inifields-section_]...  
This rarely used directive references one or more INF-writer-defined sections in which modifications within the lines of a device-specific INI file are specified.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

**Ini2Reg=**_ini-to-registry-section_[,_ini-to-registry-section_]...  
This rarely used directive references one or more INF-writer-defined sections in which sections or lines from a device-specific INI file, supplied on the source media, are to be moved into the registry.

For more information, see [**INF Ini2Reg Directive**](inf-ini2reg-directive.md).

**RegisterDlls=**_register-dll-section_[,_register-dll-section_]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

For more information, see [**INF RegisterDlls Directive**](inf-registerdlls-directive.md).

**UnregisterDlls=**_unregister-dll-section_[,_unregister-dll-section_]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).

For more information, see [**INF UnregisterDlls Directive**](inf-unregisterdlls-directive.md).

## Remarks

Throughout the Windows Driver Kit (WDK) documentation, the term _DDInstall_ is used to refer to an _install-section-name_, with or without platform extensions. Therefore, "_DDInstall_ section" means "a named section within an INF, having the format [_install-section-name_] or [_install-section-name_**.nt**_xxx_]". When you create names for _DDInstall_ sections, you should include a device-specific prefix, such as **[WDMPNPB003_Device]** or **[GPR400.Install.NT]**.

Each _DDInstall_ section must be referenced in a device/models-specific entry under the per-manufacturer [**INF _Models_ section**](inf-models-section.md) of the INF file.

Except for devices that have no associated files to be transferred from the source media, an INF file that installs a WDM driver on different operating system platforms must have at least one of the following _DDInstall_ sections:

- An _install-section-name_**.ntx86** section that specifies the entries for device/driver installations specific to x86-based platforms.
- An _install-section-name_**.ntia64** section that specifies the entries for device/driver installations specific to Itanium-based platforms.
- An _install-section-name_**.ntamd64** section that specifies the entries for device/driver installations specific to x64-based platforms.
- An _install-section-name_**.ntarm** section that specifies the entries for device/driver installations specific to Arm-based platforms.
- An _install-section-name_**.ntarm64** section that specifies the entries for device/driver installations specific to Arm64-based platforms.
- An _install-section-name_ or _install-section-name_**.nt** section that specifies the entries for device/driver installations that are not specific to a particular hardware platform.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Starting with Windows 2000, an INF file that installs drivers must have [**DDInstall.Services**](inf-ddinstall-services-section.md) sections to specify driver service information.

Each directive in a _DDInstall_ section can reference more than one section name. However, each additional named section must be separated from the next with a comma (,).

Each section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Any **AddReg** directive specified in a _DDInstall_ section is assumed to reference an add-registry section that cannot be used to store information about upper or lower-filter drivers, about multifunction devices, or about driver-independent but device-specific parameters. If a device/driver INF must store this type of information in the registry, it must use an **AddReg** directive in its undecorated and decorated _DDInstall_**.HW** sections, if any, to reference another INF-writer-defined _add-registry-section_.

Depending on the [device setup class](./overview-of-device-setup-classes.md) that was specified in the [**INF Version section**](inf-version-section.md), additional class-specific directives can be specified in a _DDInstall_ section. For more information about class-specific directives, see the following topics:

- [Building an INF File for a Windows SideShow-Compatible Device](../index.yml)
- [DDInstall Section in a Network INF File](../network/ddinstall-services-section-in-a-network-inf-file.md)
- [INF Files for Still Image Devices](../image/inf-files-for-still-image-devices.md)
- [INF Files for WIA Devices](../image/inf-files-for-wia-devices.md)
- [Installation Requirements for Network Components](../network/installation-requirements-for-network-adapters.md)
- [Specifying WDF Directives in INF Files](../wdf/specifying-wdf-directives-in-inf-files.md)

## Examples

This example shows the expansion of the _DDInstall_ sections, **Ser_Inst** and **Inp_Inst**. These sections are referenced in the example for the [**INF _Models_ section**](inf-models-section.md).

```inf
[Ser_Inst]
CopyFiles=Ser_CopyFiles, mouclass_CopyFiles

[Ser_CopyFiles]
sermouse.sys

[mouclass_CopyFiles] ; section name referenced by > 1 CopyFiles
mouclass.sys

[Inp_Inst]
CopyFiles=Inp_CopyFiles, mouclass_CopyFiles

[Inp_CopyFiles]
inport.sys
```

The following example shows the _DDInstall_ section of an INF file that installs a system-supplied WDM driver for an audio device on various operating system platforms:

```inf
[WDMPNPB003_Device.NT]
Include=ks.inf, wdmaudio.inf
Needs=KS.Registration, WDMAUDIO.Registration.NT
CopyFiles=MSSB16.CopyList
AddReg=WDM_SB16.AddReg
```

The following example shows the sections referenced by the preceding **Needs** entry in the system-supplied _ks.inf_ and _wdmaudio.inf_ files. In the preceding example, these files are specified in the **Includes** entry. When the operating system's device installer processes this device's _install-section-name_.**nt** section, these next two sections are also processed.

```inf
[KS.Registration]
; following AddReg= is actually a single line in the ks.inf file
AddReg=ProxyRegistration,CategoryRegistration,\
    TopologyNodeRegistration,PlugInRegistration,PinNameRegistration,\
    DeviceRegistration 
CopyFiles=KSProxy.Files,KSDriver.Files

[WDMAUDIO.Registration.NT]
AddReg=WDM.AddReg
CopyFiles=WDM.CopyFiles.Sys, WDM.CopyFiles.Drv
;
; INF-writer-defined add-registry and file-list sections
; referenced by preceding directives are omitted here for brevity
;
```

## See also

[**AddProperty**](inf-addproperty-directive.md)

[**_DDInstall_.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[**_DDInstall_.FactDef**](inf-ddinstall-factdef-section.md)

[**_DDInstall_.HW**](inf-ddinstall-hw-section.md)

[**_DDInstall_.Interfaces**](inf-ddinstall-interfaces-section.md)

[**_DDInstall_.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md)

[**_DDInstall_.Services**](inf-ddinstall-services-section.md)

[**DefaultInstall**](inf-defaultinstall-section.md)

[**DefaultInstall.Services**](inf-defaultinstall-services-section.md)

[**DelProperty**](inf-delproperty-directive.md)

[**FeatureScore**](inf-featurescore-directive.md)
