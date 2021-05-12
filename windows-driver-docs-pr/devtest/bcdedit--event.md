---
title: BCDEdit /event
description: The /event command enables or disables the remote event logging for the specified boot entry.
ms.date: 09/23/2020
keywords: ["BCDEdit /event Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /event
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /event


The **/event** enables or disables the remote event logging for the specified boot entry.

``` syntax
bcdedit /event [{ID}] { on | off }
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

<strong>{ID}</strong>

The {**ID**} Specifies the identifier of the entry to be modified.  Only  Windows boot loader entries may be specified.  If not
specified, {current} is used. For more information about identifiers, run "bcdedit /? ID".

## Example

The following command enables remote event logging for the current Windows operating system boot entry.

``` syntax
bcdedit /event ON
```

The following command disables remote event logging for the specified operating
system entry:

```syntax
bcdedit /event {cbd971bf-b7b8-4885-951a-fa03044f5d71} OFF
```
