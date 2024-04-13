---
title: "rdmsr (Read MSR)"
description: "The rdmsr command reads a Model-Specific Register (MSR) value from the specified address."
keywords: ["rdmsr (Read MSR) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- rdmsr (Read MSR)
api_type:
- NA
---

# rdmsr (Read MSR)


The **rdmsr** command reads a [Model-Specific Register (MSR)](../debugger/other-data-spaces.md) value from the specified address.

```dbgcmd
rdmsr Address 
```

## <span id="ddk_cmd_read_msr_dbg"></span><span id="DDK_CMD_READ_MSR_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the MSR.

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

 

## Remarks

The **rdmsr** command can display MSR's on x86-based and x64-based platforms. The MSR definitions are platform-specific.

## See also


[**wrmsr (Write MSR)**](wrmsr--write-msr-.md)


