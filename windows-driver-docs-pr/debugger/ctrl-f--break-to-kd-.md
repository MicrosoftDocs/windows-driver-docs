---
title: CTRL+F (Break to KD)
description: The CTRL+F key cancels commands or breaks into the debugger.
keywords: ["CTRL+F (Break to KD) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CTRL+F (Break to KD)
api_type:
- NA
---

# CTRL+F (Break to KD)


The CTRL+F key cancels commands or breaks into the debugger. (This control key is particularly useful when you are using CDB to debug KD itself.)

```dbgcmd
CTRL+F  ENTER 
```


## <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB, KD</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Under typical conditions, CTRL+F is identical to the standard break commands ([**CTRL+C**](ctrl-c--break-.md) in KD and CDB, and **Debug | Break** or CTRL+BREAK in WinDbg.)

However, if you are debugging KD with CDB, these two keys will work differently. CTRL+C will be intercepted by the host debugger (CDB), while CTRL+F will be intercepted by the target debugger (KD).

## <span id="see_also"></span>See also


[**.breakin (Break to the Kernel Debugger)**](../debuggercmds/-breakin--break-to-the-kernel-debugger-.md)

 

 
