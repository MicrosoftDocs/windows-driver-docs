---
title: INF InterfaceInstall32 Section
description: This section creates one or more new device interface classes.
ms.assetid: 7cd576a7-aa5b-486c-a622-cdcb9e7448b5
keywords:
- INF InterfaceInstall32 Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF InterfaceInstall32 Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF InterfaceInstall32 Section


This section creates one or more new [device interface classes](device-interface-classes.md). After a new class is created, subsequently installed devices/drivers can be registered to support the new device interface class by using [**INF *DDInstall*.Interfaces sections**](inf-ddinstall-interfaces-section.md) in their respective INF files, or by calling [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506).

```cpp
[InterfaceInstall32]
 
{InterfaceClassGUID}=install-interface-section[,flags]
...
```

## Entries


<a href="" id="interfaceclassguid"></a>*InterfaceClassGUID*  
Specifies a GUID value identifying the newly exported [device interface class](device-interface-classes.md).

To register an instance of the interface class, a specified GUID value in this section must be referenced by an [**INF AddInterface directive**](inf-addinterface-directive.md) in an [**INF *DDInstall*.Interfaces section**](inf-ddinstall-interfaces-section.md), or else the newly installed device's driver must call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) with this GUID.

For more information about how to create a GUID, see [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392). For the system-defined interface class GUIDS, see the appropriate headers, such as *Ks.h* for the kernel-streaming interfaces.

<a href="" id="install-interface-section"></a>*install-interface-section*  
References an INF-writer-defined section, possibly with any of the system-defined extensions, elsewhere in this INF.

<a href="" id="flags"></a>*flags*  
If specified, this entry must be zero.

Remarks
-------

When a specified *InterfaceClassGUID* is not already installed in the system, that interface class is installed as the corresponding <em>DDInstall</em>**.Interfaces** section is processed by the [SetupAPI](setupapi.md) functions during device installation or when that device's driver makes the initial call to **IoRegisterDeviceInterface**.

Each *install-interface-section* name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Any specified *install-interface-section* has the following general form:

```cpp
[interface-install-section] | 
[interface-install-section.nt] | 
[interface-install-section.ntx86] | 
[interface-install-section.ntia64] | (Windows XP and later versions of Windows)
[interface-install-section.ntamd64] (Windows XP and later versions of Windows)
 
AddReg=add-registry-section[, add-registry-section] ...
[AddProperty=add-property-section[, add-property-section] ...]  (Windows Vista and later versions of Windows)
[Copyfiles=@filename | file-list-section[, file-list-section] ...]
[DelReg=del-registry-section[, del-registry-section] ...]
[DelProperty=del-property-section[, del-property-section] ...]  (Windows Vista and later versions of Windows)
[BitReg=bit-registry-section[,bit-registry-section]...]
[Delfiles=file-list section[, file-list-section] ...]
[Renfiles=file-list-section[, file-list-section] ...]
[UpdateInis=update-ini-section[,update-ini-section]...]
[UpdateIniFields=update-inifields-section[,update-inifields-section]...]
[Ini2Reg=ini-to-registry-section[,ini-to-registry-section]...]
...
```

For more information about the entries in the *interface-install-section*, see [**INF DDInstall Section**](inf-ddinstall-section.md).

Starting with Windows Vista, you can set [device interface class](device-interface-classes.md) properties by including [**INF AddProperty directives**](inf-addproperty-directive.md) in an interface-install section. You can also delete device interface class properties by including [**INF DelProperty directives**](inf-delproperty-directive.md) in an interface-install section. However, you should use an **AddProperty** or **DelProperty** directive only to modify device interface class properties that are new to Windows Vista or later versions of Windows operating systems. For device interface class properties that were introduced on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry value entries, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) to set and delete the device interface class properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **AddProperty** directive and **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

An **AddReg** directive references one or more add-registry sections that set device-interface-specific information in the registry during installation of this interface. An **HKR** specified in such an add-registry section designates the **..DeviceClasses\\{**<em>InterfaceClassGUID</em>**}** key.

The registry information about this interface class should include at least a friendly name for the new [device interface class](device-interface-classes.md) and whatever information the higher level components need when they open and use this interface.

In addition, such an *install-interface-section* might use any of the optional directives shown here to specify interface-specific installation operations.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, and **.ntamd64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## See also


[**AddProperty**](inf-addproperty-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DelProperty**](inf-delproperty-directive.md)

[**DelReg**](inf-delreg-directive.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)

[**RenFiles**](inf-renfiles-directive.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**UpdateInis**](inf-updateinis-directive.md)

 

 






