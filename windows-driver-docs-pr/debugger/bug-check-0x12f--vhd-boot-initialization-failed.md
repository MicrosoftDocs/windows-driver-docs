---
title: Bug Check 0x12F VHD_BOOT_INITIALIZATION_FAILED
description: The VHD_BOOT_INITIALIZATION_FAILED bug check has a value of 0x0000012F. This indicates that an initialization failure occurred while attempting to boot from a VHD.
ms.assetid: CC4CD97B-FCBA-4B73-AB9E-D56387D4CB07
keywords: ["Bug Check 0x12F VHD_BOOT_INITIALIZATION_FAILED", "VHD_BOOT_INITIALIZATION_FAILED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VHD_BOOT_INITIALIZATION_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x12F: VHD\_BOOT\_INITIALIZATION\_FAILED


The VHD\_BOOT\_INITIALIZATION\_FAILED bug check has a value of 0x0000012F. This indicates that an initialization failure occurred while attempting to boot from a VHD.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VHD\_BOOT\_INITIALIZATION\_FAILED Parameters


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
<td align="left"><p>Action that failed</p>
1 : Couldn&#39;t extract VHD information from boot device.
2 : Timeout waiting for VHD parent device to surface.
3 : VHD path string memory allocation error.
4 : VHD path construction failed.
5 : VHD boot device mount failed.
6 : Disable sleep states failed.
7 : VHD information memory allocation error.
8 : VHD information construction failed.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">NT status code</td>
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

 

 

 




