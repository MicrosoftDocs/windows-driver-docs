---
title: Bug Check 0x73 CONFIG_LIST_FAILED
description: The CONFIG_LIST_FAILED bug check has a value of 0x00000073. This bug check indicates that one of the top-level registry keys, also known as core system hives, cannot be linked in the registry tree.
ms.assetid: fec1f3ee-5405-49c2-8082-75adfdabd6b8
keywords: ["Bug Check 0x73 CONFIG_LIST_FAILED", "CONFIG_LIST_FAILED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- CONFIG_LIST_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x73: CONFIG\_LIST\_FAILED


The CONFIG\_LIST\_FAILED bug check has a value of 0x00000073. This bug check indicates that one of the top-level registry keys, also known as core system hives, cannot be linked in the registry tree.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## CONFIG\_LIST\_FAILED Parameters


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
<td align="left"><p>1</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The NT status code that led the Windows operating system to assume that it failed to load the hive</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>The index of the hive in the hive list</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>A pointer to a UNICODE_STRING structure that contains the file name of the hive</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

The registry hive that cannot be linked might be SAM, SECURITY, SOFTWARE, or DEFAULT. The hive is valid, because it was loaded successfully.

Examine Parameter 2 to see why the hive could not be linked in the registry tree. One common cause of this error is that the Windows operating system is out of disk space on the system drive. (In this situation, this parameter is 0xC000017D, STATUS\_NO\_LOG\_SPACE.) Another common problem is that an attempt to allocate pool has failed. (In this situation, Parameter 2 is 0xC000009A, STATUS\_INSUFFICIENT\_RESOURCES.) You must investigate other status codes.

 

 




