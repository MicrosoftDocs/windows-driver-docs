---
title: BCDEdit /bootsequence
description: The bootsequence command sets the one-time boot sequence to be used by the boot manager.
ms.date: 09/23/2020
keywords: ["BCDEdit /bootsequence Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /bootsequence
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /bootsequence


The **/bootsequence** command sets the one-time boot sequence to be used by the boot manager.

``` syntax
bcdedit /bootsequence <id> [...] [ /addfirst | /addlast | /remove ]
```

## Parameters

**<id> [...]**

Specifies a list of data store identifiers that make up the boot sequence. You must specify at least one identifier and must
separate identifiers by spaces. For more information about identifiers, run "bcdedit /? ID".

**/addfirst**

Adds the specified entry identifier to the top of the boot sequence.  If this switch is specified, only a single
identifier may be specified.  If the identifier is already in the list, it is moved to the top of the list.

**/addlast**

Adds the specified entry identifier to the end of the boot sequence.  If this switch is specified, only a single
identifier may be specified.  If the identifier is already in the list, it is moved to the end of the list.

**/remove**

Removes the specified entry identifier from the boot sequence.  If this switch is specified, only a single
entry identifier may be specified.  If the identifier is not in the list then the operation has no effect. If
the last entry is being removed, then the boot sequence value is deleted from the boot manager entry.

## Examples

The following command sets two OS entries and the NTLDR based OS loader in the boot manager one-time boot sequence:

`bcdedit /bootsequence {802d5e32-0784-11da-bd33-000476eba25f} {cbd971bf-b7b8-4885-951a-fa03044f5d71} {ntldr}`

The following command adds the specified OS entry to the end of the boot manager one-time boot sequence:

`bcdedit /bootsequence {802d5e32-0784-11da-bd33-000476eba25f} /addlast`
