---
title: Enable close exception
description: Enable close exception
ms.assetid: 4089df14-3204-4a48-b67f-cf6bd53100a5
keywords: ["Enable close exception (global flag)"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enable close exception


## <span id="ddk_enable_close_exception_dtools"></span><span id="DDK_ENABLE_CLOSE_EXCEPTION_DTOOLS"></span>


The **Enable close exception** flag raises a user-mode exception whenever an invalid handle is passed to the **CloseHandle** interface or related interfaces, such as **SetEvent**, that take handles as arguments.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>ece</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x00400000</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_ENABLE_CLOSE_EXCEPTIONS</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

**Note**   This flag is still supported, but the [Enable bad handles detection](enable-bad-handles-detection.md) flag (bhd), which performs a more comprehensive check of handle use, is preferred.

 

 

 





