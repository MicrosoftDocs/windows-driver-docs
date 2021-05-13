---
title: BCDEdit /debug
description: The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.
ms.date: 04/22/2019
keywords: ["BCDEdit /debug Driver Development Tools"]
topic_type:
- apiref
api_name:
- BCDEdit /debug
api_type:
- NA
ms.localizationpriority: medium
---

# BCDEdit /debug


The **/debug** boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.


``` syntax
bcdedit /debug [{ID}] { on | off }
```

## Parameters

**{**<em>ID</em>**}**   

The **{**<em>ID</em>**}** is the ID that is associated with the boot entry, such as {DEFAULT} for the default OS boot entry. If you do not specify an **{**<em>ID</em>**}**, the command modifies the operating system that is currently active. For more information about working with boot entry identifiers, see [Boot Options Identifiers](boot-options-identifiers.md).

 **on**   
Enables kernel debugging of the specified boot entry. If a boot entry is not specified, kernel debugging is enabled for the current operating system.

**off**   
Disables kernel debugger of the specified boot entry. If a boot entry is not specified, kernel debugging is disabled for the current operating system.

### Comments

The **/debug** boot option enables kernel debugging for a specific boot entry. Use the **/dbgsettings** option to configure the type of debugging connection to use and the connection parameters. If no **/dbgsettings** are specified for the boot entry, the global debug settings are used. The default values for the global settings are shown in the following table.

|dbgsetting parameter|Default value|
|--- |--- |
|debugtype|Local|
|debugstart|Active|
|noumex|Yes|


The following example enables kernel debugging of the default boot entry.

```console
bcdedit /debug on 
```

For information about Windows debugging tools, see [Windows Debugging](../debugger/index.md) and [Setting Up KDNET Network Kernel Debugging Automatically](../debugger/setting-up-a-network-debugging-connection-automatically.md)
