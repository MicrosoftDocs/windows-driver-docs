---
title: Enable system critical breaks
description: Enable system critical breaks
keywords: ["Enable system critical breaks (global flag)"]
ms.date: 05/23/2017
---

# Enable system critical breaks


## <span id="ddk_enable_system_critical_breaks_dtools"></span><span id="DDK_ENABLE_SYSTEM_CRITICAL_BREAKS_DTOOLS"></span>


The **Enable system critical breaks** flag forces a system break into the debugger.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>scb</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x100000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_ENABLE_SYSTEM_CRIT_BREAKS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When set for a process (image file), this flag forces a system break into the debugger whenever the specified process stops abnormally. This flag is effective only when the process calls the **RtlSetProcessBreakOnExit** and **RtlSetThreadBreakOnExit** interfaces.

When set system-wide (registry or kernel flag), this flag forces a system break into the debugger whenever processes that have called the **RtlSetProcessBreakOnExit** and **RtlSetThreadBreakOnExit** interfaces stop abnormally.

 

 