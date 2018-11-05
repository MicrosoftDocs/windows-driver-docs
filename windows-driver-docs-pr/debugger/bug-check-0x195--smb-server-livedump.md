---
title: Bug Check 0x195 SMB_SERVER_LIVEDUMP
description: The SMB_SERVER_LIVEDUMP bug check has a value of 0x00000195. This indicates the SMB server detected a problem and has captured a kernel dump to collect debug information.
ms.assetid: 302BA6E0-DC7C-4AE7-BD4D-C6F6A74D82D9
keywords: ["Bug Check 0x195 SMB_SERVER_LIVEDUMP", "SMB_SERVER_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- SMB_SERVER_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x195: SMB\_SERVER\_LIVEDUMP


The SMB\_SERVER\_LIVEDUMP bug check has a value of 0x00000195. This indicates the SMB server detected a problem and has captured a kernel dump to collect debug information.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## SMB\_SERVER\_LIVEDUMP Parameters


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
<td align="left"><p>0x1 : An I/O failed to complete in a reasonable amount of time.</p>
2 - Pointer to the I/O&#39;s SRV2_WORK_ITEM</td>
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

 

 

 




