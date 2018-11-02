---
title: Bug Check 0xE6 DRIVER_VERIFIER_DMA_VIOLATION
description: The DRIVER_VERIFIER_DMA_VIOLATION bug check has a value of 0x000000E6. This is the bug check code for all Driver Verifier DMA Verification violations.
ms.assetid: badf8948-356c-4728-b34e-02f1638630a6
keywords: ["Bug Check 0xE6 DRIVER_VERIFIER_DMA_VIOLATION", "DRIVER_VERIFIER_DMA_VIOLATION"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DRIVER_VERIFIER_DMA_VIOLATION
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0xE6: DRIVER\_VERIFIER\_DMA\_VIOLATION


The DRIVER\_VERIFIER\_DMA\_VIOLATION bug check has a value of 0x000000E6. This is the bug check code for all Driver Verifier **DMA Verification** violations.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## DRIVER\_VERIFIER\_DMA\_VIOLATION Parameters


Parameter 1 is the only parameter of interest. This parameter identifies the exact violation. If a debugger is attached, an informative message is displayed in the debugger.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter 1</th>
<th align="left">Cause of Error and Debugger Message</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00</p></td>
<td align="left"><p>This code can represent two kinds of errors:</p>
<p>1. The driver tried to flush too many bytes to the end of the map register file. The number of bytes permitted and the number of bytes attempted are displayed.</p>
<p>2. Windows has run out of contiguous map registers. The number of map registers needed and the largest block of contiguous map registers is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x01</p></td>
<td align="left"><p>The performance counter has decreased. The old and new values of the counter are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x02</p></td>
<td align="left"><p>The performance counter has increased too fast. The counter value is displayed in the debugger.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x03</p></td>
<td align="left"><p>The driver freed too many DMA common buffers. Usually this means it freed the same buffer two times.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The driver freed too many DMA adapter channels. Usually this means it freed the same adapter channel two times.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x05</p></td>
<td align="left"><p>The driver freed too many DMA map registers. Usually this means it freed the same map register two times. The number of active map registers is displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The driver freed too many DMA scatter/gather lists. Usually this means it freed the same scatter/gather list two times. The number of lists allocated and the number of lists freed is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all its common buffers. The adapter address and the number of remaining buffers is displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all adapter channels, common buffers, or scatter/gather lists. The adapter address and the number of remaining items is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all map registers. The adapter address and the number of remaining map registers is displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all its scatter/gather lists. The adapter address and the number of remaining scatter/gather lists is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>HV_TOO_MANY_ADAPTER_CHANNELSThe driver has allocated too many adapter channels at the same time. . (Only one adapter channel is permitted per adapter.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>The driver tried to allocate too many map registers at the same time. The number requested and the number allowed are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>The driver did not flush its adapter buffers. The number of bytes that the driver tried to map and the maximum number of bytes allowed are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>The driver tried a DMA transfer without locking the buffer. The buffer in question was in paged memory. The address of the MDL is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The driver or the hardware wrote outside its allocated DMA buffer. The nature of the error (overrun or underrun) is displayed, as well as the relevant addresses.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>The driver tried to free its map registers while some were still mapped. The number of map registers still mapped is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x11</p></td>
<td align="left"><p>The driver has too many outstanding reference counts for the adapter. The number of reference counts and the adapter address are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>The driver called a DMA routine at an improper IRQL. The required IRQL and the actual IRQL are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>The driver called a DMA routine at an improper IRQL. The required IRQL and the actual IRQL are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The driver tried to allocate too many map registers. The number requested and the number allowed are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>The driver tried to flush a buffer that is not mapped. The address of the buffer is displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x18</p></td>
<td align="left"><p>The driver tried a DMA operation by using an adapter that was already released and no longer exists. The adapter address is displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x19</p></td>
<td align="left"><p>The driver passed a null DMA_ADAPTER value to a HAL routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>The driver passed an address and MDL to a HAL routine. However, this address is not within the bounds of this MDL. The address passed and the address of the MDL are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1D</p></td>
<td align="left"><p>The driver tried to map an address range that was already mapped. The address range and the current mapping for that range are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1E</p></td>
<td align="left"><p>The driver called <strong>HalGetAdapter</strong>. This function is obsolete -- you must use <strong>IoGetDmaAdapter</strong> instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1F</p></td>
<td align="left"><p>HV_BAD_MDLThe driver referenced an invalid system address -- either before the first MDL, or after the end of the first MDL, or by using a transfer length that is longer than the MDL buffer and crosses a page boundary within the MDL. . Either the invalid address and the first MDL address, or the MDL address and the extra transfer length are displayed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>The driver tried to flush a map register that hasn&#39;t been mapped. The map register base, flushing address, and MDL are displayed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x21</p></td>
<td align="left"><p>The driver tried to map a zero-length buffer for transfer.</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

See the description of each code in the Parameters section for a description of the cause.

Resolution
----------

This bug check can only occur when Driver Verifier has been instructed to monitor one or more drivers. If you did not intend to use Driver Verifier, you should deactivate it. You might also consider removing the driver that caused this problem.

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

The Driver Verifier **DMA Verification** option is only available in Windows XP and later versions. For full details on Driver Verifier, see the Windows Driver Kit.

 

 




