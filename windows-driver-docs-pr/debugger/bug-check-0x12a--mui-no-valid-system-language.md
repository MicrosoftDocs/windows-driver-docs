---
title: Bug Check 0x12A MUI_NO_VALID_SYSTEM_LANGUAGE
description: The MUI_NO_VALID_SYSTEM_LANGUAGE bug check has a value of 0x0000012A. This indicates that Windows did not find any installed, licensed language packs for the system default UI language.
ms.assetid: 6424FC7D-BD39-4F35-9E72-E9730D27CC24
keywords: ["Bug Check 0x12A MUI_NO_VALID_SYSTEM_LANGUAGE", "MUI_NO_VALID_SYSTEM_LANGUAGE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MUI_NO_VALID_SYSTEM_LANGUAGE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12A: MUI\_NO\_VALID\_SYSTEM\_LANGUAGE


The MUI\_NO\_VALID\_SYSTEM\_LANGUAGE bug check has a value of 0x0000012A. This indicates that Windows did not find any installed, licensed language packs for the system default UI language.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MUI\_NO\_VALID\_SYSTEM\_LANGUAGE Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">The subtype of the bugcheck
<p>0x1 : Windows did not find any installed language packs during phase I initialization.</p>
Parameter 2 - NT status code that describes the reason of failure.
<p>0x2 : Windows did not find any installed, licensed language packs for the system default UI language during kernel cache creation.</p>
Parameter 2 - NT status code that describes the reason of failure.
.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Reserved</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




