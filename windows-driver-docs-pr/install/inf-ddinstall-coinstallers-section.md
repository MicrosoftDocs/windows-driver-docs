---
title: INF DDInstall.CoInstallers Section
description: The CoInstallers section registers one or more device-specific co-installers to supplement the operations of existing device class installers.
ms.assetid: 2deb16e1-632a-4169-b718-7e3501e64562
keywords:
- INF DDInstall.CoInstallers Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.CoInstallers Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DDInstall.CoInstallers Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

This optional section registers one or more device-specific co-installers supplied on the distribution media to supplement the operations of existing device class installers.

```cpp
[install-section-name.CoInstallers] |
[install-section-name.nt.CoInstallers] | 
[install-section-name.ntx86.CoInstallers] | 
[install-section-name.ntarm.CoInstallers] | (Windows 8 and later versions of Windows)
[install-section-name.ntarm64.CoInstallers] | (Windows 10 version 1709 and later versions of Windows)
[install-section-name.ntia64.CoInstallers] |  (Windows XP and later versions of Windows)
[install-section-name.ntamd64.CoInstallers]  (Windows XP and later versions of Windows)
  
AddReg=add-registry-section[,add-registry-section]... 
CopyFiles=@filename | file-list-section[,file-list-section]...
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...]
[DelFiles=file-list-section[,file-list-section]...]
[RenFiles=file-list-section[,file-list-section]...]
[DelReg=del-registry-section[,del-registry-section]...] 
[BitReg=bit-registry-section[,bit-registry-section]...]
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
... 
```

## Entries


<a href="" id="addreg-add-registry-section--add-registry-section----"></a>**AddReg=**<em>add-registry-section</em>\[**,**<em>add-registry-section</em>\]...  
References one or more INF-writer-defined *add-registry-section*s that store registry information about the supplied co-installers.

An **HKR** specified in such an add-registry section designates the **..Class\\**<em>SetupClassGUID</em>**\\**<em>device-instance-id</em> registry path of the user-accessible driver, which is also referred to as a. "software key". Therefore, for a device-specific co-installer, it writes (or modifies) a **CoInstallers32** value entry in this user-accessible per-device/driver "software" subkey.

For a class-specific co-installer, it registers the new co-installers by modifying the contents of the appropriate **..CoDeviceInstallers\\**<em>SetupClassGUID</em> subkeys. The path of the appropriate registry *SetupClassGUID* subkeys must be explicitly specified in the referenced add-registry sections.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

<a href="" id="copyfiles--filename---file-list-section--file-list-section----"></a>**CopyFiles=@**<em>filename</em> | *file-list-section*\[**,**<em>file-list-section</em>\]...  
Transfers the source co-installer files to the destination on the target computer, usually by referencing one or more INF-writer-defined *file-list-section*s elsewhere in the INF file. Such a file-list section specifies the co-installer files to be copied from the source media to the destination directory on the target.

However, system INF files that install co-installers never use this directive in a <em>DDInstall</em>**.CoInstallers** section.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

<a href="" id="include-filename-inf--filename2-inf----"></a>**Include=**<em>filename</em>**.inf**\[**,**<em>filename2</em>**.inf**\]...  
Specifies one or more additional system-supplied INF files that contain sections needed to install the co-installers for this device or [device setup class](device-setup-classes.md). If this entry is specified, usually so is a **Needs** entry. (For more information about the **Include** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md)).

<a href="" id="needs-inf-section-name--inf-section-name----"></a>**Needs=**<em>inf-section-name</em>\[**,**<em>inf-section-name</em>\]...  
Specifies the particular sections that must be processed during the installation of this device. Typically, such a named section is a <em>DDInstall</em>**.CoInstallers** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within such a <em>DDInstall</em>**.CoInstallers** section of the included INF.

**Needs** entries cannot be nested. For more information about the **Needs** entry and restrictions on its use, see [Specifying the Source and Target Locations for Device Files](specifying-the-source-and-target-locations-for-device-files.md).

<a href="" id="delfiles-file-list-section--file-list-section----"></a>**DelFiles=**<em>file-list-section</em>\[**,**<em>file-list-section</em>\]...  
References a file-list section specifying files to be removed from the target. This directive is rarely used.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

<a href="" id="renfiles-file-list-section--file-list-section----"></a>**RenFiles=**<em>file-list-section</em>\[**,**<em>file-list-section</em>\]...  
References a file-list section specifying files on the destination to be renamed before co-installer source files are copied to the target. This directive is also rarely used.

For more information, see [**INF RenFiles Directive**](inf-renfiles-directive.md).

<a href="" id="delreg-del-registry-section--del-registry-section----"></a>**DelReg=**<em>del-registry-section</em>\[**,**<em>del-registry-section</em>\]...  
References one or more INF-writer-define *delete-registry-section*s. Such a section specifies stale registry information about the co-installers for a previous installation of the same devices that should be removed from the registry. An **HKR** specified in such a delete-registry section designates the same registry subkey as already described for the **AddReg** entry. This directive is very rarely used in a <em>DDInstall</em>**.CoInstallers** section.

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

<a href="" id="bitreg-bit-registry-section--bit-registry-section----"></a>**BitReg=**<em>bit-registry-section</em>\[**,**<em>bit-registry-section</em>\]...  
This entry is valid in this section but almost never used. An **HKR** specified in such a bit-registry section designates the same registry subkey as already described for the **AddReg** entry.

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

<a href="" id="updateinis-update-ini-section--update-ini-section----"></a>**UpdateInis=**<em>update-ini-section</em>\[**,**<em>update-ini-section</em>\]...  
This entry is valid in this section but almost never used.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

<a href="" id="updateinifields-update-inifields-section--update-inifields-section----"></a>**UpdateIniFields=**<em>update-inifields-section</em>\[**,**<em>update-inifields-section</em>\]...  
This entry is valid in this section but almost never used.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

<a href="" id="ini2reg-ini-to-registry-section--ini-to-registry-section----"></a>**Ini2Reg=**<em>ini-to-registry-section</em>\[**,**<em>ini-to-registry-section</em>\]...  
This entry is valid in this section but almost never used.

For more information, see [**INF Ini2Reg Directive**](inf-ini2reg-directive.md).

Remarks
-------

The specified *DDInstall* section must be referenced in a device/models-specific entry under the per-manufacturer *Models* section of the INF file.

If an INF includes a <em>DDInstall</em>**.Coinstallers** section, there must be one for each platform-decorated and undecorated *DDInstall* section. For example, if an INF contains an **\[**<em>install-section-name</em>**.ntx86\]** section and an **\[**<em>install-section-name</em>**\]** section and it registers device-specific co-installers, then the INF must include both an **\[**<em>install-section-name</em>**.ntx86.Coinstallers\]** section and an **\[**<em>install-section-name</em>**.Coinstallers\]** section. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

Each directive in a <em>DDInstall</em>**.CoInstallers** section can reference more than one INF-writer-defined section name. However, each additional named section must be separated from the next with a comma (,).

Each directive-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

A co-installer is a Win32 DLL that typically writes additional configuration information to the registry or performs other installation tasks that require dynamically generated, system-specific information that is not available when an INF is created. A device-specific co-installer supplements the installation operations either of the OS's device installer or of the appropriate class installer when that device is installed.

For more information about how to write and using co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

### Installing Co-installer Images

All co-installer files must be copied into the *%SystemRoot%\\system32* directory. Like any INF **CopyFiles** operation, the destination is controlled explicitly for a named *file-list-section* in the [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF file by the *dirid* value **11** or by supplying this *dirid* value for the **DefaultDestDir** entry.

### Registering Device-Specific Co-installers

Registering one or more device-specific co-installers requires adding a [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-typed value entry to the registry. Specify an *add-registry-section* referenced by the [**AddReg**](inf-addreg-directive.md) directive, by using the following general form:

```cpp
[DDInstall.CoInstallers_DeviceAddReg]
 
HKR,,CoInstallers32,0x00010000,"DevSpecificCoInstall.dll
   [,DevSpecificEntryPoint]"[,"DevSpecific2CoInstall.dll
      [,DevSpecific2EntryPoint]"...] 
```

The **HKR** entry is listed as a single line within the INF file, and each supplied device-specific co-installer DLL must have a unique name. After the listed co-installers are registered, the system's device installer calls them at each subsequent step of the installation process for that device.

If the optional *DevSpecificEntryPoint* is omitted, the default **CoDeviceInstall** routine name is used as the entry point of the co-installer DLL.

For more information, see [Registering a Device-Specific Co-installer](registering-a-device-specific-co-installer.md).

### Registering Device-Class Co-installers

To add a value entry (and setup-class subkey, if it does not exist already) for one or more device-class co-installers to the registry, an *add-registry-section* referenced by the [**AddReg**](inf-addreg-directive.md) directive has the following general form:

```cpp
[DDInstall.CoInstallers_ClassAddReg]
 
HKLM,System\CurrentControlSet\Control
    \CoDeviceInstallers,{SetupClassGUID},
       0x00010008,"DevClssCoInst.dll[,DevClssEntryPoint]" 
 ...
```

Each entry in such an add-registry section is listed as a single line within the INF file, and each supplied class co-installer DLL must have a unique name. If the supplied co-installers should be used for more than one [device setup class](device-setup-classes.md), this add-registry section can have more than one entry, each with the appropriate *SetupClassGUID* value.

Such a supplemental device-class co-installer must not replace any already registered co-installers for an existing class installer. Therefore, the class co-installer must have a unique name and the [REG_MULTI_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types)-type value supplied must be appended (as indicated by the **8** in the *flags* value **0x0010008**) to the class-specific co-installer entries, if any, already present in the **{**<em>SetupClassGUID</em>**}** subkey.

**Note**  The [SetupAPI](setupapi.md) functions never append a duplicate <em>DevClssCoInstall</em>**.dll** to a value entry if a co-installer of the same name is already registered.

 

The INF for a supplemental device-class co-installer can be activated by a right-click install or through a call to [**SetupInstallFromInfSection**](https://msdn.microsoft.com/library/windows/desktop/aa377401) made by a [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application).

Examples
--------

This example shows the *DDInstall*.**CoInstallers** section for IrDA serial network adapters. The system-supplied INF for these IrDA (serial) NICs supplies a co-installer to the system IrDA class installer.

```cpp
; DDInstall section
[PNP.NT]
AddReg=ISIR.reg, Generic.reg, Serial.reg
PromptForPort=0     ; This is handled by IRCLASS.DLL
LowerFilters=SERIAL ; This is handled by IRCLASS.DLL
BusType=14
Characteristics=0x4 ; NCF_PHYSICAL 

; ... PNP.NT.Services section omitted here
[PNP.NT.CoInstallers]
AddReg = ISIR.CoInstallers.reg 
; ...

[IRSIR.reg]
HKR, Ndi, HelpText, 0, %IRSIR.Help%
HKR, Ndi, Service, 0, "IRSIR"
HKR, Ndi\Interfaces, DefUpper, 0, "ndisirda"
HKR, Ndi\Interfaces, DefLower, 0, "nolower"
HKR, Ndi\Interfaces, UpperRange, 0, "ndisirda"
HKR, Ndi\Interfaces, LowerRange, 0, "nolower"

[Generic.reg]
HKR,,InfraredTransceiverType,0,"0"

[Serial.reg]
HKR,,SerialBased,0, "0"

[ISIR.CoInstallers.reg]
HKR,,CoInstallers32,0x00010000,"IRCLASS.dll,IrSIRClassCoInstaller"

; ... Services and Event Log registry sections omitted here
[Strings]
; ...
IRSIR.Help = "An IrDA serial infrared device is a built-in COM port or 
external transceiver which transmits infrared pulses. This NDIS 
miniport driver installs as a network adapter and binds to the FastIR 
protocol."
```

The preceding PNP<strong>.NT.CoInstallers</strong> section only referenced a co-installer-specific *add-registry* section. It has no [**CopyFiles**](inf-copyfiles-directive.md) directive because this system-supplied INF installs a set of IrDA network devices. Like all system INF files, this INF file uses the **LayoutFile** entry in its [**Version**](inf-version-section.md) section to transfer the co-installer file to the destination.

Be aware that any <em>DDInstall</em>**.CoInstallers** section in an INF supplied by an IHV or OEM also has a **CopyFiles** directive, along with [**SourceDisksNames**](inf-sourcedisksnames-section.md) and [**SourceDisksFiles**](inf-sourcedisksfiles-section.md) sections.

## See also


[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DelReg**](inf-delreg-directive.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SourceDisksFiles**](inf-sourcedisksfiles-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

**UpdateInis**
[**Version**](inf-version-section.md)

 

 






