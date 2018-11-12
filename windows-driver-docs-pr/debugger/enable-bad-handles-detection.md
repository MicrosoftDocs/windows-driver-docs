---
title: Enable bad handles detection
description: Enable bad handles detection
ms.assetid: beeecb82-a270-416e-8a2a-dd64af3d052e
keywords: ["Enable bad handles detection (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable bad handles detection


## <span id="ddk_enable_bad_handles_detection_dtools"></span><span id="DDK_ENABLE_BAD_HANDLES_DETECTION_DTOOLS"></span>


The **Enable bad handles detection** flag raises a user-mode exception (STATUS\_INVALID\_HANDLE) whenever a user-mode process passes an invalid handle to the Object Manager.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>bhd</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x40000000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_ENABLE_HANDLE_EXCEPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

 

 





