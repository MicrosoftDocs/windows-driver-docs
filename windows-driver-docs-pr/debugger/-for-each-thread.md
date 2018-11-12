---
title: for_each_thread
description: The for_each_thread extension executes the specified debugger command once for each thread in the target.
ms.assetid: 4ca8e1bd-1a1b-4fef-a2d9-42c26f9b746b
keywords: ["for_each_thread Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- for_each_thread
api_type:
- NA
ms.localizationpriority: medium
---

# !for\_each\_thread


The **!for\_each\_thread** extension executes the specified debugger command once for each thread in the target.

```dbgcmd
!for_each_thread ["CommandString"] 
!for_each_thread -? 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to be executed for each thread. If *CommandString* includes multiple commands, separate them with semicolons (;) and enclose *CommandString* in quotation marks ("). If *CommandString* is enclosed in quotations marks, the individual commands within *CommandString* cannot contain quotation marks. Within *CommandString*, **@\#Thread** is replaced by the thread address.

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

For more general information about threads, see [Threads and Processes](controlling-threads-and-processes.md). For more information about manipulating or obtaining information about threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

If no arguments are supplied, the debugger displays a list of all threads, along with thread wait states. This is equivalent to entering [**!thread @\#Thread 2**](-process.md) as the *CommandString* value.

You can terminate execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





