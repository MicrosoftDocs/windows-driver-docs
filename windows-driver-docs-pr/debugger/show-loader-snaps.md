---
title: Show Loader Snaps
description: Show loader snaps
keywords: ["Show loader snaps (global flag)"]
ms.date: 05/23/2017
---

# Show loader snaps


## <span id="ddk_show_loader_snaps_dtools"></span><span id="DDK_SHOW_LOADER_SNAPS_DTOOLS"></span>


The **Show loader snaps** flag captures detailed information about the loading and unloading of executable images and their supporting library modules and displays the data in the kernel debugger console.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>sls</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x2</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_SHOW_LDR_SNAPS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag, image file registry entry</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For system-wide (registry or kernel flag), this flag displays information about driver loading and unloading operations.

For per-process (image file), this flag displays information about loading and unloading of DLLs.

 

 