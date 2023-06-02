---
title: INF AddService directive
description: An AddService directive is used within an INF DDInstall.Services section or INF DefaultInstall.Services section.
keywords:
- INF AddService Directive Device and Driver Installation
topic_type:
- apiref
ms.topic: reference
api_name:
- INF AddService Directive
api_type:
- NA
ms.date: 06/23/2022
---

# INF AddService directive

> [!NOTE]
> This directive is not used in INF files that install devices that do not require any drivers, such as modems or display monitors.

An **AddService** directive is used within an [**INF *DDInstall*.Services section**](inf-ddinstall-services-section.md) or [**INF DefaultInstall.Services section**](inf-defaultinstall-services-section.md). It specifies characteristics of the services associated with drivers, such as how and when the services are loaded, and any dependencies on other underlying legacy drivers or services. Optionally, this directive also sets up event-logging services for the device.

```inf
[DDInstall.Services] 
 
AddService=ServiceName,[flags],service-install-section
                     [,event-log-install-section[,[EventLogType][,EventName]]]
...
```

## Entries

*ServiceName*  
Specifies the name of the service to be installed. The name should be unique enough that it is unlikely to conflict with a service installed by a different INF file. For example, the service name could include a brief abbreviation of your company name as a prefix or suffix. This name must not be localized. It must be the same regardless of the system's local language.

*flags*  
Specifies one or more (ORed) of the following system-defined flags, defined in *Setupapi.h*, expressed as a hexadecimal value:

**0x00000001** (SPSVCINST_TAGTOFRONT)  
Move the named service's tag to the front of its group order list, thereby ensuring that it is loaded first within that group (unless a subsequently installed device with this INF specification displaces it). INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

**0x00000002** (SPSVCINST_ASSOCSERVICE)  
Assign the named service as the PnP function driver (or legacy driver) for the device being installed by this INF file.

To indicate that a service is the function driver for a device, the service should specify the **SPSVCINST_ASSOCSERVICE** flag in the **AddService** directive.  For a service such as a filter driver or other driver component, the flag should not be used.

Every device driver INF should have exactly one associated service.  The INF does not require an associated service if it is an [Extension INF](using-an-extension-inf-file.md) or uses the Include/Needs directives to inherit the associated service from another INF.  For devices that do not require a function driver, the NULL driver can be specified as the associated service as follows:

```inf
AddService = ,2
```

**0x00000008** (SPSVCINST_NOCLOBBER_DISPLAYNAME)  
Do not overwrite the given service's (optional) friendly name if this service already exists in the system.

**0x00000010** (SPSVCINST_NOCLOBBER_STARTTYPE)  
Do not overwrite the given service's start type if this named service already exists in the system.

**0x00000020** (SPSVCINST_NOCLOBBER_ERRORCONTROL)  
Do not overwrite the given service's error-control value if this named service already exists in the system.

**0x00000040** (SPSVCINST_NOCLOBBER_LOADORDERGROUP)  
Do not overwrite the given service's load-order-group value if this named service already exists in the system. INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

**0x00000080** (SPSVCINST_NOCLOBBER_DEPENDENCIES)  
Do not overwrite the given service's dependencies list if this named service already exists in the system. INF files that install exclusively PnP devices and devices with WDM drivers should not set this flag.

**0x00000100** (SPSVCINST_NOCLOBBER_DESCRIPTION)  
Do not overwrite the given service's (optional) description if this service already exists in the system.

**0x00000400** (SPSVCINST_CLOBBER_SECURITY) (Windows XP and later versions of Windows)  
Overwrite the security settings for the service if this service already exists in the system.

**0x00000800** (SPSVCSINST_STARTSERVICE) (Windows Vista and later versions of Windows)  
Start the service after the service is installed. This flag cannot be used to start a service that implements a Plug and Play (PnP) function driver or filter driver for a device. Otherwise, this flag can be used to start a user-mode or kernel-mode service that is managed by the Service Control Manager (SCM).

**0x00001000** (SPSVCINST_NOCLOBBER_REQUIREDPRIVILEGES) (Windows 7 and later versions of Windows)  
Do not overwrite the privileges for the given service if this service already exists in the system.

**0x00002000** (SPSVCINST_NOCLOBBER_TRIGGERS) (Windows 10 Version 2004 and later versions of Windows)  
Do not overwrite the triggers for the given service if this service already exists in the system and has existing triggers. See the AddTrigger directive below for more information on triggers.

**0x00004000** (SPSVCINST_NOCLOBBER_SERVICESIDTYPE) (Windows 10 Version 2004 and later versions of Windows)  
Do not overwrite the SID info for the given service if this service already exists in the system and has existing SID info. See the ServiceSidType directive below for more information.

**0x00008000** (SPSVCINST_NOCLOBBER_DELAYEDAUTOSTART) (Windows 10 Version 2004 and later versions of Windows)  
Do not overwrite the delayed auto start value for the given service if this service already exists in the system and has an existing value. See the DelayedAutoStart directive below for more information.

**0x00020000** (SPSVCINST_NOCLOBBER_FAILUREACTIONS) (Windows 11 version 22H2 and later versions of Windows)  
Do not overwrite the failure actions for the given service if this service already exists in the system and has existing failure actions. See the FailureActions directive below for more information on failure actions.

**0x00040000** (SPSVCINST_NOCLOBBER_BOOTFLAGS) (Windows 11 Version **TBD** and later versions of Windows) 
Do not overwrite the boot flags value for the given service if this service already exists in the system and has an existing value. See the BootFlags directive below for more information

*service-install-section*  
References an INF-writer-defined section that contains information for installing the named service for this device (or devices). For more information, see the following **Remarks** section.

*event-log-install-section*  
Optionally references an INF-writer-defined section in which event-logging services for this device (or devices) are set up.

*EventLogType*  
Optionally specifies one of **System**, **Security**, or **Application**. If omitted, this defaults to **System**, which is almost always the appropriate value for the installation of device drivers.

For example, an INF would specify **Security** only if the to-be-installed driver provides its own security support.

*EventName*  
Optionally specifies a name to use for the event log. If omitted, this defaults to the given *ServiceName*.

## Remarks

The system-defined and case-insensitive extensions can be inserted into a _DDInstall_**.Services** section that contains an **AddService** directive in cross-operating system and/or cross-platform INF files to specify platform-specific or OS-specific installations.

Each INF-writer-created section name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

An **AddService** directive must reference a named *service-install-section* elsewhere in the INF file. Each such section has the following form:

```inf
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
[BootFlags=value] (Windows 11 build Version <TBD> and later versions of Windows) 
[LoadOrderGroup=load-order-group-name]
[Dependencies=depend-on-item-name[,depend-on-item-name]
[Security="security-descriptor-string"]...]
[RequiredPrivileges=privilege-name[,privilege-name]...] (Windows 7 and later versions of Windows)
[ServiceSidType=value] (Windows 10 Version 2004 and later versions of Windows)
[DelayedAutoStart=value] (Windows 10 Version 2004 and later versions of Windows)
[AddTrigger=service-trigger-install-section[, service-trigger-install-section, ...]] (Windows 10 Version 2004 and later versions of Windows)
[FailureActions=service-failure-actions-install-section] (Windows 11 version 22H2 and later versions of Windows)
```

Each *service-install-section* must have at least the **ServiceType**, **StartType**, **ErrorControl**, and **ServiceBinary** entries as shown here. However, the remaining entries are optional.

### Service-Install Section Entries and Values

**DisplayName**=*name*  
Specifies a friendly name for the service/driver, usually, for ease of localization, expressed as a %*strkey*% token defined in a [**Strings**](inf-strings-section.md) section of the INF file.

**Description**=*description-string*  
Optionally specifies a string that describes the service, usually expressed as a %*strkey*% token defined in a **Strings** section of the INF file.

This string gives the user more information about the service than the **DisplayName**. For example, the **DisplayName** might be something like "DHCP Client" and the Description might be something like "Manages network configuration by registering and updating IP addresses and DNS names".

The *description-string* should be long enough to be descriptive but not so long as to be awkward. If a *description-string* contains any %*strkey*% tokens, each token can represent a maximum of 511 characters. The total string, after any string token substitutions, should not exceed 1024 characters.

**ServiceType**=*type-code*  
The type-code for a kernel-mode device driver must be set to 0x00000001 (SERVICE_KERNEL_DRIVER).

The *type-code* for a Microsoft Win32 service that is installed for a device should be set to **0x00000010** (SERVICE_WIN32_OWN_PROCESS) or **0x00000020** (SERVICE_WIN32_SHARE_PROCESS). If the Win32 service can interact with the desktop, the type-code value should be combined with **0x00000100** (SERVICE_INTERACTIVE_PROCESS).

The *type-code* for a highest level network driver, such as a redirector, or a file system driver, should be set to **0x00000002** (SERVICE_FILE_SYSTEM_DRIVER).

The SERVICE_xxxx constants are defined in *Wdm.h* and *Ntddk.h*.

**StartType**=*start-code*  
Specifies when to start the driver as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation.

**0x0** (SERVICE_BOOT_START)  
Indicates a driver started by the operating system loader.

This value must be used for drivers of devices required for loading the operating system.

**0x1** (SERVICE_SYSTEM_START)  
Indicates a driver started during operating system initialization.

This value should be used by PnP drivers that do device detection during initialization but are not required to load the system.

For example, a PnP driver that can also detect a legacy device should specify this value in its INF so that its [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine is called to find the legacy device, even if that device cannot be enumerated by the PnP manager.

**0x2** (SERVICE_AUTO_START)  
Indicates a service started by the service control manager during system startup.

This value should never be used in the INF files for WDM or PnP device drivers.

**0x3** (SERVICE_DEMAND_START)  
Indicates a service started on demand, either by the PnP manager when the corresponding device is enumerated or possibly by the service control manager in response to an explicit user demand for a non-PnP device.

This value should be used in the INF files for all WDM drivers of devices that are not required to load the system and for all PnP device drivers that are neither required to load the system nor engaged in device detection.

**0x4** (SERVICE_DISABLED)  
Indicates a service that cannot be started.

This value can be used to temporarily disable the driver services for a device. However, a device/driver cannot be installed if this value is specified in the service-install section of its INF file.

For more information about **StartType**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

**ErrorControl**=*error-control-level*  
Specifies the level of error control as one of the following numeric values, expressed either in decimal or, as shown in the following list, in hexadecimal notation.

**0x0** (SERVICE_ERROR_IGNORE)  
If the driver fails to load or initialize, proceed with system startup and do not display a warning to the user.

**0x1** (SERVICE_ERROR_NORMAL)  
If the driver fails to load or initialize its device, system startup should proceed but display a warning to the user.

**0x2** (SERVICE_ERROR_SEVERE)  
If the driver fails to load, system startup should switch to the registry's **LastKnownGood** control set and continue system startup, even if the driver again indicates a loading or device/driver initialization error.

**0x3** (SERVICE_ERROR_CRITICAL)  
If the driver fails to load and system startup is not using the registry's **LastKnownGood** control set, switch to **LastKnownGood** and try again.

If startup still fails when using **LastKnownGood**, run a bug-check routine. (*Only* devices/drivers necessary for the system to boot specify this value in their INF files.)

**ServiceBinary**=*path-to-service*  
Specifies the path of the binary for the service, expressed as *%dirid%\\filename*.

The *dirid* number is either a custom directory identifier or one of the system-defined directory identifiers described in [Using Dirids](using-dirids.md). The given *filename* specifies a file already transferred (see the [**INF CopyFiles Directive**](inf-copyfiles-directive.md)) from the source distribution media to that directory on the target computer.

**StartName**=*driver-object-name*  
This optional entry specifies the name of the driver object that represents this device/driver. If *type-code* specifies **1** (SERVICE_KERNEL_DRIVER) or **2** (SERVICE_FILE_SYSTEM_DRIVER), this name is the driver object name that the I/O manager uses to load the driver.

**AddReg**=*add-registry-section*[**,**_add-registry-section_]...  
References one or more INF-writer-defined *add-registry-sections* in which any registry information pertinent to the newly installed services is set up. For more information, see [**INF AddReg Directive**](inf-addreg-directive.md).

**DelReg**=*del-registry-section*[**,**_del-registry-section_]...  
References one or more INF-writer-defined *del-registry-sections* in which pertinent registry information for an already installed services is removed. For more information, see [**INF DelReg Directive**](inf-delreg-directive.md).

This directive is almost never used in a *service-install-section*, but it might be used in an INF that "updates" the registry for a previous installation of the same device/driver services.

**BitReg**=*bit-registry-section*[**,**_bit-registry-section_]...  
Is valid in a *service-install-section* but almost never used.
 
**BootFlags**=*value*
> [!NOTE]
> This value can only be used with kernel-mode driver services and is only available with Windows 11 Version **TBD** and above 

Optionally specifies when the operating system should promote a driver's StartType value to 0x0 (SERVICE_BOOT_START). You can specify one or more (ORed) of the following numeric values, expressed as hexadecimal values.  

**0x1** (CM_SERVICE_NETWORK_BOOT_LOAD)   
Indicates the driver should be promoted if booting from the network.  

**0x2** (CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD)   
Indicates the driver should be promoted if booting from a VHD.  

**0x4** (CM_SERVICE_USB_DISK_BOOT_LOAD)   
Indicates the driver should be promoted to if booting from a USB disk.  

**0x8** (CM_SERVICE_SD_DISK_BOOT_LOAD)   
Indicates the driver should be promoted if booting from SD storage.  

**0x10** (CM_SERVICE_USB3_DISK_BOOT_LOAD)   
Indicates the driver should be promoted if booting from a disk on a USB 3.0 controller.  

**0x20** (CM_SERVICE_MEASURED_BOOT_LOAD)  
Indicates the driver should be promoted if booting while measured boot is enabled.  

**0x40** (CM_SERVICE_VERIFIER_BOOT_LOAD)   
Indicates the driver should be promoted if booting with verifier boot enabled.  

**0x80** (CM_SERVICE_WINPE_BOOT_LOAD)   
Indicates the driver should be promoted if booting to WinPE 

**LoadOrderGroup**=*load-order-group-name*  
This optional entry identifies the load order group of which this driver is a member. It can be one of the "standard" load order groups, such as **SCSI** class or **NDIS**.

In general, this entry is unnecessary for devices with WDM drivers or for exclusively PnP devices, unless there are legacy dependencies on such a group. However, this entry can be useful if device detection is supported by loading a group of drivers in a particular order.

For more information about **LoadOrderGroup**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

**Dependencies**=*depend-on-item-name*[**,**_depend-on-item-name_]...  
Each *depend-on-item-name* item in a dependencies list specifies the name of a service or load-order group on which the device/driver depends.

If the *depend-on-item-name* specifies a service, the service that must be running before this driver is started. For example, the INF for the system-supplied Win32 TCP/IP print services depends on the support of the underlying (kernel-mode) TCP/IP transport stack. Consequently, the INF for the TCP/IP print services specifies this entry as **Dependencies=TCPIP**.

A *depend-on-item-name* can specify a load order group on which this device/driver depends. Such a driver is started only if at least one member of the specified group was started. Precede the group name with a plus sign (+). For example, the system RAS services INF might have an entry like **Dependencies = +NetBIOSGroup,RpcSS** that lists both a load-order group and a service.

**Security**="*security-descriptor-string*"  
Specifies a security descriptor, to be applied to the service. This security descriptor specifies the permissions that are required to perform such operations as starting, stopping, and configuring the service. The *security-descriptor-string* value is a string with tokens to indicate the DACL (**D:**) security component.

For information about security descriptor strings, see [Security Descriptor Definition Language (Windows)](/windows/desktop/SecAuthZ/security-descriptor-definition-language). For information about the format of security descriptor strings, see Security Descriptor Definition Language (Windows).

For more information about how to specify security descriptors, see [Creating Secure Device Installations](creating-secure-device-installations.md).

**RequiredPrivileges**=*privilege-name*[**,**_privilege-name_]...
> [!NOTE]
> This value can only be used for *Win32 Services* and is only available on Windows 7 and above.

Each *privilege-name* in the list is the name of a privilege that the service requires.  See [Privilege Constants (Windows)](/windows/win32/secauthz/privilege-constants) for a list of the privilege names. For each privilege name, only the text name is required. For example, the privilege name should be written as "SeAuditPrivilege" but not SE_AUDIT_NAME.

For more information on service required privileges, see [SERVICE_REQUIRED_PRIVILEGES_INFO (Windows)](/windows/win32/api/winsvc/ns-winsvc-service_required_privileges_infow).

**ServiceSidType**=*value*  
> [!NOTE]
> This value can only be used for *Win32 Services* and is only available with Windows 10 Version 2004 and above.

This entry can use any valid value as described in [SERVICE_SID_INFO](/windows/win32/api/winsvc/ns-winsvc-service_sid_info).

**DelayedAutoStart**=*value*  
> [!NOTE]
> This value can only be used for *Win32 Services* and is only available with Windows 10 2004 and above.

Contains the delayed auto-start setting of an auto-start service.

If this member is 0x0, the service is started during system boot. Otherwise, the service is started after other auto-start services are started plus a short delay.

This setting is ignored unless the service is an auto-start service.

For more information, see [this page](/windows/win32/api/winsvc/ns-winsvc-service_delayed_auto_start_info).

**AddTrigger**=*service-trigger-install-section [, service-trigger-install-section, ...]*  
Specifies the trigger events to be registered for the *Win32 service* so that the service can be started or stopped when a trigger event occurs. For more information about service trigger events, see [Service Trigger Events](/windows/desktop/Services/service-trigger-events).

Each named *service-trigger-install-section* referenced by an AddTrigger directive has the following format:

```inf
[service-trigger-install-section]

TriggerType=trigger-type
Action=action-type
SubType=trigger-subtype
[DataItem=data-type,data]
...
```

### Service-Trigger-Install-Section Entries and Values

**TriggerType**=*trigger-type*  
Specifies the service trigger event type in one of the following numeric values, expressed either in decimal or, as is shown in the following list, hexadecimal notation:

**0x1** (SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL)  
Indicates that event is triggered when a device of the specified device interface class arrives or is present when the system starts.

For more information, see [SERVICE_TRIGGER structure](/windows/win32/api/winsvc/ns-winsvc-service_trigger).

**Action**=*action-type*  
Specifies the action to take when the specified trigger event occurs.

**0x1** (SERVICE_TRIGGER_ACTION_SERVICE_START)  
Start the service when the specified trigger event occurs.

**0x2** (SERVICE_TRIGGER_ACTION_SERVICE_STOP)  
Stop the service when the specified trigger event occurs.

For more information, see [SERVICE_TRIGGER structure](/windows/win32/api/winsvc/ns-winsvc-service_trigger).

**SubType**=*trigger-subtype*  
Specifies a GUID that identifies the trigger event subtype. The value depends on the value of the **TriggerType**.

When **TriggerType** is **0x1** (SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL), **SubType** specifies the GUID that identifies the device interface class.

For more information, see [SERVICE_TRIGGER structure](/windows/win32/api/winsvc/ns-winsvc-service_trigger).

**DataItem**=*data-type, data*  
Optionally specifies the trigger-specific data for a service trigger event.

When **TriggerType** is **0x1** (SERVICE_TRIGGER_TYPE_DEVICE_INTERFACE_ARRIVAL), an optional DataItem may be specified with a data-type of **0x2** (SERVICE_TRIGGER_DATA_TYPE_STRING) to scope the device interface class to a specific hardware ID or compatible ID.

For more information, see [SERVICE_TRIGGER_SPECIFIC_DATA_ITEM structure](/windows/win32/api/winsvc/ns-winsvc-service_trigger_specific_data_item)

The best practice for using the **AddTrigger** directive is to trigger start the service on device interface arrival. For more information, see [Win32 Services Interacting with Devices](./best-practices-win32services-interacting-with-devices.md).

> [!NOTE]
> AddTrigger syntax is only available in **Windows 10 Version 2004** and forward.

**FailureActions**=*service-failure-actions-install-section*  
Optionally specifies the action the service controller should take when a service fails.

The service control manager counts the number of times each service has failed since the system booted. The count is reset to 0 if the service has not failed for reset-period seconds. When the service fails for the Nth time, the service controller performs the action specified in element N of the Action list. If N is greater than the number of Actions, the service controller repeats the last action in the list.

The *service-failure-actions-install-section* referenced by a FailureActions directive has the following format:

```inf
[service-failure-actions-install-section]

[ResetPeriod=reset-period]
[NonCrashFailures=value]
Action=failure-action-type,delay
[Action=failure-action-type,delay]
...
```

### Service-Failure-Actions-Install-Section Entries and Values

**ResetPeriod**=*reset-period*  
Specifies the time after which to reset the failure count to zero if there are no failures, in seconds. The failure count is not reset by default when a reset period is not specified.

For more information, see [SERVICE_FAILURE_ACTIONSW structure](/windows/win32/api/winsvc/ns-winsvc-service_failure_actionsw).

**NonCrashFailures**=*value*  
Contains the failure actions flag setting of a service. The setting determines when failure actions are to be executed. A value of 0x0 indicates False and a value of 0x1 indicates True.

For more information, see [SERVICE_FAILURE_ACTIONS_FLAG structure (winsvc.h)](/windows/win32/api/winsvc/ns-winsvc-service_failure_actions_flag).

**Action**=*failure-action-type*,*delay*  
Specifies an action that the service control manager can perform. Multiple Action entries form an ordered list of failure actions.
For more information, see [SC_ACTION structure](/windows/win32/api/winsvc/ns-winsvc-sc_action).

> [!NOTE]
> FailureActions syntax can only be used for *Win32 Services* and is available starting in Windows 11, version 22H2.

### Specifying Driver Load Order

The operating system loads drivers according to the *service-install-section* **StartType** value, as follows:

- During the boot start phase, the operating system loads all **0x0** (SERVICE_BOOT_START) drivers.

- During the system start phase, the operating system first loads all WDM and PnP drivers for which the PnP manager finds device nodes (*devnodes*) (whether their INF files specify **0x01** for SERVICE_SYSTEM_START or **0x03** for SERVICE_DEMAND_START). Then the operating system loads all remaining SERVICE_SYSTEM_START drivers.

- During the auto-start phase, the operating system loads all remaining SERVICE_AUTO_START drivers.

For more information about **Dependencies**, see [Specifying Driver Load Order](specifying-driver-load-order.md).

### Promoting a Driver's StartType at Boot Depending on Boot Scenario

Depending on the boot scenario, you can use the **BootFlags** registry value to control when the operating system should promote a driver's **StartType** value to 0x0 (SERVICE_BOOT_START). You can specify one or more (ORed) of the following numeric values, expressed as a hexadecimal value:

- 0x1 (CM_SERVICE_NETWORK_BOOT_LOAD) indicates the driver should be promoted if booting from the network.

- 0x2 (CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from a VHD.

- 0x4 (CM_SERVICE_USB_DISK_BOOT_LOAD) indicates the driver should be promoted to if booting from a USB disk.

- 0x8 (CM_SERVICE_SD_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from SD storage.

- 0x10 (CM_SERVICE_USB3_DISK_BOOT_LOAD) indicates the driver should be promoted if booting from a disk on a USB 3.0 controller.

- 0x20 (CM_SERVICE_MEASURED_BOOT_LOAD) indicates the driver should be promoted if booting while measured boot is enabled.

- 0x40 (CM_SERVICE_VERIFIER_BOOT_LOAD) indicates the driver should be promoted if booting with verifier boot enabled.

- 0x80 (CM_SERVICE_WINPE_BOOT_LOAD) indicates the driver should be promoted if booting to WinPE.

The *service-install-section* has the following general form:

```inf
[service-install-section]
AddReg=add-registry-section
...

[add-registry-section]
HKR,,BootFlags,0x00010003,0x14 ; CM_SERVICE_USB3_DISK_BOOT_LOAD|CM_SERVICE_USB_DISK_BOOT_LOAD
```

### Registering for Event Logging

An **AddService** directive can also reference an *event-log-install-section* elsewhere in the INF file. Each such section has the following form:

```inf
[event-log-install-section]
 
AddReg=add-registry-section[, add-registry-section]... 
[DelReg=del-registry-section[, del-registry-section]...] 
[BitReg=bit-registry-section[,bit-registry-section]...]
 ...
```

For a typical device/driver INF file, the *event-log-install-section* uses only the **AddReg** directive to set up an event-logging message file for the driver. This event-logging *add-registry-section* has the following general form:

```inf
[drivername_EventLog_AddReg]
HKR,,EventMessageFile,0x00020000,"path\IoLogMsg.dll;path\driver.sys"
HKR,,TypesSupported,0x00010001,7 
```

In particular, the section adds two value entries in the registry subkey created for the device/driver, as follows:

- The value entry named **EventMessageFile** is of type [REG_EXPAND_SZ](/windows/desktop/SysInfo/registry-value-types), as specified by the FLG_ADDREG_TYPE_EXPAND_SZ value **0x00020000**. Its value, enclosed in double quotation marks ("), associates the system-supplied *IoLogMsg.dll* (but it could associate another logging DLL) with the driver binary file. Usually, the paths to each of these files are specified as follows:

    *%%SystemRoot%%\\System32\\IoLogMsg.dll*

    *%%SystemRoot%%\\System32\\drivers\\driver.sys*

- The value entry named **TypesSupported** is of type [REG_DWORD](/windows/desktop/SysInfo/registry-value-types), as specified by the FLG_ADDREG_TYPE_DWORD value **0x00010001**.

    For drivers, this value should be **7**. This value is equivalent to the bitwise OR of EVENTLOG_SUCCESS, EVENTLOG_ERROR_TYPE, EVENTLOG_WARNING_TYPE, and EVENTLOG_INFORMATION_TYPE, without setting the EVENTLOG_AUDIT__XXX_ bits.

An *event-log-install-section* can also use the [**DelReg**](inf-delreg-directive.md) directive to remove a previously installed event-log message file, by explicitly deleting the existing **EventMessageFile** and **TypesSupported** value entries, if a driver binary is being superseded by a newly installed driver. (See also [**INF DelService Directive**](inf-delservice-directive.md).)

While a [**BitReg**](inf-bitreg-directive.md) directive is also valid within an INF-writer-defined *event-log-install*-*section*, it is almost never used, because the standard value entries for device driver event logging are not bitmasks.

## Examples

This example shows the service-install and event-log-install sections referenced by the **AddService** directive as already shown earlier in the example for [***DDInstall*.Services**](inf-ddinstall-services-section.md).

```inf
[Example_DDInstall.Services]
AddService=ExampleFunctionDriver,0x00000002,function_ServiceInstallSection
AddService=ExampleUpperFilter,,filter_ServiceInstallSection

[function_ServiceInstallSection]
DisplayName    = %function_ServiceDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleFunctionDriver.sys

[function_EventLogInstallSection]
AddReg = function_EventLog_AddReg

[function_EventLog_AddReg]
;
; Following entry on single line in INF file. Enclosing quotation marks 
; prevent the semicolon from being interpreted as a comment.
;
HKR,,EventMessageFile,0x00020000,"%%SystemRoot%%\System32\IoLogMsg.dll;
       %13%\ExampleFunctionDriver.sys"
HKR,,TypesSupported,0x00010001,7

[filter_ServiceInstallSection]
DisplayName    = %filter_ServiceDesc%
ServiceType    = 1
StartType      = 3
ErrorControl   = 1
ServiceBinary  = %13%\ExampleUpperFilter.sys

[Strings] ; only immediately preceding %strkey% tokens shown here
%function_ServiceDesc%="Example function driver service"
%filter_ServiceDesc%="Example filter driver service"
```

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
