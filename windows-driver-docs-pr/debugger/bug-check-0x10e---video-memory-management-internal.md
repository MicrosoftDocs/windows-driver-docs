---
title: Bug Check 0x10E VIDEO_MEMORY_MANAGEMENT_INTERNAL
description: The VIDEO_MEMORY_MANAGEMENT_INTERNAL bug check has a value of 0x0000010E. This indicates that the video memory manager has encountered a condition that it is unable to recover from.
keywords: ["Bug Check 0x10E VIDEO_MEMORY_MANAGEMENT_INTERNAL", "VIDEO_MEMORY_MANAGEMENT_INTERNAL"]
ms.date: 10/14/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- VIDEO_MEMORY_MANAGEMENT_INTERNAL
api_type:
- NA
---

# Bug Check 0x10E: VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL


The VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL bug check has a value of 0x0000010E. This indicates that the video memory manager has encountered a condition that it is unable to recover from.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VIDEO\_MEMORY\_MANAGEMENT\_INTERNAL Parameters


Parameter 1 describes the type of video memory error. Values for Parameter 1 that do not appear in this table must be individually examined.

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
</tbody>
</table>

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
<td align="left"><p>An attempt to release a pinned allocation's resource failed.</p></td>
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
<td align="left"><p>0x1C</p></td>
<td align="left"><p>VidMm is trying to rotate an allocation back from the frame buffer but the VA isn't rotated where it was expected.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1D</p></td>
<td align="left"><p>VidMm is trying to use paging buffer that have been unmapped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1E</p></td>
<td align="left"><p>VidMm is trying to do an operation from the wrong process context.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1F</p></td>
<td align="left"><p>VidMm is trying to mark an allocation with a lower fence than it is currently marked with.</p></td>
</tr>
</tbody>
</table>

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
<tr class="even">
<td align="left"><p>0x20</p></td>
<td align="left"><p>VidMm is trying to manipulate an allocation is assumed was idle but isn't.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x21</p></td>
<td align="left"><p>VidMm is trying to flush the paging buffer outside of preparation or unflushed data was found in the paging buffer at the start of a preparation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x22</p></td>
<td align="left"><p>VidMm is trying to rotate a VA to an invalid range.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x23</p></td>
<td align="left"><p>The scheduler wake up a thread before the wait was completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x24</p></td>
<td align="left"><p>An allocation is being destroyed which has outstanding references to its backing store... physical memory will be leaked.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x25</p></td>
<td align="left"><p>The GPU attempted to write over an undefined area of the aperture.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x26</p></td>
<td align="left"><p>A VIDMM_LOCAL_ALLOC was closed from a process other than its owner.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x27</p></td>
<td align="left"><p>A VIDMM_ALLOC was not reprogrammed at the current split point.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x28</p></td>
<td align="left"><p>An unexpected exception happened when referencing a global allocation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x29</p></td>
<td align="left"><p>An overflow or an underflow was detected when manipulating a VIDMM_ALLOC DMA reference count.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2A</p></td>
<td align="left"><p>VidMm is trying to free the last reference to the currently displaying allocation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2B</p></td>
<td align="left"><p>VidMm is trying to free the an invalid Cpu Host Aperture page range.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2C</p></td>
<td align="left"><p>VidMm is trying to map a page range to the Cpu Host Aperture which was previously already mapped. Best case memory leak.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2D</p></td>
<td align="left"><p>Call to DdiMapCpuHostAperture failed, but was expected to succeed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x2E</p></td>
<td align="left"><p>Call to DdiUnmapCpuHostAperture failed, but was expected to succeed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2F</p></td>
<td align="left"><p>Reported range size does not match the number of elements allocated for the array.</p></td>
</tr>
</tbody>
</table>

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
<td align="left"><p>0x30</p></td>
<td align="left"><p>An error occurred during a GPU virtual address operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x31</p></td>
<td align="left"><p>The paging queue being deleted is still being processed by the VidMm worker thread.
</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x32</p></td>
<td align="left"><p>The paging queue being deleted still contains running packets.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x33</p></td>
<td align="left"><p>The device is being destroyed but there are still allocations resident on it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x34</p></td>
<td align="left"><p>A heap allocation has received a state transition event incompatible with current state.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x35</p></td>
<td align="left"><p>The paging request failed at default paging queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x36</p></td>
<td align="left"><p>The paging request failed on a paging packet or device resume that was previously marked as unrecoverable, and was expected to succeed subsequent calls.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x37</p></td>
<td align="left"><p>VidMm failed to lock pages of an allocation during TDR.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x38</p></td>
<td align="left"><p>VidMm is freeing an allocation that still has paging packets referencing it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x39</p></td>
<td align="left"><p>VidMm is putting a device to the indefinite penalty box, but it has paging packets.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3A</p></td>
<td align="left"><p>VidMm worker thread is running a paging queue that became suspended.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3B</p></td>
<td align="left"><p>Memory is still rotated to the frame buffer during D3 transition.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3C</p></td>
<td align="left"><p>Memory is still allocated or mapped to the CPU host aperture. This indicates memory may still be rotated to the frame buffer during a D3 transition.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3D</p></td>
<td align="left"><p>An invalid segment group was specified during an operation.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3E</p></td>
<td align="left"><p>Failed to acquire the VIDMM_ALLOC rundown protection.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3F</p></td>
<td align="left"><p>Resuming the scheduler device during a move or defragment operation conflicts with the penalty box state. This implies we will be resuming the scheduler for a device whose memory is not accessible yet.</p></td>
</tr>
</tbody>
</table>

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
<tr class="even">
<td align="left"><p>0x40</p></td>
<td align="left"><p>Attempting to start a preparation bracket while another operation is already in progress.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x41</p></td>
<td align="left"><p>Deleting a VIDMM_CROSSADAPTER_ALLOC that has non-zero residency or adapter count.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x42</p></td>
<td align="left"><p>Deleting a VIDMM_CROSSADAPTER_ALLOC that has a negative residency or adapter count.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x43</p></td>
<td align="left"><p>While saving or restoring the reserved frame buffer content, we were unable to map at least one page of the section object to make forward progress.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x44</p></td>
<td align="left"><p>Memory budget bookkeeping ended up in an underflow.</p></td>
</tr>
</tbody>
</table>


## Cause

This bug check is usually caused by a video driver behaving improperly.

## Resolution

If the problem persists, check Windows Update for an updated video driver.

 

 




