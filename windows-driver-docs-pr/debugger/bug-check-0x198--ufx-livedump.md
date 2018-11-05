---
title: Bug Check 0x198 UFX_LIVEDUMP
description: The UFX_LIVEDUMP bug check has a value of 0x00000198. This indicates that a UFX live dump occurred.
ms.assetid: 319F8BA5-8522-43E6-B06F-6BC021FF8411
keywords: ["Bug Check 0x198 UFX_LIVEDUMP", "UFX_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- UFX_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x198: UFX\_LIVEDUMP


The UFX\_LIVEDUMP bug check has a value of 0x00000198. This indicates that a UFX live dump occurred.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UFX\_LIVEDUMP Parameters


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
<td align="left"><p>Failure type</p>
<p>0x1 : A class driver failed to activate the bus.</p>
2 - Mask of enumerated child PDOs
3 - Mask of activated child PDOs
4 - Reserved</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 1</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 1</td>
</tr>
</tbody>
</table>

 

 

 




