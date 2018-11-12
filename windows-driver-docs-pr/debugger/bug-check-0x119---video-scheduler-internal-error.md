---
title: Bug Check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR
description: The VIDEO_SCHEDULER_INTERNAL_ERROR bug check has a value of 0x00000119. This indicates that the video scheduler has detected a fatal violation.
ms.assetid: dfffdd70-c519-4e39-a604-a0ba2217093b
keywords: ["Bug Check 0x119 VIDEO_SCHEDULER_INTERNAL_ERROR", "VIDEO_SCHEDULER_INTERNAL_ERROR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_SCHEDULER_INTERNAL_ERROR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x119: VIDEO\_SCHEDULER\_INTERNAL\_ERROR


The VIDEO\_SCHEDULER\_INTERNAL\_ERROR bug check has a value of 0x00000119. This indicates that the video scheduler has detected a fatal violation.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_SCHEDULER\_INTERNAL\_ERROR Parameters


Parameter 1 is the only parameter of interest and identifies the exact violation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Cause of Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1</p></td>
<td align="left"><p>The driver has reported an invalid fence ID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>The driver failed upon the submission of a command.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>The driver failed upon patching the command buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>The driver reported an invalid flip capability.</p></td>
</tr>
</tbody>
</table>

 

 

 




