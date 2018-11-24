---
title: INF AddService Directive
description: An AddService directive is used within an INF DDInstall.Services section or INF DefaultInstall.Services section.
ms.assetid: 3314da8b-3fde-462a-a64d-a0514710663a
keywords:
- INF AddService Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF AddService Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF AddService Directive


**Note**  This directive is not used in INF files that install devices that do not require any drivers, such as modems or display monitors.

 

An **AddService** directive is used within an [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md) or [**INF DefaultInstall.Services section**](inf-defaultinstall-services-section.md). It specifies characteristics of the services associated with drivers, such as how and when the services are loaded, and any dependencies on other underlying legacy drivers or services. Optionally, this directive also sets up event-logging services for the device.

```cpp
[DDInstall.Services] 
 
AddService=ServiceName,[flags],service-install-section
                     [,event-log-install-section[,[EventLogType][,EventName]]]
...
```

## Entries


<a href="" id="servicename"></a>*ServiceName*  
Specifies the name of the service to be installed. For a device, this value is usually a generic name for its driver, such as "sermouse," or some such name. This name must not be localized. It must be the same regardless of the system's local language.

<a href="" id="flags"></a>*flags*  
Specifies one or more (ORed) of the following system-defined flags, defined in *Setupapi.h*, expressed as a hexadecimal value:

<a href="" id="0x00000001--spsvcinst-tagtofront-"></a>**0x00000001** (SPSVCINST_TAGTOFRONT)  
Move the named service's tag to the front of its group order list, thereby ensuring that it is loaded first within that group (unless a subsequently installed device with this INF specification displaces it). INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

<a href="" id="0x00000002--spsvcinst-assocservice-"></a>**0x00000002** (SPSVCINST_ASSOCSERVICE)  
Assign the named service as the PnP function driver (or legacy driver) for the device being installed by this INF file.

Do not specify this flag when installing filter drivers or other driver components not directly associated with a device. Set this flag for only one driver for each [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md).

<a href="" id="0x00000008--spsvcinst-noclobber-displayname-"></a>**0x00000008** (SPSVCINST_NOCLOBBER_DISPLAYNAME)  
Do not overwrite the given service's (optional) friendly name if this service already exists in the system.

<a href="" id="0x00000010--spsvcinst-noclobber-starttype-"></a>**0x00000010** (SPSVCINST_NOCLOBBER_STARTTYPE)  
Do not overwrite the given service's start type if this named service already exists in the system.

<a href="" id="0x00000020--spsvcinst-noclobber-errorcontrol-"></a>**0x00000020** (SPSVCINST_NOCLOBBER_ERRORCONTROL)  
Do not overwrite the given service's error-control value if this named service already exists in the system.

<a href="" id="0x00000040--spsvcinst-noclobber-loadordergroup-"></a>**0x00000040** (SPSVCINST_NOCLOBBER_LOADORDERGROUP)  
Do not overwrite the given service's load-order-group value if this named service already exists in the system. INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

<a href="" id="0x00000080--spsvcinst-noclobber-dependencies--"></a>**0x00000080** (SPSVCINST_NOCLOBBER_DEPENDENCIES)   
Do not overwrite the given service's dependencies list if this named service already exists in the system. INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

<a href="" id="0x00000100--spsvcinst-noclobber-description-"></a>**0x00000100** (SPSVCINST_NOCLOBBER_DESCRIPTION)  
Do not overwrite the given service's (optional) description if this service already exists in the system.

<a href="" id="0x00000400--spsvcinst-clobber-security---windows-xp-and-later-versions-of-windows--"></a>**0x00000400** (SPSVCINST_CLOBBER_SECURITY) (Windows XP and later versions of Windows)   
Overwrite the security settings for the service if this service already exists in the system.

<a href="" id="0x00000800--spsvcsinst-startservice---windows-vista-and-later-versions-of-windows--"></a>**0x00000800** (SPSVCSINST_STARTSERVICE) (Windows Vista and later versions of Windows)   
Start the service after the service is installed. This flag cannot be used to start a service that implements a Plug and Play (PnP) function driver or filter driver for a device. Otherwise, this flag can be used to start a user-mode or kernel-mode service that is managed by the Service Control Manager (SCM).

<a href="" id="0x00001000--spsvcinst-noclobber-requiredprivileges---windows-7-and-later-versions-of-windows-"></a>**0x00001000** (SPSVCINST_NOCLOBBER_REQUIREDPRIVILEGES) (Windows 7 and later versions of Windows)  
Do not overwrite the privileges for the given service if this service already exists in the system.

<a href="" id="service-install-section"></a>*service-install-section*  
References an INF-writer-defined section that contains information for installing the named service for this device (or devices). For more information, see the following **Remarks** section.

<a href="" id="event-log-install-section"></a>*event-log-install-section*  
Optionally references an INF-writer-defined section in which event-logging services for this device (or devices) are set up.

<a href="" id="eventlogtype"></a>*EventLogType*  
Optionally specifies one of **System**, **Security**, or **Application**. If omitted, this defaults to **System**, which is almost always the appropriate value for the installation of device drivers.

For example, an INF would specify **Security** only if the to-be-installed driver provides its own security support.

<a href="" id="eventname"></a>*EventName*  
Optionally specifies a name to use for the event log. If omitted, this defaults to the given *ServiceName*.

Remarks
-------

The system-defined and case-insensitive extensions can be inserted into a <em>DDInstall</em>**.Services** section that contains an **AddService** directive in cross-operating system and/or cross-platform INF files to specify platform-specific or OS-specific installations.

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddService** directive must reference a named *service-install-section* elsewhere in the INF file. Each such section has the following form:

```cpp
[service-install-section]
 
[DisplayName=name]
[Description=description-string]
ServiceType=type-code
StartType=start-code
ErrorControl=error-control-level
ServiceBinary=path-to-service
[StartName=driver-object-name]
[AddReg=add-registry-section[, add-registry-section] ...]
[DelReg=del-registry-section[, del-registry-section] ...]
[BitReg=bit-registry-section[,bit-registry-section] ...]
[LoadOrderGroup=load-order-group-name]
[Dependencies=depend-on-item-name[,depend-on-item-name]
[Security="security-descriptor-string"]...]
```

Each *service-install-section* must have at least the **ServiceType**, **StartType**, **ErrorControl**, and **ServiceBinary** entries as shown here. However, the remaining entries are optional.

### Service-Install Section Entries and Values

<a href="" id="displayname-name"></a>**DisplayName**=*name*  
Specifies a friendly name for the service/driver, usually, for ease of localization, expressed as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF file.

<a href="" id="description-description-string"></a>**Description**=*description-string*  
Optionally specifies a string that describes the service, usually expressed as a %*strkey*% token defined in a **Strings** section of the INF file.

This string gives the user more information about the service than the **DisplayName**. For example, the **DisplayName** might be something like "DHCP Client" and the Description might be something like "Manages network configuration by registering and updating IP addresses and DNS names".

The *description-string* should be long enough to be descriptive but not so long as to be awkward. If a *description-string* contains any %*strkey*% tokens, each token can represent a maximum of 511 characters. The total string, after any string token substitutions, should not exceed 1024 characters.

<a href="" id="servicetype-type-code"></a>**ServiceType**=*type-code*  
The type-code for a kernel-mode device driver must be set to 0x00000001 (SERVICE_KERNEL_DRIVER).

The *type-code* for a Microsoft Win32 service that is installed for a device should be set to **0x00000010** (SERVICE_WIN32_OWN_PROCESS) or **0x00000020** (SERVICE_WIN32_SHARE_PROCESS). If the Win32 service can interact with the desktop, the type-code value should be combined with **0x00000100** (SERVICE_INTERACTIVE_PROCESS).

The *type-code* for a highest level network driver, such as a redirector, or a file system driver, should be set to **0x00000002** (SERVICE_FILE_SYSTEM_DRIVER).

The SERVICE_xxxx constants are defined in *Wdm.h* and *Ntddk.h*.

<a href="" id="starttype-start-code"></a>**StartType**=*start-code*  
Specifies when to start the driver as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation.

<a href="" id="0x0--service-boot-start-"></a>**0x0** (SERVICE_BOOT_START)  
Indicates a driver started by the operating system loader.

This value must be used for drivers of devices required for loading the operating system.

<a href="" id="0x1--service-system-start-"></a>**0x1** (SERVICE_SYSTEM_START)  
Indicates a driver started during operating system initialization.

This value should be used by PnP drivers that do device detection during initialization but are not required to load the system.

For example, a PnP driver that can also detect a legacy device should specify this value in its INF so that its [*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine is called to find the legacy device, even if that device cannot be enumerated by the PnP manager.

<a href="" id="0x2--service-auto-start-"></a>**0x2** (SERVICE_AUTO_START)  
Indicates a driver started by the service control manager during system startup.

This value should never be used in the INF files for WDM or PnP device drivers.

<a href="" id="0x3--service-demand-start-"></a>**0x3** (SERVICE_DEMAND_START)  
Indicates a driver started on demand, either by the PnP manager when the corresponding device is enumerated or possibly by the service control manager in response to an explicit user demand for a non-PnP device.

This value should be used in the INF files for all WDM drivers of devices that are not required to load the system and for all PnP device drivers that are neither required to load the system nor engaged in device detection.

<a href="" id="0x4--service-disabled-"></a><strong>0x4 (</strong>SERVICE_DISABLED)  
Indicates a driver that cannot be started.

This value can be used to temporarily disable the driver services for a device. However, a device/driver cannot be installed if this value is specified in the service-install section of its INF file.

For more information about **StartType**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

<a href="" id="errorcontrol-error-control-level"></a>**ErrorControl**=*error-control-level*  
Specifies the level of error control as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation.

<a href="" id="0x0--service-error-ignore-"></a>**0x0** (SERVICE_ERROR_IGNORE)  
If the driver fails to load or initialize, proceed with system startup and do not display a warning to the user.

<a href="" id="0x1--service-error-normal-"></a>**0x1** (SERVICE_ERROR_NORMAL)  
If the driver fails to load or initialize its device, system startup should proceed but display a warning to the user.

<a href="" id="0x2--service-error-severe-"></a>**0x2** (SERVICE_ERROR_SEVERE)  
If the driver fails to load, system startup should switch to the registry's **LastKnownGood** control set and continue system startup, even if the driver again indicates a loading or device/driver initialization error.

<a href="" id="0x3--service-error-critical-"></a>**0x3** (SERVICE_ERROR_CRITICAL)  
If the driver fails to load and system startup is not using the registry's **LastKnownGood** control set, switch to **LastKnownGood** and try again.

If startup still fails when using **LastKnownGood**, run a bug-check routine. (*Only* devices/drivers necessary for the system to boot specify this value in their INF files.)

<a href="" id="servicebinary-path-to-service"></a>**ServiceBinary**=*path-to-service*  
Specifies the path of the binary for the service, expressed as *%dirid%\\filename*.

The *dirid* number is either a custom directory identifier or one of the system-defined directory identifiers described in [Using Dirids](using-dirids.md). The given *filename* specifies a file already transferred (see the [**INF CopyFiles Directive**](inf-copyfiles-directive.md)) from the source distribution media to that directory on the target computer.

<a href="" id="startname-driver-object-name"></a>**StartName**=*driver-object-name*  
This optional entry specifies the name of the driver object that represents this device/driver. If *type-code* specifies **1** (SERVICE_KERNEL_DRIVER) or **2** (SERVICE_FILE_SYSTEM_DRIVER), this name is the driver object name that the I/O manager uses to load the driver.

<a href="" id="addreg-add-registry-section--add-registry-section----"></a>**AddReg**=*add-registry-section*\[**,**<em>add-registry-section</em>\]...  
References one or more INF-writer-defined *add-registry-sections* in which any registry information pertinent to the newly installed services is set up. An **HKR** specification in such an *add-registry-section* designates the **HKLM\\System\\CurrentControlSet\\Services\\ServiceName** registry key. For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

This directive is rarely used in a service-install-section.

<a href="" id="delreg-del-registry-section--del-registry-section----"></a>**DelReg**=*del-registry-section*\[**,**<em>del-registry-section</em>\]...  
References one or more INF-writer-defined *del-registry-sections* in which pertinent registry information for an already installed services is removed. An **HKR** specification in such a *del-registry-section* designates the **HKLM\\System\\CurrentControlSet\\Services\\ServiceName** registry key. For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

This directive is almost never used in a *service-install-section*, but it might be used in an INF that "updates" the registry for a previous installation of the same device/driver services.

<a href="" id="bitreg-bit-registry-section--bit-registry-section----"></a>**BitReg**=*bit-registry-section*\[**,**<em>bit-registry-section</em>\]...  
Is valid in a *service-install-section* but almost never used. An **HKR** specification in such a *bit-registry-section* also designates the **HKLM\\System\\CurrentControlSet\\Services\\ServiceName** registry key.

<a href="" id="loadordergroup-load-order-group-name"></a>**LoadOrderGroup**=*load-order-group-name*  
This optional entry identifies the load order group of which this driver is a member. It can be one of the "standard" load order groups, such as **SCSI** class or **NDIS**.

In general, this entry is unnecessary for devices with WDM drivers or for exclusively PnP devices, unless there are legacy dependencies on such a group. However, this entry can be useful if device detection is supported by loading a group of drivers in a particular order.

For more information about **LoadOrderGroup**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

<a href="" id="dependencies-depend-on-item-name--depend-on-item-name----"></a>**Dependencies**=*depend-on-item-name*\[**,**<em>depend-on-item-name</em>\]...  
Each *depend-on-item-name* item in a dependencies list specifies the name of a service or load-order group on which the device/driver depends.

If the *depend-on-item-name* specifies a service, the service that must be running before this driver is started. For example, the INF for the system-supplied Win32 TCP/IP print services depends on the support of the underlying (kernel-mode) TCP/IP transport stack. Consequently, the INF for the TCP/IP print services specifies this entry as **Dependencies=TCPIP**.

A *depend-on-item-name* can specify a load order group on which this device/driver depends. Such a driver is started only if at least one member of the specified group was started. Precede the group name with a plus sign (+). For example, the system RAS services INF might have an entry like **Dependencies = +NetBIOSGroup,RpcSS** that lists both a load-order group and a service.

<a href="" id="security--security-descriptor-string-"></a>**Security**="*security-descriptor-string*"  
Specifies a security descriptor, to be applied to the service. This security descriptor specifies the permissions that are required to perform such operations as starting, stopping, and configuring the service. The *security-descriptor-string* value is a string with tokens to indicate the DACL (**D:**) security component.

For information about security descriptor strings, see [Security Descriptor Definition Language (Windows)](https://msdn.microsoft.com/library/windows/desktop/aa379567). For information about the format of security descriptor strings, see Security Descriptor Definition Language (Windows).

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

### Specifying Driver Load Order

The operating system loads drivers according to the *service-install-section*  **StartType** value, as follows:

-   During the system boot start phase, the operating system loads all **0x0** (SERVICE_BOOT_START) drivers.
-   During the system start phase, the operating system first loads all WDM and PnP drivers for which the PnP manager finds device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) in the registry **..\\Enum** tree (whether their INF files specify **0x01** for SERVICE_SYSTEM_START or **0x03** for SERVICE_DEMAND_START).Then the operating system loads all remaining SERVICE_SYSTEM_START drivers.
-   During the system auto-start phase, the operating system loads all remaining SERVICE_AUTO_START drivers.

For more information about **Dependencies**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

### Promoting a Driver's StartType at Boot Depending on Boot Scenario

Depending on the boot scenario, you can use the **BootFlags** registry value to control when the operating system should promote a driver's **StartType** value to 0x0 (SERVICE_BOOT_START). You can specify one or more (ORed) of the following numeric values, expressed as a hexadecimal value:

-   0x1 (CM_SERVICE_NETWORK_BOOT_LOAD) indicates the driver should be promoted if booting from the network.

-   0x2 (CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from a VHD.

-   0x4 (CM_SERVICE_USB_DISK_BOOT_LOAD) indicates the driver should be promoted to if booting from a USB disk.

-   0x8 (CM_SERVICE_SD_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from SD storage.

-   0x10 (CM_SERVICE_USB3_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from a disk on a USB 3.0 controller.

-   0x20 (CM_SERVICE_MEASURED_BOOT_LOAD) indicates the driver should be promoted if booting while measured boot is enabled.

-   0x40 (CM_SERVICE_VERIFIER_BOOT_LOAD) indicates the driver should be promoted if booting with verifier boot enabled.

-   0x80 (CM_SERVICE_WINPE_BOOT_LOAD) indicates the driver should be promoted if booting to WinPE.

The *service-install-section* has the following general form:

```cpp
[service-install-section]
AddReg=add-registry-section
...

[add-registry-section]
HKR,,BootFlags,0x00010003,0x14 ; CM_SERVICE_USB3_DISK_BOOT_LOAD|CM_SERVICE_USB_DISK_BOOT_LOAD
```

### Registering for Event Logging

An **AddService** directive can also reference an *event-log-install-section* elsewhere in the INF file. Each such section has the following form:

```cpp
[event-log-install-section]
 
AddReg=add-registry-section[, add-registry-section]... 
[DelReg=del-registry-section[, del-registry-section]...] 
[BitReg=bit-registry-section[,bit-registry-section]...]
 ...
```

For a typical device/driver INF file, the *event-log-install-section* uses only the **AddReg** directive to set up an event-logging message file for the driver. An **HKR** specification in an *add-registry-section* designates the **HKLM\\System\\CurrentControlSet\\Services\\EventLog\\**<em>EventLogType</em>**\\**<em>EventName</em> registry key. This event-logging *add-registry-section* has the following general form:

```cpp
[drivername_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"path\IoLogMsg.dll;path\driver.sys"
HKR,,TypesSupported,0x00010001,7 
```

In particular, the section adds two value entries in the registry subkey created for the device/driver, as follows:

-   The value entry named **EventMessageFile** is of type [REG_EXPAND_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), as specified by the FLG_ADDREG_TYPE_EXPAND_SZ value **0x00020000**. Its value, enclosed in double quotation marks ("), associates the system-supplied *IoLogMsg.dll* (but it could associate another logging DLL) with the driver binary file. Usually, the paths to each of these files are specified as follows:

    *%%SystemRoot%%\\System32\\IoLogMsg.dll*

    *%%SystemRoot%%\\System32\\drivers\\driver.sys*

-   The value entry named **TypesSupported** is of type [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types), as specified by the FLG_ADDREG_TYPE_DWORD value **0x00010001**.

    For drivers, this value should be **7**. This value is equivalent to the bitwise OR of EVENTLOG_SUCCESS, EVENTLOG_ERROR_TYPE, EVENTLOG_WARNING_TYPE, and EVENTLOG_INFORMATION_TYPE, without setting the EVENTLOG_AUDIT_*XXX* bits.

An *event-log-install-section* can also use the [**DelReg**](inf-delreg-directive.md) directive to remove a previously installed event-log message file, by explicitly deleting the existing **EventMessageFile** and **TypesSupported** value entries, if a driver binary is being superseded by a newly installed driver. (See also [**INF DelService Directive**](inf-delservice-directive.md).)

While a [**BitReg**](inf-bitreg-directive.md) directive is also valid within an INF-writer-defined *event-log-install*-*section*, it is almost never used, because the standard value entries for device driver event logging are not bitmasks.

Examples
--------

This example shows the service-install and event-log-install sections referenced by the **AddService** directive as already shown earlier in the example for [***DDInstall*.Services**](inf-ddinstall-services-section.md).

```cpp
[sermouse_Service_Inst]
DisplayName    = %sermouse.SvcDesc%
ServiceType    = 1                   ; = SERVICE_KERNEL_DRIVER
StartType      = 3                   ; = SERVICE_DEMAND_START
ErrorControl   = 1                   ; = SERVICE_ERROR_NORMAL
ServiceBinary  = %12%\sermouse.sys
LoadOrderGroup = Pointer Port

[sermouse_EventLog_Inst]
AddReg = sermouse_EventLog_AddReg

[sermouse_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll;
       %%SystemRoot%%\System32\drivers\sermouse.sys"
;
; Preceding entry on single line in INF file. Enclosing quotation marks 
; prevent the semicolon from being interpreted as a comment.
;
HKR,,TypesSupported,0x00010001,7

[mouclass_Service_Inst]
DisplayName    = %mouclass.SvcDesc%
ServiceType    = 1                   ; = SERVICE_KERNEL_DRIVER
StartType      = 1                   ; = SERVICE_SYSTEM_START
ErrorControl   = 1                   ; = SERVICE_ERROR_NORMAL
ServiceBinary  = %12%\mouclass.sys
LoadOrderGroup = Pointer Class

[mouclass_EventLog_Inst]
AddReg = mouclass_EventLog_AddReg

[mouclass_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll;
       %%SystemRoot%%\System32\drivers\mouclass.sys"
HKR,,TypesSupported,0x00010001,7
; ...
[Strings]
; ...
sermouse.SvcDesc = "Serial Mouse Driver"
mouclass.SvcDesc = "Mouse Class Driver"
```

The example in the reference for the [***DDInstall*.HW**](inf-ddinstall-hw-section.md) section, described earlier, also shows some service-install sections referenced by the **AddService** directive to set up PnP upper-filter drivers.

## See also


[**AddReg**](inf-addreg-directive.md)

[**BitReg**](inf-bitreg-directive.md)

[**CopyFiles**](inf-copyfiles-directive.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)

[**DelService**](inf-delservice-directive.md)

[**DestinationDirs**](inf-destinationdirs-section.md)

[**Strings**](inf-strings-section.md)

 

 






