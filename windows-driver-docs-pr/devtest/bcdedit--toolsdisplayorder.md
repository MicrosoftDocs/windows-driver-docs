---
title: BCDEdit /toolsdisplayorder
description: The BCDEdit /toolsdisplayorder command sets the display order to be used by the boot manager when displaying the tools menu.
ms.date: 09/23/2020
keywords: ["BCDEdit /toolsdisplayorder Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /toolsdisplayorder
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /toolsdisplayorder


The **BCDEdit /toolsdisplayorder** command sets the display order to be used by the boot manager when displaying the tools menu.

```syntax
bcdedit /toolsdisplayorder <id> [...] [ /addfirst | /addlast | /remove ]
```

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

## Parameters

**<id> [...]**

Specifies a list of identifiers that make up the tools display order.  At least one identifier must be specified and they must be separated by spaces.  For more information about identifiers, run "bcdedit /? ID".

**/addfirst**

Adds the specified entry identifier to the top of the tools display order.  If this switch is specified, only a single entry identifier may be specified.  If the specified identifier is already in the list, it is moved to the top of the list.

**/addlast**

Adds the specified entry identifier to the end of the tools display order.  If this switch is specified, only a single entry identifier may be specified.  If the specified identifier is already in the list, it is moved to the end of the list.

**/remove**

Removes the specified entry identifier from the tools display order.  If this switch is specified, only a single entry identifier may be specified.  If the identifier is not in the list, then the operation will have no effect.  If the last entry is being removed, then the tools display order value is deleted from the boot manager
entry.

## Examples

The following command sets two tools entries and the memory diagnostic in the boot manager's tools display order:

`bcdedit /toolsdisplayorder {802d5e32-0784-11da-bd33-000476eba25f} {cbd971bf-b7b8-4885-951a-fa03044f5d71} {memdiag}`

The following command adds the specified tool entry to the end of the boot manager's tools display order:

`bcdedit /toolsdisplayorder {802d5e32-0784-11da-bd33-000476eba25f} /addlast`
