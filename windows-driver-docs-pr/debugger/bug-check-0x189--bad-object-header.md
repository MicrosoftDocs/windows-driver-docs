---
title: Bug Check 0x189 BAD_OBJECT_HEADER
description: The BAD_OBJECT_HEADER bug check has a value of 0x00000189. This indicates that The OBJECT_HEADER has been corrupted.
ms.assetid: 1B4F586A-2DFB-421A-863B-CC706FB4795B
keywords: ["Bug Check 0x189 BAD_OBJECT_HEADER", "BAD_OBJECT_HEADER"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- BAD_OBJECT_HEADER
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x189: BAD\_OBJECT\_HEADER


The BAD\_OBJECT\_HEADER bug check has a value of 0x00000189. This indicates that The OBJECT\_HEADER has been corrupted.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## BAD\_OBJECT\_HEADER Parameters


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
<td align="left">Pointer to bad OBJECT_HEADER</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Pointer to the resulting OBJECT_TYPE based on the TypeIndex in the OBJECT_HEADER</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left"><p>Type of corruption.</p>
0x0 : The type index is corrupt
0x1 : The object security descriptor is invalid</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




