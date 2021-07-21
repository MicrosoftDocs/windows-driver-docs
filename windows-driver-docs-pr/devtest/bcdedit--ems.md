---
title: BCDEdit /ems
description: The BCDEdit /ems option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.
ms.date: 09/23/2020
keywords: ["BCDEdit /ems Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /ems
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /ems


The **BCDEdit /ems** option enables or disables Emergency Management Services (EMS) for the specified operating system boot entry.

``` syntax
bcdedit /ems [{ID}] { on | off }
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**{ID}**

The {**ID**} is the GUID that is associated with the boot entry. If you do not specify an {**ID**}, the command modifies the current operating system boot entry. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces { }.

## Comments

Use [**BCDEdit /emssettings**](bcdedit--emssettings.md) command and its parameters to establish EMS settings for all boot entries. Then, use the **BCDEdit /ems** command to enable EMS for a particular boot entry.

EMS allows users to control particular components of a server remotely, even when the server is not connected to the network or to other standard remote-administration tools.

## Example

The following command enables EMS for a boot entry with the identifier of {49916baf-0e08-11db-9af4-000bdbd316a0}.

```console
bcdedit /ems {49916baf-0e08-11db-9af4-000bdbd316a0} on
```
