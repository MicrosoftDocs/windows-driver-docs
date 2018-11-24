---
title: INF DelService Directive
description: A DelService directive is used in a DDInstall.Services section to remove one or more previously installed device/driver services from the target computer.
ms.assetid: eca57f7c-1551-4247-ab1f-858e6e3ad9d7
keywords:
- INF DelService Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DelService Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF DelService Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **DelService** directive is used in a [***DDInstall*.Services**](inf-ddinstall-services-section.md) section to remove one or more previously installed device/driver services from the target computer.

```cpp
[DDInstall.Services] 
 
DelService=ServiceName[,[flags][,[EventLogType][,EventName]]
...
```

## Entries


<a href="" id="servicename"></a>*ServiceName*  
Specifies the name of the service to be removed.

For a device, this value is usually a generic name for its driver, such as "sermouse," or some such name.

<a href="" id="flags"></a>*flags*  
This optional value is specifies one or more of the following flags, defined in *Setupapi.h*, that are specified as a hexadecimal value:

<a href="" id="0x00000004--spsvcinst-deleteeventlogentry-"></a>**0x00000004** (SPSVCINST_DELETEEVENTLOGENTRY)  
An event-log entry (or entries) associated with the given ServiceName should also be removed from the system.

<a href="" id="0x00000200---spsvcinst-stopservice--"></a>**0x00000200** (SPSVCINST_STOPSERVICE)   
Stop the service before deleting it.

<a href="" id="eventlogtype"></a>*EventLogType*  
Optionally specifies one of **System**, **Security**, or **Application**. This can be omitted if the event log to be removed is of type **System**.

<a href="" id="eventname"></a>*EventName*  
Optionally specifies the name for the event log. This can be omitted if it is identical to the specified *ServiceName* entry.

Remarks
-------

This directive is rarely used. The only services that can be safely deleted are those that were used only in earlier versions of the operating system, and are therefore never used for the currently installed version.

Starting with Windows XP, you can use the *TargetOSVersion* decoration to control version-specific installation behavior. For more information about this decoration, see [**INF Manufacturer Section**](inf-manufacturer-section.md).

However, by default, event-log information supplied by a particular device driver is not removed from the system on deinstallation, unless the INF for the device/driver explicitly requests the removal (*flags* or *EventName*) of the event log along with the removal of the driver services.

## See also


[**AddService**](inf-addservice-directive.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**DelReg**](inf-delreg-directive.md)

 

 






