---
title: Changing the Friendly Name of a Boot Entry
description: Changing the Friendly Name of a Boot Entry
keywords:
- names WDK boot options
- friendly names WDK boot options
- renaming boot entries WDK
- Boot.ini files WDK , friendly names
- boot options WDK , friendly names
ms.date: 11/05/2024
---

# Changing the Friendly Name of a Boot Entry


In Windows, the items that appear in the Windows Boot Manager are the descriptions of each boot entry.

Typically, after you copy a boot entry, you change the friendly name of the newly created entry to distinguish it from the original.

You can also change the friendly name to make it easier to recognize customized boot entries. A string that precisely describes the entry can save significant time and effort.

For example, the following friendly name strings add little value.

```
"Windows 10 Debug1"
"Windows 10 Debug2"
```

However, more precise strings, such as the ones that follow, make the boot choice much easier.

```
"Windows 10 kdnet"
"Windows 10 NullModem"
```

To change the friendly name of a boot entry for Windows, use BCDEdit. 

> [!CAUTION]
> Administrative privileges are required to update the boot configuration. Changing some boot entry options could render your computer inoperable. 


## Using BCDEdit

To change the description of a boot entry as it appears on the boot menu, you can use the **/set** *IDdescription* option. The command uses the following syntax. The ID is the GUID that is associated with the boot entry (or one of the well-known identifiers, for example, {current}).

> [!NOTE]
> If you are using [Windows PowerShell](/powershell/scripting/overview), you must use quotes around the boot entry identifier, for example: **"{49916baf-0e08-11db-9af4-000bdbd316a0}"** or **"{current}"**.


```console
bcdedit /set ID description "The new description"
```

For example:

```console
bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} description "Windows 10 NullModem"
```

To change the description of the boot entry that corresponds to the operating system that is currently running, use the following example:

```console
bcdedit /set {current} description "Windows 10 NullModem"
```

You can also change the description when you copy an existing boot entry using the **/d** option.

```console
bcdedit /copy {current} /d "Windows 10 NullModem"
```

## See also

[Adding Boot Entries](./adding-boot-entries.md)

[**BCDEdit /set**](bcdedit--set.md)


