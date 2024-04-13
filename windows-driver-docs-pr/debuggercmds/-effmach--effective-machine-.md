---
title: ".effmach (Effective Machine)"
description: "The .effmach command displays or changes the processor mode that the debugger uses."
keywords: ["Effective Machine (.effmach) command", ".effmach (Effective Machine) Windows Debugging"]
ms.date: 01/24/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .effmach (Effective Machine)
api_type:
- NA
---

# .effmach (Effective Machine)


The **.effmach** command displays or changes the processor mode that the debugger uses.

```dbgcmd
.effmach [MachineType]
```

## Parameters


<span id="_______MachineType______"></span><span id="_______machinetype______"></span><span id="_______MACHINETYPE______"></span> *MachineType*   
Specifies the processor type that the debugger uses for this session. If you omit this parameter, the debugger displays the current machine type.

You can enter one of the following machine types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Machine type</strong></p></td>
<td align="left"><p><strong>Description</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>.</strong></p></td>
<td align="left"><p>Use the processor mode of the target computer's native processor mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>#</strong></p></td>
<td align="left"><p>Use the processor mode of the code that is executing for the most recent event.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>x86</strong></p></td>
<td align="left"><p>Use an x86-based processor mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>amd64</strong></p></td>
<td align="left"><p>Use an x64-based processor mode.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ebc</strong></p></td>
<td align="left"><p>Use an EFI byte code processor mode.</p></td>
</tr>
</tr>
<tr class="odd">
<td align="left"><p><strong>arm</strong></p></td>
<td align="left"><p>Use an Arm64 processor mode.</p></td>
</tr>
</tr>
<tr class="evenodd">
<td align="left"><p><strong>chpe</strong></p></td>
<td align="left"><p>Use a CHPE processor mode.</p></td>
</tr>
</tbody>
</table>

 

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The processor mode influences many debugger features:

-   Which processor is used for stack tracing.

-   Whether the process uses 32-bit or 64-bit pointers.

-   Which processor's register set is active.

