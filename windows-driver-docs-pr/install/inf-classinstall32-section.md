---
title: INF ClassInstall32 Section
description: A ClassInstall32 section installs a new device setup class (and possibly a class installer) for devices in the new class.
ms.assetid: c1da44ca-3b99-43de-99ef-56fbe67b46c2
keywords:
- INF ClassInstall32 Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF ClassInstall32 Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF ClassInstall32 Section


**Note**  If you are building a universal or mobile driver package, this section is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **ClassInstall32** section installs a new [device setup class](device-setup-classes.md) (and possibly a class installer) for devices in the new class.

```cpp
[ClassInstall32] | 
[ClassInstall32.nt] | 
[ClassInstall32.ntx86] |
[ClassInstall32.ntarm] | (Windows 8 and later versions of Windows) 
[ClassInstall32.ntarm64] | (Windows 10 version 1709 and later versions of Windows) 
[ClassInstall32.ntia64] | (Windows XP and later versions of Windows)
[ClassInstall32.ntamd64] (Windows XP and later versions of Windows)

AddReg=add-registry-section[,add-registry-section]...
[AddProperty=add-property-section[,add-property-section] ...]  (Windows Vista and later versions of Windows)
[Copyfiles=@filename | file-list-section[,file-list-section]...]
[DelReg=del-registry-section[,del-registry-section]...]
[DelProperty=del-property-section[,del-property-section] ...]  (Windows Vista and later versions of Windows)
[Delfiles=file-listsection[,file-list-section]...]
[Renfiles=file-list-section[,file-list-section]...]
[BitReg=bit-registry-section[,bit-registry-section]...]
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
```

## Entries


<a href="" id="addreg-add-registry-section--add-registry-section-----"></a>**AddReg=**<em>add</em>-*registry*-*section*\[**,**<em>add</em>-*registry*-*section*\] ...  
References one or more named sections that contain class-specific value entries to be written into the registry. Typically, this is used to give the new device setup class at least a friendly name that other components can later retrieve from the registry and use to open installed devices of this new device class, to "install" any new device class installer and/or property-page provider for this device setup class, and so forth.

An **HKR** specification in any *add-registry-section* designates the **..Class\\{**<em>SetupClassGUID</em>**}** registry key. For additional information, see the following **Remarks** section.

For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

<a href="" id="addproperty-add-property-section--add-property-section-----"></a>**AddProperty=**<em>add-property-section</em>\[**,**<em>add-property-section</em>\] ...  
(Windows Vista and later versions of Windows) References one or more INF file sections that modify [device properties](device-properties.md) that are set for a [device setup class](device-setup-classes.md). You should use an [**INF AddProperty directive**](inf-addproperty-directive.md) only to set a device setup class property that is new to Windows Vista or later versions of Windows operating systems.

For device class properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) to set the device setup class properties. These guidelines apply to system-defined properties and custom properties.

For more information about how to use the **AddProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

<a href="" id="copyfiles--filename---file-list-section--file-list-section-----"></a>**Copyfiles=@**<em>filename</em> | *file*-*list*-*section*\[**,**<em>file</em>-*list*-*section*\] ...  
Either specifies one named file to be copied from the source media to the destination or references one or more named sections in which class-relevant files on the source media are specified for transfer to the destination. The **DefaultDestDir** entry in the [**DestinationDirs**](inf-destinationdirs-section.md) section of the INF specifies the destination directory for any class-specific single file to be copied.

For more information, see [**INF CopyFiles Directive**](inf-copyfiles-directive.md).

**Note**  System-supplied INF files for device setup classes (and class installers) do not use this directive in this section.

 

<a href="" id="delreg-del-registry-section--del-registry-section-----"></a>**DelReg=**<em>del</em>-*registry*-*section*\[**,**<em>del</em>-*registry*-*section*\] ...  
References one or more named sections in which value entries or keys are specified to be removed from the registry during installation of the class installer.

However, if a particular **{**<em>SetupClassGUID</em>**}** subkey exists in the registry **..Class** branch, the system setup code subsequently ignores the **ClassInstall32** section of any INF that specifies the same GUID value in its **Version** section. Consequently, an INF cannot replace an existing class installer or modify its behavior from a **ClassInstall32** section. To modify the behavior of existing class installer, use a class-specific co-installer.

For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

<a href="" id="delproperty-del-property-section--del-property-section-----"></a>**DelProperty=**<em>del-property-section</em>\[**,**<em>del-property-section</em>\] ...  
(Windows Vista and later versions of Windows) References one or more INF file sections that delete [device properties](device-properties.md) that are set for a [device setup class](device-setup-classes.md). You should use an [**INF DelProperty directive**](inf-delproperty-directive.md) only to delete a device setup class property that is new to Windows Vista or later versions of Windows operating systems.

For device class properties that were introduced earlier on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry entry values, you should continue to use [**INF DelReg directives**](inf-delreg-directive.md) to delete the device setup class properties. These guidelines apply to system-defined properties and custom properties.

For more information about how to use the **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

<a href="" id="delfiles-file-listsection--file-list-section-----"></a>**Delfiles=**<em>file-listsection</em>\[**,**<em>file</em>-*list*-*section*\] ...  
References one or more named sections in which previously installed class-relevant files on the destination are specified for deletion.

For more information, see [**INF DelFiles Directive**](inf-delfiles-directive.md).

<a href="" id="renfiles-file-list-section--file-list-section-----"></a>**Renfiles=**<em>file-list-section</em>\[**,**<em>file</em>-*list*-*section*\] ...  
References one or more named sections in which class-relevant files to be renamed on the destination are listed.

For more information, see [**INF RenFiles Directive**](inf-renfiles-directive.md).

<a href="" id="bitreg-bit-registry-section--bit-registry-section----"></a>**BitReg=**<em>bit-registry-section</em>\[**,**<em>bit-registry-section</em>\]...  
Is valid in this section but almost never used.

For more information, see [**INF BitReg Directive**](inf-bitreg-directive.md).

<a href="" id="updateinis-update-ini-section--update-ini-section------"></a>**UpdateInis**=*update-ini-section\[,update-ini-section\]*...   
Is valid in this section but almost never used.

For more information, see [**INF UpdateInis Directive**](inf-updateinis-directive.md).

<a href="" id="updateinifields-update-inifields-section--update-inifields-section----"></a>**UpdateIniFields=**<em>update-inifields-section</em>\[**,**<em>update-inifields-section</em>\]...  
Is valid in this section but almost never used.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

<a href="" id="ini2reg-ini-to-registry-section--ini-to-registry-section----"></a>**Ini2Reg=**<em>ini-to-registry-section</em>\[**,**<em>ini-to-registry-section</em>\]...  
Is valid in this section but almost never used.

For more information, see [**INF UpdateIniFields Directive**](inf-updateinifields-directive.md).

Remarks
-------

You should include a **ClassInstall32** section in a device INF file only to install a new custom device setup class. INF files for devices in an installed class, whether a [system-supplied device setup class](https://msdn.microsoft.com/library/windows/hardware/ff553419) or a custom class, should not include a **ClassInstall32** section. Because the system processes a **ClassInstall32** section only if a class is not already installed, you cannot use a **ClassInstall32** section to reinstall or change the settings for a class that is already installed. In particular, you cannot use a **ClassInstall32** section to add a class co-installer or a class filter driver for a class that is already installed. For information about how to install co-installers and filter drivers, see [Writing a Co-installer](writing-a-co-installer.md) and [Installing a Filter Driver](installing-a-filter-driver.md).

Usually, a **ClassInstall32** section has one or more **AddReg** directives to add entries under a system-provided *SetupClassGUID* subkey in the registry. These entries can include a class-specific "friendly name," class installer path, class icon, property page provider, and so forth.

Except for **AddReg** and **CopyFiles**, the other directives shown here are rarely used in a **ClassInstall32** section.

To support a multiplatform distribution of driver files, construct platform-specific **ClassInstall32** sections. For example, all system SetupAPI functions that process a **ClassInstall32** section will search first for a **ClassInstall32.ntx86** section on an x86 platform and only examine an undecorated **ClassInstall32** section if they cannot find a **ClassInstall32.ntx86** section. For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

**Note**  The **ClassInstall32** section name is also used for installations on 64-bit platforms.

 

Starting with Windows 2000, every installed device is associated with a [device setup class](device-setup-classes.md) in the registry. If the INF for a device to be installed is not associated with a new device class installer, or if its **ClassGUID=** specification in the **Version** section does not match a system-defined setup class GUID, that device's registry subkey is created under **..Class\\{**<em>UnknownClassGUID</em>**}**.

The INF for any device class installer typically has an **AddReg** directive in its **ClassInstall32** section, to define at least one named section that creates a friendly name for its kind of device. The setup code automatically creates a *SetupClassGUID* subkey in the registry from the value supplied for the **ClassGUID=** entry in the INF's **Version** section when the first device of that (new) setup class is installed.

Under this *SetupClassGUID* subkey, such an INF also provides registry information for *Models*-specific subkeys by using additional **AddReg** directives in its *DDInstall* section. In addition, the INF can use the add-registry sections referenced in its **ClassInstall32** section to specify a property-page provider and to exert control over how its class of devices is handled in the user interface.

Such a class-specific add-registry section has the following general form:

```cpp
[SetupClassAddReg]
 
HKR,,,,%DevClassName% ; device-class friendly name 
[HKR,,Installer32,,"class-installer.dll,class-entry-point"] 
[HKR,,EnumPropPages32,,"prop-provider.dll,provider-entry-point"]
HKR,,Icon,,"icon-number" 
[HKR,,SilentInstall,,1]
[HKR,,NoInstallClass,,1]
[HKR,,NoDisplayClass,,1]
```

The system uses the specified icon to represent your installer to the user.

-   If the Icon value is positive, it represents a resource identifier for a resource. The resource is extracted from the class installer DLL, if the Installer32 key is specified, or from the property page DLL, if the EnumPropPages32 key is specified. The value "0" represents the first icon in the DLL. The value "1" is reserved.
-   If the Icon value is negative, the absolute value is the resource identifier of the icon in SetupApi.DLL.

Setting the predefined **SilentInstall**, **NoDisplayClass**, and **NoInstallClass** Boolean value entries in a class-specific registry key has the following effects:

-   Setting SilentInstall directs installers to send no popup messages to the user that require a response while installing devices of this class, whether specified in the DDInstall sections of the class installer's INF file or in separate INF files for subsequently installed devices that declare themselves of this class by setting the same ClassGuid={ClassGUID} specification in their respective Version sections. For example, the system class installers of CD-ROM and disk devices and the system parallel port class installer set SilentInstall in their respective registry keys.

    If a class-specific installer requires the computer to be restarted for any device that it installs, the class-specific add-registry section in its INF cannot have this value entry.

-   Setting NoDisplayClass suppresses the user-visible display of all devices of this class by Device Manager. For example, the system class installers for printers and for network drivers (including clients, services, and protocols) set NoDisplayClass in their respective registry keys.
-   Setting NoInstallClass indicates that no device of this type will ever require manual installation by an end-user. For example, the system class installers for exclusively Plug and Play (PnP) devices set NoInstallClass in their respective registry keys.

A **ClassInstall32** section can contain **AddReg** directives to set the **DeviceType**, **DeviceCharacteristics**, and **Security** for devices of its setup class. See the [**INF AddReg Directive**](inf-addreg-directive.md) for more information.

Examples
--------

This example shows the **ClassInstall32** section, along with the named section it references with the [**AddReg directive**](inf-addreg-directive.md), of the INF for the system display class installer.

```cpp
[ClassInstall32] 
AddReg=display_class_addreg

[display_class_addreg]
HKR,,,,%DisplayClassName%
HKR,,Installer32,,"Desk.Cpl,DisplayClassInstaller"
HKR,,Icon,,"-1"
```

By contrast, this example shows the add-registry section referenced in the system CD-ROM INF's **ClassInstall32** section. It sets up a class-specific property-page provider for the CD-ROM devices/drivers that it installs. This INF also sets the **SilentInstall** and **NoInstallClass** value entries in the CD-ROM class key to **TRUE** (**1**).

```cpp
[cdrom_class_addreg]
HKR,,,,%CDClassName%
HKR,,EnumPropPages32,,"SysSetup.Dll,CdromPropPageProvider"
HKR,,SilentInstall,,1
HKR,,NoInstallClass,,1
HKR,,Icon,,"101"
```

## See also


[**AddProperty**](inf-addproperty-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DelProperty**](inf-delproperty-directive.md)

[**DelReg**](inf-delreg-directive.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[***Models***](inf-models-section.md)

[**RenFiles**](inf-renfiles-directive.md)

[**SetupDiBuildClassInfoListEx**](https://msdn.microsoft.com/library/windows/hardware/ff550911)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**UpdateInis**](inf-updateinis-directive.md)

[**Version**](inf-version-section.md)

 

 






