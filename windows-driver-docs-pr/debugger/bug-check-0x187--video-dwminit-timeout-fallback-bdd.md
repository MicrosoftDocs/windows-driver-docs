---
title: Bug Check 0x187 VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD
description: The VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD bug check has a value of 0x00000187. This indicates that video fell back to BDD rather than using the IHV driver. This always generates a live dump.
ms.assetid: CF4AB5DB-2779-4E6E-BF27-AE320403A982
keywords: ["Bug Check 0x187 VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD", "VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x187: VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD


The VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD bug check has a value of 0x00000187. This indicates that video fell back to BDD rather than using the IHV driver. This always generates a live dump.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD Parameters


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
<td align="left">Reason Code.
<p>0x1 : DWM failed to initialize after retries, stopping display adapters and falling back to BDD</p></td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Reserved</td>
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

 

 

 




