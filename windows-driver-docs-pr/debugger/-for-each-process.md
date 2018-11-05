---
title: for_each_process
description: The for_each_process extension executes the specified debugger command once for each process in the target.
ms.assetid: 28cc0982-43a4-41ba-a26f-6910cc1b77b8
keywords: ["for_each_process Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- for_each_process
api_type:
- NA
ms.localizationpriority: medium
---

# !for\_each\_process


The **!for\_each\_process** extension executes the specified debugger command once for each process in the target.

```dbgcmd
!for_each_process ["CommandString"] 
!for_each_process -? 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to be executed for each process.

If *CommandString* includes multiple commands, separate them with semicolons (;) and enclose *CommandString* in quotation marks ("). If *CommandString* is enclosed in quotations marks, the individual commands within *CommandString* cannot contain quotation marks. Within *CommandString*, **@\#Process** is replaced by the process address.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension works only in kernel mode, even though it resides in Ext.dll.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For general information about processes, see [Threads and Processes](controlling-threads-and-processes.md). For information about manipulating or obtaining information about processes, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

If no arguments are supplied, the debugger displays a list of all processes, along with time and priority statistics. This is equivalent to entering [**!process @\#Process 0**](-process.md) as the *CommandString* value.

To terminate execution at any point, press CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





