---
title: Bug Check 0xA2 MEMORY_IMAGE_CORRUPT
description: The MEMORY_IMAGE_CORRUPT bug check has a value of 0x000000A2. This bug check indicates that corruption has been detected in the image of an executable file in memory.
ms.assetid: 73990217-4af2-478c-aa5e-39e6bc5811cf
keywords: ["Bug Check 0xA2 MEMORY_IMAGE_CORRUPT", "MEMORY_IMAGE_CORRUPT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- MEMORY_IMAGE_CORRUPT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xA2: MEMORY\_IMAGE\_CORRUPT


The MEMORY\_IMAGE\_CORRUPT bug check has a value of 0x000000A2. This bug check indicates that corruption has been detected in the image of an executable file in memory.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## MEMORY\_IMAGE\_CORRUPT Parameters


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
<th align="left">Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x02</p></td>
<td align="left"><p><strong>If Parameter 3 is zero:</strong> The page number in the table page that failed</p>
<p><strong>If Parameter 3 is nonzero:</strong> The page number with the failing page run index</p></td>
<td align="left"><p>Zero, or the index that failed to match the run</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>A table page check failure occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The starting physical page number of the range</p></td>
<td align="left"><p>The length (in pages) of the range</p></td>
<td align="left"><p>The page number of the table page that contains this run</p></td>
<td align="left"><p>The checksum for the range of memory listed is incorrect.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

A cyclic redundancy check (CRC) check on the memory range has failed.

On a system wake operation, various regions of memory might be checked to guard against memory failures.

 

 




