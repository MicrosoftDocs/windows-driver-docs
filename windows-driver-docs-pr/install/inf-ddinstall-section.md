---
title: INF DDInstall Section
description: Each per-Models DDInstall section contains an optional DriverVer directive and one or more directives referencing additional named sections in the INF file, shown here with the most frequently specified INF directives, CopyFiles and AddReg, listed first.
ms.assetid: 79cba88d-fda1-4b91-bf51-98afd7224bc9
keywords:
- INF DDInstall Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall Section


Each per-Models *DDInstall* section contains an optional **DriverVer** directive and one or more directives referencing additional named sections in the INF file, shown here with the most frequently specified INF directives, **CopyFiles** and **AddReg**, listed first.

The sections referenced by these directives contain instructions for installing driver files and writing any device-specific and/or driver-specific information into the registry.

```cpp
[install-section-name] | 
[install-section-name.nt] | 
[install-section-name.ntx86] | 
[install-section-name.ntia64] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64]  (Windows XP and later versions of Windows)

[DriverVer=mm/dd/yyyy[,x.y.v.z] ]
[CopyFiles=@filename | file-list-section[,file-list-section] ...]
[CopyINF=filename1.inf[,filename2.inf]...]   (Windows XP and later versions of Windows)
[AddReg=add-registry-section[,add-registry-section]...]
[AddProperty=add-registry-section[,add-registry-section]...]  (Windows Vista and later versions of Windows)
[Include=filename1.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[Delfiles=file-list-section[,file-list-section]...]
[Renfiles=file-list-section[,file-list-section]...]
[DelReg=del-registry-section[,del-registry-section]...]
[DelProperty=add-registry-section[,add-registry-section]...]  (Windows Vista and later versions of Windows)
[FeatureScore=featurescore]...  (Windows Vista and later versions of Windows)
[BitReg=bit-registry-section[,bit-registry-section]...]
[LogConfig=log-config-section[,log-config-section]...]
[ProfileItems=profile-items-section[,profile-items-section]...]  (Microsoft Windows 2000 and later versions of Windows)
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
[RegisterDlls=register-dll-section[,register-dll-section]...]
[UnregisterDlls=unregister-dll-section[,unregister-dll-section]...]
[ExcludeID=device-identification-string[,device-identification-string]...]...  ((Windows XP and later versions of Windows)
[Reboot]
```

## Entries


<a href="" id="driverver-mm-dd-yyyy--x-y-v-z--"></a>**DriverVer=**<em>mm/dd/yyyy</em>\[**,**<em>x.y.v.z</em>\]   
This optional entry specifies version information for the [driver package](driver-packages.md).

For information about how to specify this entry, see [**INF DriverVer Directive**](inf-driverver-directive.md).

<a href="" id="copyfiles--filename---file-list-section--file-list-section-----"></a>**CopyFiles=@**<em>filename</em> | *file-list-section*\[**,**<em>file-list-section</em>\] ...  
This directive either specifies one named file to be copied from the source media to the destination or references one or more INF-writer-defined sections in which device-relevant files on the source media are specified for transfer to the destination. The **CopyFiles** directive is optional, but is present in most *DDInstall* sections.

The **DefaultDestDir** entry in the [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF specifies the destination for any single file to be copied. The [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections, or an additional INF specified in the **LayoutFile** entry of this INF's [**Version**](inf-version-section.md) section, provide the location on the distribution media of the driver files.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

<a href="" id="copyinf-filename1-inf--filename2-inf----"></a>**CopyINF=**<em>filename1</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
(Windows XP and later) This directive causes specified INF files to be copied to the target system.

For more information, see [**INF CopyINF Directive**](inf-copyinf-directive.md).

<a href="" id="addreg-add-registry-section--add-registry-section----"></a>**AddReg=**<em>add-registry-section</em>\[**,**<em>add-registry-section</em>\]...  
This directive references one or more INF-writer-defined sections in which new subkeys, possibly with initial value entries, are specified to be written into the registry or in which the value entries of existing keys are modified.

An **HKR** specification in such an add-registry section designates the **..Class\\**<em>SetupClassGUID</em>**\\**<em>device-instance-id</em> registry path of the user-accessible driver. This type of **HKR** specification is also referred to as a. "software key".

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

<a href="" id="addproperty-add-registry-section--add-registry-section----"></a>**AddProperty=**<em>add-registry-section</em>\[**,**<em>add-registry-section</em>\]...  
(Windows Vista and later) References one or more INF file sections that modify [device properties](device-properties.md) that are set for a device instance. You should use an [**INF AddProperty directive**](inf-addproperty-directive.md) only to set a device instance property that is new to Windows Vista or later versions of Windows operating systems.

For device instance properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) to set the device instance properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **AddProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

<a href="" id="include-filename1-inf--filename2-inf----"></a>**Include=**<em>filename1</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device and/or driver. If this entry is specified, usually so is a **Needs** entry.

For example, the system INF files for device drivers that depend on the system's kernel-streaming support specify this entry as follows:

```cpp
Include= ks.inf[, [kscaptur.inf,] [ksfilter.inf]]...
```

For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
This optional entry specifies sections within system-supplied INF files that must be processed during the installation of this device. Typically, such a named section is a *DDInstall* (or <em>DDInstall</em>**.**<em>xxx</em>) section within one of the INF files that are listed in an **Include** entry. However, it can be any section that is referenced within such a *DDInstall* or <em>DDInstall</em>**.**<em>xxx</em> section of the included INF.

For example, the INF files for device drivers that have the preceding **Include** entry specify this entry as follows:

```cpp
Needs= KS.Registration[, KSCAPTUR.Registration | KSCAPTUR.Registration.NT, MSPCLOCK.Installation]
```

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="delfiles-file-list-section--file-list-section----"></a>**Delfiles=**<em>file-list-section</em>\[**,**<em>file-list-section</em>\]...  
This directive references one or more INF-writer-defined sections listing files on the target to be deleted.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

<a href="" id="renfiles-file-list-section--file-list-section----"></a>**Renfiles=**<em>file-list-section</em>\[**,**<em>file-list-section</em>\]...  
This directive references one or more INF-writer-defined sections listing files to be renamed on the destination before device-relevant source files are copied to the target computer.

For more information, see[**INF RenFiles Directive**](inf-renfiles-directive.md).

<a href="" id="delreg-del-registry-section--del-registry-section----"></a>**DelReg=**<em>del-registry-section</em>\[**,**<em>del-registry-section</em>\]...  
This directive references one or more INF-writer-defined sections in which keys and/or value entries are specified to be removed from the registry during installation of the devices.

Typically, this directive is used to handle upgrades when an INF must clean up old registry entries from a previous installation of this device.

An **HKR** specification in such a delete-registry section designates the **..Class\\**<em>SetupClassGUID</em>**\\**<em>device-instance-id</em> registry path of the user-accessible driver. This type of **HKR** specification is also referred to as a. "software key".

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

<a href="" id="delproperty-add-registry-section--add-registry-section----"></a>**DelProperty=**<em>add-registry-section</em>\[**,**<em>add-registry-section</em>\]...  
(Windows Vista and later) References one or more INF file sections that delete [device properties](device-properties.md) that are set for a device instance. You should use an [**INF DelProperty directive**](inf-delproperty-directive.md) only to delete a device instance property that is new to Windows Vista or later versions of Windows.

For device instance properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF DelReg directives**](inf-delreg-directive.md) to delete the device instance properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

<a href="" id="featurescore-featurescore"></a>**FeatureScore=**<em>featurescore</em>  
**Warning**  The **FeatureScore** directive is only processed when specified directly in the **\[DDInstall\]** section.

 

(Windows Vista and later) This directive provides an additional ranking criterion for drivers that are based on the features that a driver supports. For example, feature scores might be defined for a [device setup class](device-setup-classes.md) that distinguishes between drivers based on class-specific criteria.

For more information about how drivers are ranked, see [How Windows Ranks Drivers (Windows Vista and Later)](how-setup-ranks-drivers--windows-vista-and-later-.md).

For more information about this directive, see [**INF FeatureScore Directive**](inf-featurescore-directive.md).

**Note**  Although a *DDInstall* section can contain multiple **FeatureScore** entries, only the first entry is processed for the section.

 

<a href="" id="bitreg-bit-registry-section--bit-registry-section----"></a>**BitReg=**<em>bit-registry-section</em>\[**,**<em>bit-registry-section</em>\]...  
This directive references one or more INF-writer-defined sections in which existing registry value entries of type [REG_BINARY](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) are modified.

An **HKR** specification in such a bit-registry section designates the **..Class\\**<em>SetupClassGUID</em>**\\**<em>device-instance-id</em> registry path of the user-accessible driver. This type of **HKR** specification is also referred to as a. "software key".

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

<a href="" id="logconfig-log-config-section--log-config-section----"></a>**LogConfig=**<em>log-config-section</em>\[**,**<em>log-config-section</em>\]...  
This directive references one or more INF-writer-defined sections within an INF for a root-enumerated device or for a manually installed device. In these named sections, the INF for such a "detected" or manually installed device specifies one or more logical configurations of bus-relative hardware resources that the device must have to be operational. The INF for such a manually installed device that is not software-configurable should also have a <em>DDInstall</em>**.FactDef** section.

The **LogConfig** directive is never used to install Plug and Play (PnP) devices. However, you can use an [**INF DDInstall.LogConfigOverride section**](inf-ddinstall-logconfigoverride-section.md) to provide an override configuration for PnP devices.

This directive is irrelevant to all higher-level (nondevice) drivers and components.

For more information, see [**INF LogConfig Directive**](inf-logconfig-directive.md).

<a href="" id="profileitems-profile-items-section--profile-items-section----"></a>**ProfileItems=**<em>profile-items-section</em>\[**,**<em>profile-items-section</em>\]...  
(Microsoft Windows 2000 and later versions of Windows) This directive references one or more INF-writer-defined sections that describe items to be added to, or removed from, the Start menu.

For more information, see [**INF ProfileItems Directive**](inf-profileitems-directive.md).

<a href="" id="updateinis-update-ini-section--update-ini-section----"></a>**UpdateInis=**<em>update-ini-section</em>\[**,**<em>update-ini-section</em>\]...  
This rarely used directive references one or more INF-writer-defined sections, specifying a source INI file from which a particular section or line within such a section is to be read into a destination INI file of the same name during installation. Optionally, line-by-line modifications to an existing INI file on the destination from a given source INI file of the same name can be specified in the update-ini section.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

<a href="" id="updateinifields-update-inifields-section--update-inifields-section----"></a>**UpdateIniFields=**<em>update-inifields-section</em>\[**,**<em>update-inifields-section</em>\]...  
This rarely used directive references one or more INF-writer-defined sections in which modifications within the lines of a device-specific INI file are specified.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

<a href="" id="ini2reg-ini-to-registry-section--ini-to-registry-section----"></a>**Ini2Reg=**<em>ini-to-registry-section</em>\[**,**<em>ini-to-registry-section</em>\]...  
This rarely used directive references one or more INF-writer-defined sections in which sections or lines from a device-specific INI file, supplied on the source media, are to be moved into the registry.

For more information, see [**INF Ini2Reg Directive**](inf-ini2reg-directive.md).

<a href="" id="registerdlls-register-dll-section--register-dll-section----"></a>**RegisterDlls=**<em>register-dll-section</em>\[**,**<em>register-dll-section</em>\]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-registration.

For more information, see [**INF RegisterDlls Directive**](inf-registerdlls-directive.md).

<a href="" id="unregisterdlls-unregister-dll-section--unregister-dll-section----"></a>**UnregisterDlls=**<em>unregister-dll-section</em>\[**,**<em>unregister-dll-section</em>\]...  
This directive references one or more INF sections used to specify files that are OLE controls and require self-unregistration (self-removal).

For more information, see [**INF UnregisterDlls Directive**](inf-unregisterdlls-directive.md).

<a href="" id="excludeid-device-identification-string--device-identification-string----"></a>**ExcludeID=**<em>device-identification-string</em>\[**,**<em>device-identification-string</em>\]...  
**Warning**  The **ExcludeID** directive is only processed when specified directly in the **\[DDInstall\]** section.

 

(Windows XP and later) This directive specifies one or more device identification strings (either [hardware IDs](hardware-ids.md) or [compatible IDs](compatible-ids.md)). The *DDInstall* section does not install devices that have [device IDs](device-ids.md) that match any of the hardware IDs or compatible IDs listed.

<a href="" id="reboot"></a>**Reboot**  
This directive indicates that the caller should be prompted to reboot the system after installation is complete.

For more information, see [**INF Reboot Directive**](inf-reboot-directive.md).

Remarks
-------

Throughout the Windows Driver Kit (WDK) documentation, the term *DDInstall* is used to refer to an *install-section-name*, with or without platform extensions. Therefore, "*DDInstall* section" means "a named section within an INF, having the format \[*install-section-name*\] or \[<em>install-section-name</em>**.nt***xxx*\]". When you create names for *DDInstall* sections, you should include a device-specific prefix, such as **\[WDMPNPB003_Device\]** or **\[GPR400.Install.NT\]**.

Each *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer [**INF *Models* section**](inf-models-section.md) of the INF file.

Except for devices that have no associated files to be transferred from the source media, an INF file that installs a WDM driver on different operating system platforms must have at least one of the following *DDInstall* sections:

- An <em>install-section-name</em>**.ntx86** section that specifies the entries for device/driver installations specific to x86-based platforms.
- An <em>install-section-name</em>**.ntia64** section that specifies the entries for device/driver installations specific to Itanium-based platforms.
- An <em>install-section-name</em>**.ntamd64** section that specifies the entries for device/driver installations specific to x64-based platforms.
- An *install-section-name* or <em>install-section-name</em>**.nt** section that specifies the entries for device/driver installations that are not specific to a particular hardware platform.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Starting with Windows 2000, an INF file that installs drivers must have [**DDInstall.Services**](inf-ddinstall-services-section.md) sections to specify device/driver registry information to be stored in the registry's **...\\CurrentControlSet\\Services** tree. Depending on the device, it can also have one or more <em>DDInstall</em>**.HW**, <em>DDInstall</em>**.CoInstallers**, <em>DDInstall</em>**.Interfaces**, and/or <em>DDInstall</em>**.LogConfigOverride** sections.

Each directive in a *DDInstall* section can reference more than one section name. However, each additional named section must be separated from the next with a comma (,).

Each section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Any **AddReg** directive specified in a *DDInstall* section is assumed to reference an add-registry section that cannot be used to store information about upper or lower-filter drivers, about multifunction devices, or about driver-independent but device-specific parameters. If a device/driver INF must store this type of information in the registry, it must use an **AddReg** directive in its undecorated and decorated <em>DDInstall</em>**.HW** sections, if any, to reference another INF-writer-defined *add-registry-section*.

Depending on the [device setup class](device-setup-classes.md) that was specified in the [**INF Version section**](inf-version-section.md), additional class-specific directives can be specified in a *DDInstall* section. For more information about class-specific directives, see the following topics:

-   [Building an INF File for a Windows SideShow-Compatible Device](https://msdn.microsoft.com/library/windows/hardware/ff547750)
-   [DDInstall Section in a Network INF File](https://msdn.microsoft.com/library/windows/hardware/ff546332)
-   [INF Files for Still Image Devices](https://msdn.microsoft.com/library/windows/hardware/ff542762)
-   [INF Files for WIA Devices](https://msdn.microsoft.com/library/windows/hardware/ff542770)
-   [Installation Requirements for Network Components](https://msdn.microsoft.com/library/windows/hardware/ff554949)
-   [Specifying WDF Directives in INF Files](https://msdn.microsoft.com/windows/hardware/drivers/wdf/specifying-wdf-directives-in-inf-files)

Examples
--------

This example shows the expansion of the *DDInstall* sections, **Ser_Inst** and **Inp_Inst**. These sections are referenced in the example for the [**INF *Models* section**](inf-models-section.md).

```cpp
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

The following example provides a general illustration of using platform extensions:

```cpp
[Manufacturer]
%MSFT% = Microsoft

[Microsoft]
%Device.DeviceDesc% = DeviceInstall, HWID
[DeviceInstall.NTx86]
;
; This section is used for installations on x86 systems.
;
...
[DeviceInstall.NTx86.Services]
;
; Services installation for x86 systems.
;
...
[DeviceInstall.NT]
;
; This section is used for installations on systems (all other architectures).
;
...
[DeviceInstall.NT.Services]
;
; Services installation for systems (all other architectures).
;
...
```

The following example shows the *DDInstall* section of an INF file that installs a system-supplied WDM driver for an audio device on various operating system platforms:

```cpp
[WDMPNPB003_Device.NT]
DriverVer=01/14/1999,5.0
Include=ks.inf, wdmaudio.inf
Needs=KS.Registration, WDMAUDIO.Registration.NT
LogConfig=SB16.LC1,SB16.LC2,SB16.LC3,SB16.LC4,SB16.LC5 
; a few log-config-sections omitted here for brevity
CopyFiles=MSSB16.CopyList
AddReg=WDM_SB16.AddReg
```

The following example shows the sections referenced by the preceding **Needs** entry in the system-supplied *ks.inf* and *wdmaudio.inf* files. In the preceding example, these files are specified in the **Includes** entry. When the operating system's device installer and/or media class installer process this device's <em>install-section-name</em>**.nt** section, these next two sections are also processed.

```cpp
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

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.FactDef**](inf-ddinstall-factdef-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[***DDInstall*.LogConfigOverride**](inf-ddinstall-logconfigoverride-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**DefaultInstall**](inf-defaultinstall-section.md)

[**DefaultInstall.Services**](inf-defaultinstall-services-section.md)

[**DelProperty**](inf-delproperty-directive.md)

[**FeatureScore**](inf-featurescore-directive.md)

 

 






