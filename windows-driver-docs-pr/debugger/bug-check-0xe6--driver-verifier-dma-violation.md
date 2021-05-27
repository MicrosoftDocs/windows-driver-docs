---
title: Bug Check 0xE6 DRIVER_VERIFIER_DMA_VIOLATION
description: The DRIVER_VERIFIER_DMA_VIOLATION bug check has a value of 0x000000E6. This is the bug check code for all Driver Verifier DMA Verification violations.
keywords: ["Bug Check 0xE6 DRIVER_VERIFIER_DMA_VIOLATION", "DRIVER_VERIFIER_DMA_VIOLATION"]
ms.date: 05/07/2019
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

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

> [!NOTE]
> The E6 major bugcheck code can be observed when Driver Verifier is not enabled. Please see the [DMA Verification](../devtest/dma-verification.md) page for more information if you are experiencing this code without Driver Verifier enabled. 

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
<td align="left"><p>0x00 - Miscellaneous DMA error.</p></td>
<td align="left"><p>This code can represent two kinds of errors as indicated by parameter 2:</p>
<p>0x1 - The driver tried to flush too many bytes to the end of the map register file. 
<p>Parameter 3 - Number of bytes left in the MDL.</p>
<p>Parameter 4 - Number of bytes left requested to be flushed.</p>
<p>0x2 - Windows has run out of contiguous map registers. </p>
<p>Parameter 3 - Map registers needed.</p>
<p>Parameter 4 - Number of contiguous map registers. </p></td>
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
<td align="left"><p>The driver freed too many DMA common buffers. Usually this means it freed the same buffer two times. </p>
<p>Parameter 2 - Number of extra common buffers freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x04</p></td>
<td align="left"><p>The driver freed too many DMA adapter channels. Usually this means it freed the same adapter channel two times.</p>
<p> Parameter 2 - Number of extra adapter channels freed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x05</p></td>
<td align="left"><p>The driver freed too many DMA map registers. Usually this means it freed the same map register two times. </p>
<p>Parameter 2 - Number of extra map registers freed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x06</p></td>
<td align="left"><p>The driver freed too many DMA scatter/gather lists. Usually this means it freed the same scatter/gather list two times.</p>
<p>Parameter 2 - Allocated scatter-gather lists. </p>
<p>Parameter 3 - Freed scatter-gather lists.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x07</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all its common buffers. </p>
<p> Parameter 2 - Pointer to the DMA adapter.</p>
<p> Parameter 3 - Number of outstanding common buffers.</p>
<p> Parameter 4 - Pointer to the corresponding internal verifier data. </p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x08</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all adapter channels, common buffers, or scatter/gather lists. <p> <p> Parameter 2 - Pointer to the DMA adapter.
<p> Parameter 3 - Number of outstanding adapter channels.
<p> Parameter 4 - Pointer to the corresponding internal verifier data.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x09</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all map registers.</p> 
<p>Parameter 2 - Pointer to the DMA adapter.</p>
<p>Parameter 3 - Number of outstanding map registers.</p>
<p>Parameter 4 - Pointer to the corresponding internal verifier data.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x0A</p></td>
<td align="left"><p>The driver tried to release the adapter without first freeing all its scatter/gather lists. </p>
<p>Parameter 2 - Pointer to the DMA adapter.</p>
<p>Parameter 3 - Number of outstanding scatter-gather lists.</p>
<p>Parameter 4 - Pointer to the corresponding internal verifier data.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x0B</p></td>
<td align="left"><p>The driver has allocated too many adapter channels at the same time (Only one adapter channel is permitted per adapter.)</p>
<p>Parameter 2 - Outstanding adapter channels.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x0C</p></td>
<td align="left"><p>The driver tried to allocate too many map registers at the same time. </p>
<p>Parameter 2 - Required map registers.</p>
<p>Parameter 3 - Maximum map registers.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x0D</p></td>
<td align="left"><p>The driver did not flush its adapter buffers.</p>
<p>Parameter 2 - Number of bytes mapped.</p>
<p>Parameter 3 - Maximum number of bytes that can be mapped at a time.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x0E</p></td>
<td align="left"><p>The driver tried a DMA transfer without locking the buffer. The buffer in question was in paged memory. </p>
<p>Parameter 2 - Address of the DMA buffer MDL.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x0F</p></td>
<td align="left"><p>The driver or the hardware wrote outside its allocated DMA buffer. Parameter 2 is the Violation code.</p>

<p>0x01 : The tag before the DMA buffer has been modified.Expected tag is DmaVrfy0.</p>
<p>Parameter 3 - Buffer length.</p>
<p>Parameter 4 - Buffer start.</p>
<p>0x02 : The tag after the DMA buffer has been modified.</p>
Expected tag is DmaVrfy0.
<p>Parameter 3 - Buffer length.</p>
<p>Parameter 4 - Buffer start.</p>
0x03 : Free map register was overwritten.</p>
<p>Parameter 3 - Corruption address. Expected fill pattern is 0x0F.</p>
0x04 : Padding before the buffer has been incorrectly modified.</p>
<p>Parameter 3 - Buffer start. Expected padding is 0x0F.</p>
<p>Parameter 4 - Corruption address.</p>
0x05 : Padding after the buffer has been incorrectly modified.</p>
<p>Parameter 3 - Buffer start.</p>
<p>Parameter 4 - Corruption address. Expected padding pattern is 0x0F.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x10</p></td>
<td align="left"><p>The driver tried to free its map registers while some were still mapped. </p>
<p>Parameter 2 - Number of registers still mapped.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x11</p></td>
<td align="left"><p>The driver has too many outstanding reference counts for the adapter. </p>
<p>Parameter 2 - Reference count.</p>
<p>Parameter 3 - Pointer to the DMA adapter.</p>
<p>Parameter 4 - Pointer to the corresponding internal verifier data.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x13</p></td>
<td align="left"><p>The driver called a DMA routine at an improper IRQL. Parameter 2 is the Violation code.</p>
 0x01 : Current IRQL is different than expected.
<p>Parameter 3 - Expected IRQL.</p>
<p>Parameter 4 - Current IRQL.</p>
 0x02 : Current IRQL is higher than expected.</p>
<p>Parameter 3 - Expected maximum IRQL.</p>
<p>Parameter 4 - Current IRQL.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x14</p></td>
<td align="left"><p>The driver called a DMA routine at an improper IRQL.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x15</p></td>
<td align="left"><p>The driver tried to allocate too many map registers.</p> 
<p>Parameter 2 - Allocated map registers.</p>
<p>Parameter 3 - Maximum map registers.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x16</p></td>
<td align="left"><p>The driver tried to flush a buffer that is not mapped. </p>
<p>Parameter 2 - Address in the system virtual space of the map register.</p>
<p>Parameter 3 - Pointer to the corresponding internal verifier data.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x18</p></td>
<td align="left"><p>The driver tried a DMA operation by using an adapter that was already released and no longer exists. </p>
<p>Parameter 2 - Pointer to the DMA adapter.</p>
<p>Parameter 3 - Pointer to the corresponding internal verifier data.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x19</p></td>
<td align="left"><p>The driver passed a null DMA_ADAPTER value to a HAL routine.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x1B</p></td>
<td align="left"><p>The driver passed an address and MDL to a HAL routine. However, this address is not within the bounds of this MDL. </p>
<p>Parameter 2 - Virtual address that is out of MDL bounds.</p>
<p>Parameter 3 - MDL.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x1D</p></td>
<td align="left"><p>The driver tried to map an address range that was already mapped. </p>
<p>Parameter 2 - Buffer to map start. </p>
<p>Parameter 3 - Buffer to map end. </p>
<p>Parameter 4 - System address in buffer that is already mapped.
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x1E</p></td>
<td align="left"><p>The driver called <strong>HalGetAdapter</strong>. This function is obsolete -- you must use <strong>IoGetDmaAdapter</strong> instead.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x1F</p></td>
<td align="left"><p> Invalid DMA buffer. The driver referenced an invalid system address -- either before the first MDL, or after the end of the first MDL, or by using a transfer length that is longer than the MDL buffer and crosses a page boundary within the MDL.Parameter 2 is the Violation code.</p>
<p>0x01 : Virtual buffer address is before the first MDL.</p>
<p>Parameter 3 - Virtual address of the start of the DMA buffer.</p>
<p>Parameter 4 - Pointer to the first MDL describing the DMA buffer.</p>

<p>0x02 : Virtual address is after the first MDL.</p>
<p>Parameter 3 - Virtual address of the start of the DMA buffer.</p>
<p>Parameter 4 - Pointer to the first MDL describing the DMA buffer.</p>

<p>0x03 : Extra transfer length crosses a page boundary.</p>
<p>Parameter 3 - Pointer to the MDL describing the DMA buffer.</p>
<p>Parameter 4 - Length of the DMA transfer.

<p>0x04 : Virtual address of a DMA buffer is not cache aligned.
<p>Parameter 3 - Virtual address of the start of the DMA buffer.</p>
<p>Parameter 4 - Pointer to MDL describing the DMA buffer.</p>

<p>0x05 : DMA buffer length is not cache aligned.</p>
<p>Parameter 3 - Length of the DMA buffer.</p>
<p>Parameter 4 - Pointer to MDL describing the DMA buffer.
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x20</p></td>
<td align="left"><p>The driver tried to flush a map register that hasn't been mapped.</p>
<p>Parameter 2 - Map register base.</p>
<p>Parameter 3 - The VA of the start of the DMA buffer.</p>
<p>Parameter 4 - Pointer to the MDL used to describe the DMA buffer.</p>
</td>
</tr>
<tr class="even">
<td align="left"><p>0x21</p></td>
<td align="left"><p>The driver tried to map a zero-length buffer for transfer.</p>
<p>Parameter 2 - Pointer to the corresponding internal verifier data.</p>
</td>
</tr>
<tr class="odd">
<td align="left"><p>0x22</p></td>
<td align="left"><p>DMA buffer not mapped in system VA.</p>
<p>Parameter 2 - MDL</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x23</p></td>
<td align="left"><p>Cannot flush a channel that hasn't been completed or cancelled. </p>
<p>Parameter 2 - Violation code. </p>
<p>Value: 0x00 : Illegal channel flush </p>
<p>Parameter 3 - Controller Id.</p>
<p>Parameter 4 - Channel Number.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x24</p></td>
<td align="left"><p>Insufficient buffer for requested length.</p>
<p>Parameter 2 - Unaccounted length.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x25</p></td>
<td align="left"><p>Unknown device description version.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x26</p></td>
<td align="left"><p>IOMMU detected DMA violation. </p>
<p>Parameter 2 - Device Object of faulting device.</p>
<p>Parameter 3 - Faulting information (usually faulting physical address).</p>
<p>Parameter 4 - Fault type (hardware specific).</p></td>
</tr>
</tbody>
</table>

 

## Cause

See the description of each code in the Parameters section for a description of the cause.

## Resolution

This bug check can only occur when Driver Verifier has been instructed to monitor one or more drivers. If you did not intend to use Driver Verifier, you should deactivate it. You might also consider removing the driver that caused this problem.

If you are the driver writer, use the information obtained through this bug check to fix the bugs in your code.

For more information on Driver Verifier, see [Driver Verifier](../devtest/driver-verifier.md).

 

