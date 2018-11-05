---
title: Bug Check 0xF8 RAMDISK_BOOT_INITIALIZATION_FAILED
description: The RAMDISK_BOOT_INITIALIZATION_FAILED bug check has a value of 0x000000F8. This indicates that an initialization failure occurred while attempting to boot from the RAM disk.
ms.assetid: 73b053af-6ecb-48a3-b09d-e28d39390d11
keywords: ["Bug Check 0xF8 RAMDISK_BOOT_INITIALIZATION_FAILED", "RAMDISK_BOOT_INITIALIZATION_FAILED"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- RAMDISK_BOOT_INITIALIZATION_FAILED
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xF8: RAMDISK\_BOOT\_INITIALIZATION\_FAILED


The RAMDISK\_BOOT\_INITIALIZATION\_FAILED bug check has a value of 0x000000F8. This indicates that an initialization failure occurred while attempting to boot from the RAM disk.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## RAMDISK\_BOOT\_INITIALIZATION\_FAILED Parameters


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
<td align="left"><p>Indicates the cause of the failure.</p>
<p><strong>1:</strong> No LoaderXIPRom descriptor was found in the loader memory list.</p>
<p><strong>2:</strong> Unable to open the RAM disk driver (ramdisk.sys or \Device\Ramdisk).</p>
<p><strong>3:</strong> FSCTL_CREATE_RAM_DISK failed.</p>
<p><strong>4:</strong> Unable to create GUID string from binary GUID.</p>
<p><strong>5:</strong> Unable to create symbolic link pointing to the RAM disk device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>NTSTATUS code</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>0</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>0</p></td>
</tr>
</tbody>
</table>

 

 

 




