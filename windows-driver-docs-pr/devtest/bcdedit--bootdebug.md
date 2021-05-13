---
title: BCDEdit /bootdebug
description: The /bootdebug boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.
ms.date: 04/22/2019
keywords: ["BCDEdit /bootdebug Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /bootdebug
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /bootdebug

The **/bootdebug** boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.


``` syntax
bcdedit /bootdebug [{ID}] { on | off }
```

## Parameters

**{**<em>ID</em>**}**

The **{**<em>ID</em>**}** is the ID that is associated with the boot entry, such as {DEFAULT} for the default OS boot entry. If you do not specify an **{**<em>ID</em>**}**, the command modifies the operating system that is currently active. For more information about working with boot entry identifiers, see [Boot Options Identifiers](boot-options-identifiers.md).

**on**

Enables boot debugging of the specified boot entry. If a boot entry is not specified, boot debugging is enabled for the current operating system.

**off**

Disables boot debugging of the specified boot entry. If a boot entry is not specified, boot debugging is disabled for the current operating system.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

### Comments

The **/bootdebug** boot option enables boot debugging for a specific boot entry. Use the **/dbgsettings** option to configure the type of debugging connection (*debugtype*) to use and the connection parameters. 

The default values for the dbgsettings are shown in the following table.

|dbgsetting parameter|Default value|
|--- |--- |
|debugtype|Local|
|debugstart|Active|
|noumex|Yes|


The following command enables boot debugging of the Windows boot loader for the current operating system. The Windows boot loader (Winload.exe) controls the load UI and loads the kernel boot drivers.

```console
bcdedit /bootdebug on
```

The following command disables boot debugging of Windows Boot Manager (Bootmgr.exe). Windows Boot Manager selects which operating system will start, and then loads the Windows boot loader.

```console
bcdedit /bootdebug {bootmgr} off
```

In the following example, the commands enable debugging of Windows Boot Manager, the boot loader, and then kernel debugging of the operating system. This combination allows debugging at every stage of startup. If this combination is used, the target computer will break into the debugger three times: when Windows Boot Manager loads, when the boot loader loads, and when the operating system starts up.

```console
bcdedit /bootdebug {bootmgr} on
bcdedit /bootdebug on
bcdedit /debug on
```

For general information about Windows debugging tools, see [Windows Debugging](../debugger/index.md).
