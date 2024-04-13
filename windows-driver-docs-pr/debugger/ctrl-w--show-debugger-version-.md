---
title: CTRL+W (Show Debugger Version)
description: The CTRL+W key displays version information for the debugger and all loaded extension DLLs.
keywords: ["CTRL+W (Show Debugger Version) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- CTRL+W (Show Debugger Version)
api_type:
- NA
---

# CTRL+W (Show Debugger Version)


The CTRL+W key displays version information for the debugger and all loaded extension DLLs.

CDB / KD Syntax

```dbgcmd
CTRL+W  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+W 
```


## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>CDB, KD, WinDbg</p></td>
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

This has the same effect as the [**version (Show Debugger Version)**](../debuggercmds/version--show-debugger-version-.md) command, except that the latter command displays the Windows operating system version as well.

In WinDbg, this can also be accomplished by selecting **View | Show Version**.

## <span id="see_also"></span>See also


[**version (Show Debugger Version)**](../debuggercmds/version--show-debugger-version-.md)

[**vertarget (Show Target Computer Version)**](../debuggercmds/vertarget--show-target-computer-version-.md)

 

 
