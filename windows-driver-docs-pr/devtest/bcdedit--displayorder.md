---
title: BCDEdit /displayorder
description: The displayorder command sets the display order to be used by the boot manager.
ms.date: 09/23/2020
keywords: ["BCDEdit /displayorder Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /displayorder
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /displayorder


The **/displayorder** command sets the display order to be used by the boot manager.

``` syntax
bcdedit /displayorder <id> [...] [ /addfirst | /addlast | /remove ]
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**\<id\> [...]**  Specifies a list of identifiers that make up the display order.  At least one identifier must be specified
and they must be separated by spaces.  For more information about identifiers, run "bcdedit /? ID".

**/addfirst**   Adds the specified entry identifier to the top of the display order.  If this switch is specified, only a
single entry identifier may be specified.  If the specified identifier is already in the list, it will be moved to the
top of the list.

**/addlast**  Adds the specified entry identifier to the end of the display order.  If this switch is specified, only a
single entry identifier may be specified.  If the specified identifier is already in the list, it is moved to the
end of the list.

**/remove**

Removes the specified entry identifier from the display order.  If this switch is specified, only a single
entry identifier may be specified.  If the identifier is not in the list then the operation has no effect. If
the last entry is being removed, then the display order value is deleted from the boot manager entry.

## Examples

The following command sets two OS entries and the NTLDR based OS loader in the boot manager display order:

`bcdedit /displayorder {802d5e32-0784-11da-bd33-000476eba25f} {cbd971bf-b7b8-4885-951a-fa03044f5d71} {ntldr}`

The following command adds the specified OS entry to the end of the boot manager display order:

`bcdedit /displayorder {802d5e32-0784-11da-bd33-000476eba25f} /addlast`
