---
title: CTRL+K (Change Post-Reboot Break State)
description: The CTRL+K key changes the conditions on which the debugger will automatically break into the target computer.
ms.assetid: 74f57775-63ad-4a96-9ba5-bfedd4c8c826
keywords: ["CTRL+K (Change Post-Reboot Break State) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CTRL+K (Change Post-Reboot Break State)
api_type:
- NA
ms.localizationpriority: medium
---

# CTRL+K (Change Post-Reboot Break State)


The CTRL+K key changes the conditions on which the debugger will automatically break into the target computer.

KD Syntax

```dbgcmd
CTRL+K  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+K 
```

## <span id="ddk_meta_ctrl_k_dbg"></span><span id="DDK_META_CTRL_K_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Debuggers</strong></p></td>
<td align="left"><p>KD and WinDbg only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>kernel mode only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an overview of related commands and an explanation of how the reboot process affects the debugger, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

Remarks
-------

This control key causes the kernel debugger to cycle through the following three states:

<span id="No_break"></span><span id="no_break"></span><span id="NO_BREAK"></span>**No break**  
In this state, the debugger will not break into the target computer unless you press [**CTRL+C**](ctrl-c--break-.md).

<span id="Break_on_reboot"></span><span id="break_on_reboot"></span><span id="BREAK_ON_REBOOT"></span>**Break on reboot**  
In this state, the debugger will break into a rebooted target computer after the kernel initializes. This is equivalent to starting KD or WinDbg with the **-b**[command-line option](command-line-options.md).

<span id="Break_on_first_module_load"></span><span id="break_on_first_module_load"></span><span id="BREAK_ON_FIRST_MODULE_LOAD"></span>**Break on first module load**  
In this state, the debugger will break into a rebooted target computer after the first kernel module is loaded. (This will cause the break to occur earlier than in the **Break on reboot** option.) This is equivalent to starting KD or WinDbg with the **-d**[command-line option](command-line-options.md).

When CTRL+K is used, the new break state is displayed.

In WinDbg, this can also be accomplished by selecting [Debug | Kernel Connection | Cycle Initial Break](debug---kernel-connection---cycle-initial-break.md).

 

 





