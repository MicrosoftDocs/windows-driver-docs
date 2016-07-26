---
title: INF DelService Directive
description: A DelService directive is used in a DDInstall.Services section to remove one or more previously installed device/driver services from the target computer.
ms.assetid: eca57f7c-1551-4247-ab1f-858e6e3ad9d7
keywords: ["INF DelService Directive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- INF DelService Directive
api_type:
- NA
---

# INF DelService Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-configurable-inf-file.md).

 

A **DelService** directive is used in a [***DDInstall*.Services**](inf-ddinstall-services-section.md) section to remove one or more previously installed device/driver services from the target computer.

``` syntax
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

<a href="" id="0x00000004--spsvcinst-deleteeventlogentry-"></a>**0x00000004** (SPSVCINST\_DELETEEVENTLOGENTRY)  
An event-log entry (or entries) associated with the given ServiceName should also be removed from the system.

<a href="" id="0x00000200---spsvcinst-stopservice--"></a>**0x00000200** (SPSVCINST\_STOPSERVICE)   
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20INF%20DelService%20Directive%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





