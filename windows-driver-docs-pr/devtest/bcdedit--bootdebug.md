---
title: BCDEdit /bootdebug
description: The /bootdebug boot option enables or disables boot debugging of the current or specified Windows operating system boot entry.
ms.assetid: 85d0a25e-c411-4d7e-ae11-ce5bed1a37b8
ms.date: 05/21/2018
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

> [!NOTE]
> Before setting BCDEdit options you might need to disable or suspend BitLocker and Secure Boot on the computer.

 

``` syntax
    bcdedit /bootdebug [{ID}] { on | off } 
   
```

Parameters
----------

**{**<em>ID</em>**}**   

The **{**<em>ID</em>**}** is the GUID that is associated with the boot entry. If you do not specify an **{**<em>ID</em>**}**, the command modifies the operating system that is currently active. If a boot entry is specified, the GUID associated with the boot entry must be enclosed in braces **{}**.

**on**   

Enables boot debugging of the specified boot entry. If a boot entry is not specified, boot debugging is enabled for the current operating system.

**off**   

Disables boot debugging of the specified boot entry. If a boot entry is not specified, boot debugging is disabled for the current operating system.

### Comments

The **/bootdebug** boot option enables boot debugging for a specific boot entry. Use the **/dbgsettings** option to configure the type of debugging connection (*debugtype*) to use and the connection parameters. If no **/dbgsettings** are specified for the boot entry, the global debug settings are used. The default values for the global settings are shown in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">dbgsetting parameter</th>
<th align="left">Default value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Debugtype</p></td>
<td align="left"><p>Serial</p></td>
</tr>
<tr class="even">
<td align="left"><p>Debugport</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Baudrate</p></td>
<td align="left"><p>115200</p></td>
</tr>
</tbody>
</table>

 

For information about Windows debugging tools, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063). For information about setting up and configuring a kernel-mode debugging session, see [Setting Up Kernel-Mode Debugging Manually](https://msdn.microsoft.com/library/windows/hardware/hh439378).

The following command disables boot debugging of Windows Boot Manager (Bootmgr.exe). Windows Boot Manager selects which operating system will start, and then loads the Windows boot loader.

```
bcdedit /bootdebug {bootmgr} off 
```

The following command enables boot debugging of the Windows boot loader for the current operating system. The Windows boot loader (Winload.exe) controls the progress bar and loads the kernel boot drivers.

```
bcdedit /bootdebug on 
```

In the following example, the first command sets the global debugger settings for a 1394 kernel debugging connection. The next three commands enable debugging of Windows Boot Manager, the boot loader, and then kernel debugging of the operating system. This combination allows debugging at every stage of startup. If this combination is used, the target computer will break into the debugger three times: when Windows Boot Manager loads, when the boot loader loads, and when the operating system starts up.

```
bcdedit /dbgsettings 1394 CHANNEL:1 
bcdedit /bootdebug {bootmgr} on 
bcdedit /bootdebug on 
bcdedit /debug on 
```

 

 





