---
title: ".echocpunum (Show CPU Number)"
description: "The .echocpunum command turns on or turns off the display of the processor number when you are debugging a multiprocessor target computer."
keywords: ["Show CPU Number (.echocpunum) command", "multiprocessor computer, Show CPU Number (.echocpunum) command", ".echocpunum (Show CPU Number) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .echocpunum (Show CPU Number)
api_type:
- NA
---

# .echocpunum (Show CPU Number)


The **.echocpunum** command turns on or turns off the display of the processor number when you are debugging a multiprocessor target computer.

```dbgcmd
.echocpunum 0 
.echocpunum 1 
.echocpunum 
```

## <span id="ddk_meta_show_cpu_number_dbg"></span><span id="DDK_META_SHOW_CPU_NUMBER_DBG"></span>Parameters


<span id="_______0______"></span> **0**   
Turns off the display of the processor number.

<span id="_______1______"></span> **1**   
Turns on the display of the processor number.

## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>Kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For more information about how to debug multiprocessor computers, see [Multiprocessor Syntax](multiprocessor-syntax.md).

## Remarks

If you use the **.echocpunum** command without any arguments, the display of processor numbers is turned on or off, and the new state is displayed.

By default, the display is turned off.

