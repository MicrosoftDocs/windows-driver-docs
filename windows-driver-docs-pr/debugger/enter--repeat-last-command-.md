---
title: ENTER (Repeat Last Command)
description: The ENTER key repeats the last command that you typed.
ms.assetid: 058e455a-8934-4b28-8cf0-2d3f09a7e7cc
keywords: ["ENTER (Repeat Last Command) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ENTER (Repeat Last Command)
api_type:
- NA
ms.localizationpriority: medium
---

# ENTER (Repeat Last Command)


The ENTER key repeats the last command that you typed.

```dbgcmd
ENTER
```

## <span id="ddk_cmd_repeat_last_command_dbg"></span><span id="DDK_CMD_REPEAT_LAST_COMMAND_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
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

 

Remarks
-------

In CDB and KD, pressing the ENTER key by itself at a command prompt reissues the command that you previously entered.

In WinDbg, the ENTER key can have no effect or you can use it to repeat the previous command. You can set this option in the **Options** dialog box. (To open the **Options** dialog box, click **Options** on the **View** menu or click the **Options** button (![screen shot of the options button](images/tbopt.png)) on the toolbar.)

If you set ENTER to repeat the last command, but you want to create white space in the [Debugger Command window](debugger-command-window.md), use the [**\* (Comment Line Specifier)**](----comment-line-specifier-.md) token and then press ENTER several times.

 

 





