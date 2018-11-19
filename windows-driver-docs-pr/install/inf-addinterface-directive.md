---
title: INF AddInterface Directive
description: One or more AddInterface directives can be specified within an INF DDInstall.Interfaces section.
ms.assetid: 9bd3e051-51f9-4624-802b-b841b25d6616
keywords:
- INF AddInterface Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddInterface Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF AddInterface Directive


One or more **AddInterface** directives can be specified within an [**INF DDInstall.Interfaces section**](inf-ddinstall-interfaces-section.md). This directive installs device-specific support for [device interface classes](device-interface-classes.md) exported to higher level components, such as other drivers or applications. The directive typically references an *add-interface-section* , which sets up registry information for the device-specific instance of the device interface class.

```cpp
[DDInstall.Interfaces]
  
AddInterface={InterfaceClassGUID} [,[reference-string] [,[add-interface-section][,flags]]] 
```

An exported device interface class can be one of the system-defined device interface classes, such as those that are defined by kernel streaming, or a new device interface class specified by an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md).

## Entries


<a href="" id="interfaceclassguid"></a>*InterfaceClassGUID*  
Specifies the GUID value that identifies the device interface class. This can be expressed as an explicit GUID value of the form **{**<em>nnnnnnnn</em>**-***nnnn***-***nnnn*-*nnnn***-**<em>nnnnnnnnnnnn</em>**}** or as a %*strkey*% token defined to **"{**<em>nnnnnnnn</em>**-***nnnn***-***nnnn*-*nnnn***-**<em>nnnnnnnnnnnn</em>**}"** in a [**Strings**](inf-strings-section.md) section of the INF file.

For more information about how to create a GUID, see [Using GUIDs in Drivers](https://msdn.microsoft.com/library/windows/hardware/ff565392). For the system-defined interface class GUIDS, see the appropriate header, such as *Ks.h* for the kernel-streaming interface GUIDs.

<a href="" id="reference-string"></a>*reference-string*  
This optional value, associated with the device-specific instance of the specified interface class, can be expressed either as a **"**<em>quoted string</em>**"** or as a %*strkey*% token defined in an [**INF Strings section**](inf-strings-section.md).

PnP function and filter drivers usually omit this value from the **AddInterface=** entries in their INF files. A *reference-string* is used by the *swenum* driver as a placeholder for software devices that are created on demand by using multiple instances of a single interface class. The same *InterfaceClassGUID* value can be specified in INF entries with two or more unique *reference-string*s. Because the I/O manager passes the *reference-string* value as a path component of the interface instance's name whenever it is opened, the installed driver can discriminate between interface instances of the same class for a single device.

<a href="" id="add-interface-section"></a>*add-interface-section*  
References the name of a section elsewhere in the INF file. This typically contains an [**INF AddReg directive**](inf-addreg-directive.md) to set up the registry entries exporting the driver's support of this [device interface class](device-interface-classes.md). For more information, see the following **Remarks** section.

<a href="" id="flags"></a>*flags*  
If specified, this entry must be zero.

Remarks
-------

If the [device interface class](device-interface-classes.md) identified by a specified **{**<em>InterfaceClassGUID</em>**}** is not installed already, the system setup code installs that class in the system. Any INF file that installs a new class also has an [**INF InterfaceInstall32 section**](inf-interfaceinstall32-section.md). This section contains the specified **{**<em>InterfaceClassGUID</em>**}** and references an *interface-install-section* that sets up interface-specific installation operations for that class.

To enable an instance of a device interface class for run-time use by higher level components, a device driver must first call [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) to retrieve the symbolic link name of the device interface instance to enable.  Usually, a PnP function or filter driver makes this call from its [**AddDevice**](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine.  To enable instances of device interfaces provisioned in the INF, the device driver must provide the **{**<em>InterfaceClassGUID</em>**}** and *reference-string* specified in the INF when it calls [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506).  The driver then calls [**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700) to enable the interface using the symbolic link name returned by [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506). 

Each **AddInterface** directive in an [**INF DDInstall.Interfaces section**](inf-ddinstall-interfaces-section.md) can reference an INF-writer-defined *add-interface-section* elsewhere in the INF file. Each INF-writer-defined section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An *add-interface-section* referenced by the **AddInterface** directive has the following form:

```cpp
[add-interface-section]
 
AddReg=add-registry-section[, add-registry-section]...
[AddProperty=add-property-section[, add-property-section] ...]  (Windows Vista and later versions of Windows)
[DelReg=del-registry-section[, del-registry-section] ...]
[DelProperty=del-property-section[, del-property-section] ...]  (Windows Vista and later versions of Windows)
[BitReg=bit-registry-section[,bit-registry-section] ...]
[CopyFiles=@filename | file-list-section[,file-list-section]...]
[DelFiles=file-list-section[,file-list-section]...]
[RenFiles=file-list-section[,file-list-section]...]
[UpdateInis=update-ini-section[, update-ini-section] ...]
[UpdateIniFields=update-inifields-section[, update-inifields-section] ...]
[Ini2Reg=ini-to-registry-section[, ini-to-registry-section] ...]
```

Starting with Windows Vista, you can set device interface properties by including [**INF AddProperty directives**](inf-addproperty-directive.md) in an add-interface section. You can also delete device interface properties by including [**INF DelProperty directives**](inf-delproperty-directive.md) in an *add-interface section*. However, you should use **AddProperty** or **DelProperty** directives only to modify device interface properties that are new to Windows Vista or a later version of Windows operating systems. For device interface properties that were introduced on Windows Server 2003, Windows XP, or Windows 2000, and that have corresponding registry value entries, you should continue to use [**INF AddReg directives**](inf-addreg-directive.md) and [**INF DelReg directives**](inf-delreg-directive.md) to set and delete the device interface properties. These guidelines apply to system-defined properties and custom properties. For more information about how to use the **AddProperty** directive and **DelProperty** directive, see [Using the INF AddProperty Directive and the INF DelProperty Directive](using-the-inf-addproperty-directive-and-the-inf-delproperty-directive.md).

Typically, an *add-interface-section* contains only an [**INF AddReg directive**](inf-addreg-directive.md) that, in turn, references a single *add-registry-section*. The *add-registry-section* is used to store information in the registry about the interfaces supported by the device driver for subsequent use by still higher level drivers and applications.

An *add-registry-section* referenced within an *add-interface-section* is specific to the instances for the device, driver, and interface. It might have a value entry defining a friendly name for the exported device interface instance so that still higher level components can refer to that interface by its friendly name in the user interface.

An **HKR** specified in such an *add-registry-section* section designates the run-time accessible state registry key for a device interface.  The driver can access state stored in this registry key at runtime by calling [**IoOpenDeviceInterfaceRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff549433) to retrieve a HANDLE to the state registry key.  User mode components can query the state by calling [**CM_Open_Device_Interface_Key**](https://msdn.microsoft.com/library/windows/hardware/hh780223).

Examples
--------

This example shows some of the expansion of the *DDInstall*.**Interfaces** section for a particular audio device that supports system-defined kernel-streaming interfaces.

```cpp
; ...
[ESS6881.Device.Interfaces]
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Wave%,ESSAud.Interface.Wave
AddInterface=%KSCATEGORY_RENDER%,%KSNAME_Wave%,ESSAud.Interface.Wave
AddInterface=%KSCATEGORY_CAPTURE%,%KSNAME_Wave%,ESSAud.Interface.Wave
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_Topology%,\
ESSAud.Interface.Topology
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_UART%,WDM.Interface.UART
AddInterface=%KSCATEGORY_RENDER%,%KSNAME_UART%,WDM.Interface.UART
AddInterface=%KSCATEGORY_CAPTURE%,%KSNAME_UART%,WDM.Interface.UART
AddInterface=%KSCATEGORY_AUDIO%,%KSNAME_FMSynth%,WDM.Interface.FMSynth
AddInterface=%KSCATEGORY_RENDER%,%KSNAME_FMSynth%,\
WDM.Interface.FMSynth

[ESSAud.Interface.Wave]
AddReg=ESSAud.Interface.Wave.AddReg

[ESSAud.Interface.Wave.AddReg]
HKR,,CLSID,,%Proxy.CLSID%
HKR,,FriendlyName,,%ESSAud.Wave.szPname%
; ... 
[WDM.Interface.UART]
AddReg=WDM.Interface.UART.AddReg

[WDM.Interface.UART.AddReg]
HKR,,CLSID,,%Proxy.CLSID%
HKR,,FriendlyName,,%WDM.UART.szPname%
; ...
[Strings]
KSCATEGORY_AUDIO="{6994ad04-93ef-11d0-a3cc-00a0c9223196}"
KSCATEGORY_RENDER="{65e8773e-8f56-11d0-a3b9-00a0c9223196}"
KSCATEGORY_CAPTURE="{65e8773d-8f56-11d0-a3b9-00a0c9223196}"
; ...
KSNAME_WAVE="Wave"
KSNAME_UART="UART"
; ...
Proxy.CLSID="{17cca71b-ecd7-11d0-b908-00a0c9223196}"
; ... 
ESSAud.Wave.szPname="ESS AudioDrive" 
; ... 
```

## See also


[**AddProperty**](inf-addproperty-directive.md)

[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[**DelFiles**](inf-delfiles-directive.md)

[**DelProperty**](inf-delproperty-directive.md)

[**DelReg**](inf-delreg-directive.md)

[**Ini2Reg**](inf-ini2reg-directive.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506)

[**IoSetDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff549700)

[**RenFiles**](inf-renfiles-directive.md)

[**UpdateIniFields**](inf-updateinifields-directive.md)

[**UpdateInis**](inf-updateinis-directive.md)

 

 






