---
title: ~u (Unfreeze Thread)
description: The ~u command unfreezes the specified thread.Do not confuse this command with the U (Unassemble) command.
ms.assetid: 6ac3c84a-3734-4b16-a239-4233e186c2df
keywords: ["~u (Unfreeze Thread) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ~u (Unfreeze Thread)
api_type:
- NA
ms.localizationpriority: medium
---

# ~u (Unfreeze Thread)


The **~u** command unfreezes the specified thread.

Do not confuse this command with the [**U (Unassemble)**](u--unassemble-.md) command.

```dbgcmd
~Thread u 
```

## <span id="ddk_cmd_unfreeze_thread_dbg"></span><span id="DDK_CMD_UNFREEZE_THREAD_DBG"></span>Parameters


<span id="_______Thread______"></span><span id="_______thread______"></span><span id="_______THREAD______"></span> *Thread*   
Specifies the thread or threads to unfreeze. For more information about the syntax, see [Thread Syntax](thread-syntax.md).

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how frozen threads behave and a list of other commands that control the freezing and suspending of threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

You can specify threads only in user mode. In kernel mode, the tilde (~) refers to a processor.

The following examples show you how to use the ~ commands.

The following command displays the current status of all threads.

```dbgcmd
0:000> ~* k
```

The following command freeze the thread that caused the current exception.

```dbgcmd
0:000> ~# f
```

The following command checks that the status of this thread is suspended.

```dbgcmd
0:000> ~* k
```

The following command unfreezes thread number 123.

```dbgcmd
0:000> ~123 u
```

 

 





