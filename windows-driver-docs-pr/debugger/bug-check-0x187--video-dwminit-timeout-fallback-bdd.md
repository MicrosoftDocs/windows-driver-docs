---
title: Bug Check 0x187 VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD
description: The VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD live dump has a value of 0x00000187. This indicates that video fell back to BDD rather than using the IHV driver. This always generates a live dump.
keywords: ["Bug Check 0x187 VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD", "VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_DWMINIT_TIMEOUT_FALLBACK_BDD
api_type:
- NA
---

# Bug Check 0x187: VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD

The VIDEO\_DWMINIT\_TIMEOUT\_FALLBACK\_BDD live dump has a value of 0x00000187. This indicates that video fell back to BDD rather than using the IHV driver. This always generates a live dump.

(This code can never be used for a real bug check; it is used to identify live dumps.)

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


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

 

 

 




