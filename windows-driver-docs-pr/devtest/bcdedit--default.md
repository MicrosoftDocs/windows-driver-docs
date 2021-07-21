---
title: BCDEdit /default
description: The **BCDEdit /default** command sets the default entry that the boot manager will use when the timeout expires.
ms.date: 09/23/2020
keywords: ["BCDEdit /default Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /default
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /default


The **BCDEdit /default** command sets the default entry that the boot manager will use when the timeout expires.

``` syntax
bcdedit /default <id>
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**\<id\>**

Specifies the identifier of the boot entry to be used as the default when the time-out expires. For information about identifiers, run "bcdedit /? ID".

## Examples

The following command sets the specified entry as the default boot manager entry.

`bcdedit /default {cbd971bf-b7b8-4885-951a-fa03044f5d71}`

The following command sets the NTLDR based OS loader as the default
entry:

`bcdedit /default {ntldr}`
