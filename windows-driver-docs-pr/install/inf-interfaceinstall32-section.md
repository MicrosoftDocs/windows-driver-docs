---
title: INF InterfaceInstall32 section
description: This section creates one or more new device interface classes.
keywords:
- INF InterfaceInstall32 Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF InterfaceInstall32 section
api_type:
- NA
ms.date: 06/06/2022
---

# INF InterfaceInstall32 Section

This section creates one or more new [device interface classes](./overview-of-device-interface-classes.md). After a new class is created, subsequently installed devices/drivers can register support for the new device interface class by calling [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface).

```inf
[InterfaceInstall32]
 
{InterfaceClassGUID}=install-interface-section[,flags]
...
```

## Entries

_InterfaceClassGUID_  
Specifies a GUID value identifying the newly exported [device interface class](./overview-of-device-interface-classes.md).

To register an instance of the interface class, a device's driver must call [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) with this GUID.  The specified GUID value in this section may also be referenced by an [**INF AddInterface directive**](inf-addinterface-directive.md) in an [**INF _DDInstall_.Interfaces section**](inf-ddinstall-interfaces-section.md).

For more information about how to create a GUID, see [Using GUIDs in Drivers](../kernel/using-guids-in-drivers.md). For the system-defined interface class GUIDS, see the appropriate headers, such as _Ks.h_ for the kernel-streaming interfaces.

_install-interface-section_  
References an INF-writer-defined section, possibly with any of the system-defined extensions, elsewhere in this INF.

_flags_  
If specified, this entry must be zero.

## Remarks

When a specified _InterfaceClassGUID_ is not already installed in the system, that interface class is installed as the corresponding _DDInstall_**.Interfaces** section is processed during device installation or when that device's driver makes the initial call to **IoRegisterDeviceInterface**.

Each _install-interface-section_ name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Any specified _install-interface-section_ has the following general form:

```inf
[interface-install-section] | 
[interface-install-section.nt] | 
[interface-install-section.ntx86] | 
[interface-install-section.ntia64] | (Windows XP and later versions of Windows)
[interface-install-section.ntamd64] | (Windows XP and later versions of Windows)
[interface-install-section.ntarm] | (Windows 8 and later versions of Windows)
[interface-install-section.ntarm64] (Windows 10 and later versions of Windows)
 
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

For more information about the entries in the _interface-install-section_, see [**INF DDInstall Section**](inf-ddinstall-section.md).

Starting with Windows Vista, you can set [device interface class](./overview-of-device-interface-classes.md) properties by including [**INF AddProperty directives**](inf-addproperty-directive.md) in an interface-install section. You can also delete device interface class properties by including [**INF DelProperty directives**](inf-delproperty-directive.md) in an interface-install section. However, you should use an **AddProperty** or **DelProperty** directive only to modify device interface class properties that are new to Windows Vista or later versions of Windows operating systems. For device interface class properties that were introduced on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry value entries, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) to set and delete the device interface class properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **AddProperty** directive and **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

An **AddReg** directive references one or more add-registry sections that set device-interface-specific information in the registry during installation of this interface.

The registry information about this interface class should include at least a friendly name for the new [device interface class](./overview-of-device-interface-classes.md) and whatever information the higher level components need when they open and use this interface.

In addition, such an _install-interface-section_ might use any of the optional directives shown here to specify interface-specific installation operations.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## See also

[**AddProperty**](inf-addproperty-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**ClassInstall32**](inf-classinstall32-section.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)

[**_DDInstall_.Interfaces**](inf-ddinstall-interfaces-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DelProperty**](inf-delproperty-directive.md)

[**DelReg**](inf-delreg-directive.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface)

[**RenFiles**](inf-renfiles-directive.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**UpdateInis**](inf-updateinis-directive.md)
