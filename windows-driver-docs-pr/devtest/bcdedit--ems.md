---
title: BCDEdit /ems
description: The /ems option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.
ms.assetid: 28a28fa9-e359-4fd7-be4d-9b4129db8ac7
ms.date: 05/21/2018
keywords: ["BCDEdit /ems Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /ems
api_type:
- NA
ms.localizationpriority: medium
---

BCDEdit /ems
============

The **/ems** option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.

``` syntax
    bcdedit /ems [{ID}] { on | off } 

   
```

Parameters
----------

<strong>{ID}</strong>   

The {**ID**} is the GUID that is associated with the boot entry. If you do not specify an {**ID**}, the command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces { }.

### Comments

In Windows Vista and later, use [**BCDEdit /emssettings**](bcdedit--emssettings.md) command and its parameters to establish EMS settings for all boot entries. Then, use the **BCDEdit /ems** command to enable EMS for a particular boot entry.

EMS allows users to control particular components of a server remotely, even when the server is not connected to the network or to other standard remote-administration tools. For information about EMS, search for Emergency Management Services on the [Microsoft TechNet](http://go.microsoft.com/fwlink/p/?linkid=10111) website.

### Example

The following command enables EMS for a boot entry with the identifier of {49916baf-0e08-11db-9af4-000bdbd316a0}.

```
bcdedit /ems {49916baf-0e08-11db-9af4-000bdbd316a0} on
```

 

 





