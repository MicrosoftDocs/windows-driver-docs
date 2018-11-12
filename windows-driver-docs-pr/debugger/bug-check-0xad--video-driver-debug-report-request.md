---
title: Bug Check 0xAD VIDEO_DRIVER_DEBUG_REPORT_REQUEST
description: The VIDEO_DRIVER_DEBUG_REPORT_REQUEST bug check has a value of 0x000000AD. This bug check indicates that the video port created a non-fatal minidump on behalf of the video driver during run time.
ms.assetid: eedde484-584b-478b-9429-a9c78bb62c1e
keywords: ["Bug Check 0xAD VIDEO_DRIVER_DEBUG_REPORT_REQUEST", "VIDEO_DRIVER_DEBUG_REPORT_REQUEST"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_DRIVER_DEBUG_REPORT_REQUEST
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xAD: VIDEO\_DRIVER\_DEBUG\_REPORT\_REQUEST


The VIDEO\_DRIVER\_DEBUG\_REPORT\_REQUEST bug check has a value of 0x000000AD. This bug check indicates that the video port created a non-fatal minidump on behalf of the video driver during run time.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_DRIVER\_DEBUG\_REPORT\_REQUEST Parameters


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
<td align="left"><p>Driver-specific</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>Driver-specific</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Driver-specific</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>The number of all reports that have been requested since boot time</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The video port created a non-fatal minidump on behalf of the video driver during run time because the video driver requested a debug report.

The VIDEO\_DRIVER\_DEBUG\_REPORT\_REQUEST bug check can be caused only by minidump creation, not by the creation of a full dump or kernel dump.

 

 




