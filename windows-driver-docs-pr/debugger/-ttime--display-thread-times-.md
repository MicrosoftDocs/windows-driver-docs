---
title: .ttime (Display Thread Times)
description: The .ttime command displays the running times for a thread.
ms.assetid: ff48310f-3eb9-4112-b5ab-b7c16878ac8f
keywords: [".ttime (Display Thread Times) Windows Debugging"]
ms.author: domars
ms.date: 08/01/2018
topic_type:
- apiref
api_name:
- .ttime (Display Thread Times)
api_type:
- NA
ms.localizationpriority: medium
---

# .ttime (Display Thread Times)


The **.ttime** command displays the running times for a thread.

```dbgcmd
.ttime 
```

## <span id="ddk_meta_display_thread_times_dbg"></span><span id="DDK_META_DISPLAY_THREAD_TIMES_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86 only</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This command only works in user mode. In kernel mode you should use [**!thread**](-thread.md) instead. This command works with user-mode minidumps as long as they were created with the **/mt** or **/ma** options; see [User-Mode Dump Files](user-mode-dump-files.md) for details.

The **.ttime** command shows the creation time of the thread, as well as the amount of time it has been running in kernel mode and in user mode.

Here is an example:

```dbgcmd
0:000> .ttime
Created: Sat Jun 28 17:58:42 2003
Kernel:  0 days 0:00:00.131
User:    0 days 0:00:02.109
```

 

 





