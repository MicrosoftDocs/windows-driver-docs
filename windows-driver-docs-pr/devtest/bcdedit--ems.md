---
title: BCDEdit /ems
description: The /ems option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.
ms.assetid: 28a28fa9-e359-4fd7-be4d-9b4129db8ac7
keywords: ["BCDEdit /ems Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /ems
api_type:
- NA
---

BCDEdit /ems
============

The **/ems** option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.

``` syntax
    bcdedit /ems [{ID}] { on | off } 

   
```

Parameters
----------

<a href="" id="--------id-------"></a> **{***ID***}**   
The **{***ID***}** is the GUID that is associated with the boot entry. If you do not specify an **{***ID***}**, the command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces { }.

### Comments

InWindows Vista and later, use [**BCDEdit /emssettings**](bcdedit--emssettings.md) command and its parameters to establish EMS settings for all boot entries. Then, use the **BCDEdit /ems** command to enable EMS for a particular boot entry.

EMS allows users to control particular components of a server remotely, even when the server is not connected to the network or to other standard remote-administration tools. For information about EMS, search for Emergency Management Services on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

### Example

The following command enables EMS for a boot entry with the identifier of {49916baf-0e08-11db-9af4-000bdbd316a0}.

```
bcdedit /ems {49916baf-0e08-11db-9af4-000bdbd316a0} on
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20BCDEdit%20/ems%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




