---
title: irql extension command
description: The irql extension displays the interrupt request level (IRQL) of a processor on the target computer before the debugger break.
ms.assetid: 52dd3b9f-c03c-4b90-a01b-25289de67f5a
keywords: ["IRQL", "Interrupt Request Level", "irql Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- irql
api_type:
- NA
ms.localizationpriority: medium
---

# !irql


The **!irql** extension displays the interrupt request level (IRQL) of a processor on the target computer before the debugger break.

```dbgcmd
!irql [Processor] 
```

## <span id="ddk__irql_dbg"></span><span id="DDK__IRQL_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor. Enter the processor number. If this parameter is omitted, the debugger displays the IRQL of the current processor.

### <span id="DLL"></span><span id="dll"></span>DLL

The **!irql** extension is only available in Windows Server 2003 and later versions of Windows.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Windows Server 2003 and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about IRQLs, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

When the target computer breaks into the debugger, the IRQL changes, but the IRQL that was effective just before the debugger break is saved. The **!irql** extension displays the saved IRQL.

Similarly, when a bug check occurs and a crash dump file is created, the IRQL saved in the crash dump file is the one immediately prior to the bug check, not the IRQL at which the [**KeBugCheckEx**](https://msdn.microsoft.com/library/windows/hardware/ff551961) routine was executed.

In both cases, the current IRQL is raised to DISPATCH\_LEVEL, except on x86 architectures. Thus, if more than one such event occurs, the IRQL displayed will also be DISPATCH\_LEVEL, making it useless for debugging purposes.

The [**!pcr**](-pcr.md) extension displays the current IRQL on all versions of Windows, but the current IRQL is usually not useful. The IRQL that existed just before the bug check or debugger connection is more interesting, and this is displayed only with **!irql**.

If you supply an invalid processor number, or there has been kernel corruption, the debugger displays a message "Cannot get PRCB address".

Here is an example of the output from this extension from a dual-processor x86 computer:

```dbgcmd
kd> !irql 0
Debugger saved IRQL for processor 0x0 -- 28 (CLOCK2_LEVEL)

kd> !irql 1
Debugger saved IRQL for processor 0x1 -- 0 (LOW_LEVEL)
```

If the debugger is in verbose mode, a description of the IRQL itself is included. Here is an example from an Itanium processor:

```dbgcmd
kd> !irql
Debugger saved IRQL for processor 0x0 -- 12 (PC_LEVEL) [Performance counter level]
```

The meaning of the IRQL number often depends on the processor. Here is an example from an x64 processor. Note that the IRQL number is the same as in the previous example, but the IRQL meaning is different:

```dbgcmd
kd> !irql
Debugger saved IRQL for processor 0x0 -- 12 (SYNCH_LEVEL) [Synchronization level]
```

 

 





