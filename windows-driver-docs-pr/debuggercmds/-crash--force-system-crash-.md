---
title: ".crash (Force System Crash)"
description: "The .crash command causes the target computer to issue a bug check."
keywords: [".crash (Force System Crash) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .crash (Force System Crash)
api_type:
- NA
---

# .crash (Force System Crash)


The **.crash** command causes the target computer to issue a bug check.

```dbgsyntax
.crash
```

## <span id="ddk_meta_force_system_crash_dbg"></span><span id="DDK_META_FORCE_SYSTEM_CRASH_DBG"></span>


## Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

## Additional Information

For an overview of related commands and a description of the options available after a system crash, see [Crashing and Rebooting the Target Computer](../debugger/crashing-and-rebooting-the-target-computer.md).

## Remarks

This command will immediately cause the target computer to crash.

If you are already in a bug check handler, do not use **.crash**. Use [**g (Go)**](g--go-.md) instead to continue execution of the handler, which will generate a crash dump.

A kernel-mode dump file will be written if crash dumps have been enabled. See [Creating a Kernel-Mode Dump File](../debugger/creating-a-kernel-mode-dump-file.md) for details.

