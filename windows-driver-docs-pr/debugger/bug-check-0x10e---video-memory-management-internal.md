---
title: Bug Check 0x10E VIDEO_MEMORY_MANAGEMENT_INTERNAL
description: The VIDEO_MEMORY_MANAGEMENT_INTERNAL bug check has a value of 0x0000010E. This indicates that the video memory manager has encountered a condition that it is unable to recover from.
ms.assetid: 2fb29098-084c-462a-bb06-789e73924d16
keywords: ["Bug Check 0x10E VIDEO_MEMORY_MANAGEMENT_INTERNAL", "VIDEO_MEMORY_MANAGEMENT_INTERNAL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- VIDEO_MEMORY_MANAGEMENT_INTERNAL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x10E: VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL


The VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL bug check has a value of 0x0000010E. This indicates that the video memory manager has encountered a condition that it is unable to recover from.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL Parameters


Parameter 1 is the only parameter of interest; this identifies the exact violation. Values for Parameter 1 that do not appear in this table must be individually examined.

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
<td align="left"><p>An attempt was made to rotate a non-rotate range.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2</p></td>
<td align="left"><p>An attempt was made to destroy a non-empty process heap.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3</p></td>
<td align="left"><p>An attempt to unmap from an aperture segment failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x4</p></td>
<td align="left"><p>A rotation in a must-succeed path failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x5</p></td>
<td align="left"><p>A deferred command failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x6</p></td>
<td align="left"><p>An attempt was made to reallocate resources for an allocation that was having its eviction canceled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x7</p></td>
<td align="left"><p>An invalid attempt was made to defer free usage.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x8</p></td>
<td align="left"><p>The split direct memory access (DMA) buffer contains an invalid reference.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x9</p></td>
<td align="left"><p>An attempt to evict an allocation failed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xA</p></td>
<td align="left"><p>An invalid attempt to use a pinned allocation was made.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xB</p></td>
<td align="left"><p>A driver returned an invalid error code from <em>BuildPagingBuffer</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xC</p></td>
<td align="left"><p>A resource leak was detected in a segment.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xD</p></td>
<td align="left"><p>A segment is being used improperly.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0xE</p></td>
<td align="left"><p>An attempt to map an allocation into an aperture segment failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0xF</p></td>
<td align="left"><p>A driver returned an invalid error code from <em>AcquireSwizzlingRange</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x10</p></td>
<td align="left"><p>A driver returned an invalid error code from <em>ReleaseSwizzlingRange</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x11</p></td>
<td align="left"><p>An invalid attempt to use an aperture segment was made.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x12</p></td>
<td align="left"><p>A driver overflowed the provided DMA buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>A driver overflowed the provided private data buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>An attempt to purge all segments failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>An attempt was made to free a virtual address descriptor (VAD) that was still in the rotated state</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>A driver broke the guaranteed DMA buffer model contract.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x17</p></td>
<td align="left"><p>An unexpected system command failure occurred.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x18</p></td>
<td align="left"><p>An attempt to release a pinned allocation&#39;s resource failed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x19</p></td>
<td align="left"><p>A driver failed to patch a DMA buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1A</p></td>
<td align="left"><p>The owner of a shared allocation was freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>An attempt was made to release an aperture range that is still in use.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x25</p></td>
<td align="left"><p>The GPU attempted to write over an undefined area of the aperture.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

This bug check is usually caused by a video driver behaving improperly.

Resolution
----------

If the problem persists, check Windows Update for an updated video driver.

 

 




