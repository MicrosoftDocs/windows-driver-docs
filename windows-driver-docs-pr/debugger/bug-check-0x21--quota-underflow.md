---
title: Bug Check 0x21 QUOTA_UNDERFLOW
description: The QUOTA_UNDERFLOW bug check has a value of 0x00000021. This indicates that quota charges have been mishandled by returning more quota to a particular block than was previously charged.
ms.assetid: 41b1c93b-77e0-4baa-8eed-7a956e45d144
keywords: ["Bug Check 0x21 QUOTA_UNDERFLOW", "QUOTA_UNDERFLOW"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- QUOTA_UNDERFLOW
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x21: QUOTA\_UNDERFLOW


The QUOTA\_UNDERFLOW bug check has a value of 0x00000021. This indicates that quota charges have been mishandled by returning more quota to a particular block than was previously charged.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## QUOTA\_UNDERFLOW Parameters


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
<td align="left"><p>1</p></td>
<td align="left"><p>The process that was initially charged, if available.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The quota type. For the list of all possible quota type values, see the header file Ps.h in the Windows Driver Kit (WDK).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The initial charged amount of quota to return.</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The remaining amount of quota that was not returned.</p></td>
</tr>
</tbody>
</table>

 

 

 




