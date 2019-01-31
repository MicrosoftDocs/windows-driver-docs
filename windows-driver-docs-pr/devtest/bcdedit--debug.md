---
title: BCDEdit /debug
description: The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.
ms.assetid: 013ec247-f2ca-4918-9dfa-8b1348d0b4e5
ms.date: 01/31/2019
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

Parameters
----------

**{**<em>ID</em>**}**   
The **{**<em>ID</em>**}** is the GUID that is associated with the boot entry. If you do not specify an **{**<em>ID</em>**}**, the command modifies the operating system that is currently active. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces **{ }**.

 **on**   
Enables kernel debugging of the specified boot entry. If a boot entry is not specified, kernel debugging is enabled for the current operating system.

**off**   
Disables kernel debugger of the specified boot entry. If a boot entry is not specified, kernel debugging is disabled for the current operating system.

### Comments

The **/debug** boot option enables kernel debugging for a specific boot entry. Use the **/dbgsettings** option to configure the type of debugging connection to use and the connection parameters. If no **/dbgsettings** are specified for the boot entry, the global debug settings are used. The default values for the global settings are shown in the following table.

|dbgsetting parameter|Default value|
|--- |--- |
|Connection type|Serial|
|Debug port|1|
|Baud rate|115200|


> [!IMPORTANT]
> Setting up a network debugging manually is a complex and error prone process.
> To set up network debugging automatically, see [Setting Up KDNET Network Kernel Debugging Automatically](https://docs.microsoft.com/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection-automatically). Using the KDNET utility is **strongly** recommended for all debugger users.


The following example enables kernel debugging of the boot entry with the GUID of 49916baf-0e08-11db-9af4-000bdbd316a0.

```
bcdedit /debug {49916baf-0e08-11db-9af4-000bdbd316a0} on 
```

For information about Windows debugging tools, see [Windows Debugging](https://docs.microsoft.com/windows-hardware/drivers/debugger/index) and [Setting Up KDNET Network Kernel Debugging Automatically](https://docs.microsoft.com/windows-hardware/drivers/debugger/setting-up-a-network-debugging-connection-automatically) 

 





