---
title: Bug Check 0xD9 LOCKED_PAGES_TRACKER_CORRUPTION
description: The LOCKED_PAGES_TRACKER_CORRUPTION bug check has a value of 0x000000D9. This indicates that the internal locked-page tracking structures have been corrupted.
keywords: ["Bug Check 0xD9 LOCKED_PAGES_TRACKER_CORRUPTION", "LOCKED_PAGES_TRACKER_CORRUPTION"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- LOCKED_PAGES_TRACKER_CORRUPTION
api_type:
- NA
---

# Bug Check 0xD9: LOCKED\_PAGES\_TRACKER\_CORRUPTION


The LOCKED\_PAGES\_TRACKER\_CORRUPTION bug check has a value of 0x000000D9. This indicates that the internal locked-page tracking structures have been corrupted.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## LOCKED\_PAGES\_TRACKER\_CORRUPTION Parameters


Parameter 1 indicates the type of violation. The meaning of the other parameters depends on the value of Parameter 1.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Parameter 2</th>
<th align="left">Parameter 3</th>
<th align="left">Parameter 4</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The address of the memory descriptor list</p></td>
<td align="left"><p>The number of pages locked for the current process</p></td>
<td align="left"><p>The MDL is being inserted twice on the same process list.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The address of the memory descriptor list</p></td>
<td align="left"><p>The number of pages locked for the current process</p></td>
<td align="left"><p>The MDL is being inserted twice on the systemwide list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The address of the first internal tracking structure found</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The address of the memory descriptor list</p></td>
<td align="left"><p>The MDL was found twice in the process list when being freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The address of the internal lock tracking structure</p></td>
<td align="left"><p>The address of the memory descriptor list</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>The MDL was found in the systemwide list on free after it was removed.</p></td>
</tr>
</tbody>
</table>

 

## Cause

The error is indicated by the value of Parameter 1.

 

 




