---
title: Bug Check 0xED UNMOUNTABLE\_BOOT\_VOLUME
description: The UNMOUNTABLE\_BOOT\_VOLUME bug check has a value of 0x000000ED. This indicates that the I/O subsystem attempted to mount the boot volume and it failed.
ms.assetid: 7c4ab301-f110-4fc8-9ff8-242e0d2155fd
keywords: ["Bug Check 0xED UNMOUNTABLE_BOOT_VOLUME", "UNMOUNTABLE_BOOT_VOLUME"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- UNMOUNTABLE_BOOT_VOLUME
api_type:
- NA
---

# Bug Check 0xED: UNMOUNTABLE\_BOOT\_VOLUME


The UNMOUNTABLE\_BOOT\_VOLUME bug check has a value of 0x000000ED. This indicates that the I/O subsystem attempted to mount the boot volume and it failed.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](http://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## UNMOUNTABLE\_BOOT\_VOLUME Parameters


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
<td align="left"><p>The device object of the boot volume</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The status code from the file system that describes why it failed to mount the volume</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

 

 




