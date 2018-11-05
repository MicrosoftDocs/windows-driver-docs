---
title: sq (Set Quiet Mode)
description: The sq command turns quiet mode on or off.
ms.assetid: db8a266c-e2e5-4de7-8154-993a78585f04
keywords: ["sq (Set Quiet Mode) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- sq (Set Quiet Mode)
api_type:
- NA
ms.localizationpriority: medium
---

# sq (Set Quiet Mode)


The **sq** command turns quiet mode on or off.

```dbgcmd
sq 
sq{e|d} 
```

## <span id="ddk_cmd_set_quiet_mode_dbg"></span><span id="DDK_CMD_SET_QUIET_MODE_DBG"></span>


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

The **sqe** command turns quiet mode on, and the **sqd** command turns it off. The **sq** command turns on and off quiet mode. Each of these commands also displays the new quiet mode status.

You can set quiet mode in KD or kernel-mode WinDbg by using the KDQUIET [environment variable](kernel-mode-environment-variables.md). (Note that quiet mode exists in both user-mode and kernel-mode debugging, but the KDQUIET environment variable is only recognized in kernel mode.)

*Quiet mode* has three distinct effects:

-   The debugger does not display messages every time that an extension DLL is loaded or unloaded.

-   The [**r (Registers)**](r--registers-.md) command no longer requires an equal sign (=) in its syntax.

-   When you break into a target computer while kernel debugging, the long warning message is suppressed.

Do not confuse quiet mode with the effects of the **-myob** [command-line option](command-line-options.md) (in CDB and KD) or the **-Q** [**command-line option**](windbg-command-line-options.md) (in WinDbg).

 

 





