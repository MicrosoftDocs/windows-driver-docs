---
title: Bug Check 0x13A KERNEL_MODE_HEAP_CORRUPTION
description: The KERNEL_MODE_HEAP_CORRUPTION bug check has a value of 0x0000013A. This indicates that the kernel mode heap manager has detected corruption in a heap.
ms.assetid: 806669B3-B811-462A-A3B6-2F583BF0E19A
keywords: ["Bug Check 0x13A KERNEL_MODE_HEAP_CORRUPTION", "KERNEL_MODE_HEAP_CORRUPTION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_MODE_HEAP_CORRUPTION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x13A: KERNEL\_MODE\_HEAP\_CORRUPTION


The KERNEL\_MODE\_HEAP\_CORRUPTION bug check has a value of 0x0000013A. This indicates that the kernel mode heap manager has detected corruption in a heap.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_MODE\_HEAP\_CORRUPTION Parameters


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
<td align="left"><p>Type of corruption detected</p>
0x3 : A corrupt entry header was detected.
0x4 : Multiple corrupt entry headers were detected.
0x5 : A corrupt entry header in a large allocation was detected.
0x6 : A corruption was detected with features consistent with a buffer overrun.
0x7 : A corruption was detected with features consistent with a buffer underrun.
0x8 : A free block was passed to an operation that is only valid for busy blocks.
0x9 : An invalid argument was specified for the current operation.
0xA : A corruption was detected with features consistent with a use-after-free error.
0xB : The wrong heap was specified for the current operation.
0xC : A corrupt free list was detected.
0xD : The heap detected list corruption in a list other than the free list.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left">Address of the heap that reported the corruption</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">Address at which the corruption was detected</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">Reserved</td>
</tr>
</tbody>
</table>

 

 

 




