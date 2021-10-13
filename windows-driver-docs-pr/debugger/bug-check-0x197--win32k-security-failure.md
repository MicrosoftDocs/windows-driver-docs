---
title: Bug Check 0x197 WIN32K_SECURITY_FAILURE
description: The WIN32K_SECURITY_FAILURE bug check has a value of 0x00000197. This indicates a security failure was detected in win32k.
keywords: ["Bug Check 0x197 WIN32K_SECURITY_FAILURE", "WIN32K_SECURITY_FAILURE"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WIN32K_SECURITY_FAILURE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x197: WIN32K\_SECURITY\_FAILURE


The WIN32K\_SECURITY\_FAILURE bug check has a value of 0x00000197. This indicates a security failure was detected in win32k.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## WIN32K\_SECURITY\_FAILURE Parameters


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
<p>0x1 : An objects handle entry didn't point back to the object.</p>
2 - Pointer to the object type
3 - Pointer to the object handle entry
4 - Expected object</td>
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

 

 

 




