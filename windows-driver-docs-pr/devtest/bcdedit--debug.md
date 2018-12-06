---
title: BCDEdit /debug
description: The /debug boot option enables or disables kernel debugging of the Windows operating system associated with the specified boot entry or the current boot entry.
ms.assetid: 013ec247-f2ca-4918-9dfa-8b1348d0b4e5
ms.date: 07/02/2018
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
<td align="left"><p>Connection type</p></td>
<td align="left"><p>Serial</p></td>
</tr>
<tr class="even">
<td align="left"><p>Debug port</p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Baud rate</p></td>
<td align="left"><p>115200</p></td>
</tr>
</tbody>
</table>

 

For information about Windows debugging tools, see [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063). For information about setting up and configuring a kernel-mode debugging session, see [Setting Up Kernel-Mode Debugging Manually](https://msdn.microsoft.com/library/windows/hardware/hh439378).

The following example enables kernel debugging of the boot entry with the GUID of 49916baf-0e08-11db-9af4-000bdbd316a0.

```
bcdedit /debug {49916baf-0e08-11db-9af4-000bdbd316a0} on 
```

In the following example, the first command sets the global debugger settings for USB 2.0 and names the target myVistaTarget. The second command enables the debugger for the current session.

```
bcdedit /dbgsettings usb targetname:myVistaTarget 
bcdedit /debug ON 
```

 

 





