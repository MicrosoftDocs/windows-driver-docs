---
title: CTRL+A (Toggle Baud Rate)
description: The CTRL+A key toggles the baud rate used in the kernel debugging connection.
ms.assetid: 77a95ca1-073c-480a-abda-f484adbc1d23
keywords: ["CTRL+A (Toggle Baud Rate) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CTRL+A (Toggle Baud Rate)
api_type:
- NA
ms.localizationpriority: medium
---

# CTRL+A (Toggle Baud Rate)


The CTRL+A key toggles the baud rate used in the kernel debugging connection.

KD Syntax

```dbgcmd
CTRL+A  ENTER 
```

WinDbg Syntax

```dbgcmd
CTRL+ALT+A 
```

## <span id="ddk_meta_ctrl_a_dbg"></span><span id="DDK_META_CTRL_A_DBG"></span>


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

 

Remarks
-------

This will cycle through all available baud rates for the kernel debugging connection.

Supported baud rates are 19200, 38400, 57600, and 115200. Each time this control key is used, the next baud rate will be selected. If the baud rate is already at 115200, it will be reduced to 19200.

In WinDbg, this can also be accomplished by selecting [Debug | Kernel Connection | Cycle Baud Rate](debug---kernel-connection---cycle-baud-rate.md).

You cannot actually use this control key to change the baud rate at which you are debugging. The baud rate of the host computer and the target computer must match, and the baud rate of the target computer cannot be changed without rebooting. Therefore, you only need to toggle through the baud rates if the two computers are attempting to communicate at different rates. In this case, you must change the host computer's baud rate to match that of the target computer.

 

 





