---
title: BCDEdit /enum
description: The BCDEdit /enum command lists entries in Boot Configuration Data (BCD) store. 
ms.date: 09/24/2020
keywords: ["BCDEdit /enum Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /enum
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /enum


The **BCDEdit /enum** command lists entries in Boot Configuration Data (BCD) store. The /enum command is the default,
so running "bcdedit" without parameters is equivalent to running "bcdedit /enum ACTIVE".

```syntax
bcdedit [/store <filename>] /enum [<type> | <id>] [/v]
```

> [!CAUTION]
>Administrative privileges are required to use BCDEdit to view the BCD store. Changing some boot entry options using the BCDEdit /set command could render your computer inoperable. As an alternative, use the System Configuration utility (MSConfig.exe) to change boot settings.

## Parameters

**\<filename\>**

Specifies the store to be used. If this option is not specified, the system store is used. For more information, run "bcdedit /? store".

**\<type\>**

Specifies the type of entries to be listed. <type> can be one of the following:

*ACTIVE* - All entries in the boot manager display order. This is the default.

*FIRMWARE* - All firmware applications.

*BOOTAPP* - All boot environment applications.

*BOOTMGR* - The boot manager.

*OSLOADER* - All operating system entries.

*RESUME* - All resume from hibernation entries.

*INHERIT* - All inherit entries.

*ALL* - All entries.

**\<id\>**

Specifies the identifier of the entry to be listed.  If an identifier is provided, then only the specified object will be
listed. For information about identifiers, run "bcdedit /? ID".

**/v**

Displays entry identifiers in full, rather than using names for well-known identifiers.

## Examples

The following command lists all operating system loader boot entries.

`bcdedit /enum OSLOADER`

The following command lists all boot manager entries.

`bcdedit /enum BOOTMGR`

The following command lists only the default boot entry.

`bcdedit /enum {default}`

The following command enables enum for a boot entry with the identifier of {49916baf-0e08-11db-9af4-000bdbd316a0}.

`bcdedit /enum {49916baf-0e08-11db-9af4-000bdbd316a0} on`
