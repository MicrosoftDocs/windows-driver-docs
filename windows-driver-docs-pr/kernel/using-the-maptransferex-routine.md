---
title: Using the MapTransferEx Routine
author: windows-driver-content
description: The MapTransferEx routine initializes a set of previously allocated DMA resources and starts a DMA transfer.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 79D3DDB2-B134-43B2-A6CC-94035C793047
---

# Using the MapTransferEx Routine


The [**MapTransferEx**](https://msdn.microsoft.com/library/windows/hardware/hh406521) routine initializes a set of previously allocated DMA resources and starts a DMA transfer. This routine is available in version 3 of the DMA operations interface. Version 3 of this interface is supported starting with Windows 8. For more information about the DMA operations interface, see [**DMA\_OPERATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff544071).

## Comparison of MapTransferEx to MapTransfer


**MapTransferEx** is an improved version of the [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) routine. **MapTransfer** is available in all versions of the DMA operations interface, starting with version 1 in Windows 2000. One call to **MapTransfer** can map one contiguous block of physical memory from an MDL. However, the data buffer for a complex DMA transfer might be described by an MDL chain, and each MDL in the chain might describe several blocks of physically contiguous memory. To use **MapTransfer** to transfer such a buffer, a driver must make many calls to **MapTransfer**. Typically, these calls are made inside a pair of nested loops. The inner loop iterates from one block of contiguous physical memory to the next in each MDL, and the outer loop iterates from one MDL to the next in the MDL chain.

In contrast, one call to **MapTransferEx** can transfer the entire data buffer for a complex DMA transfer. The following three **MapTransferEx** parameters describe the buffer memory to use for the transfer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>Mdl</em></td>
<td><p>A pointer to the first MDL in a chain of one or more MDLs. For more information about MDL chains, see [Using MDLs](using-mdls.md).</p></td>
</tr>
<tr class="even">
<td><em>Offset</em></td>
<td><p>The byte offset of the buffer from start of the memory that is described by the MDL chain.</p></td>
</tr>
<tr class="odd">
<td><em>Length</em></td>
<td><p>A pointer to a location that contains the length, in bytes, of the data buffer.</p></td>
</tr>
</tbody>
</table>

 

At the start of a **MapTransferEx** call, the **MapTransferEx** routine advances through the MDL chain to find the start of the buffer. The start of the buffer is specified by the *Offset* parameter. Next, working from the start of the buffer to the end, **MapTransferEx** constructs a scatter/gather list in which each buffer fragment in the list is a physically contiguous block of memory from the MDL chain. To construct this list, **MapTransferEx** steps from one physically contiguous block of memory to the next within each MDL, and from one MDL to the next in the MDL chain. List construction finishes when the total amount of buffer memory described by the scatter/gather list equals the number of bytes specified by the \**Length* input parameter. The ordering of the buffer fragments in the resulting scatter/gather list matches the ordering of the physically contiguous blocks in the MDL chain.

## Multiple calls to MapTransferEx


**MapTransferEx** might not always be able to transfer an entire DMA data buffer in one call. The following list describes some of the conditions that might require **MapTransferEx** to be called more than once to complete the transfer:

-   The DMA adapter requires map registers, and the number of map registers assigned to the adapter is not sufficient to describe the entire buffer.
-   The storage allocated by the driver to contain the scatter/gather list is not large enough to contain the scatter/gather list for the entire buffer.
-   The transfer uses a system DMA controller that limits the number of buffer fragments that can be specified in a hardware scatter/gather list.

In all of these cases, **MapTransferEx** maps as much of the data buffer as it can in one call, and tells the driver how much of the buffer was mapped by the call. The preceding list does not include other conditions, such as platform-specific cache behavior, that might require more than one call to **MapTransferEx** to complete a transfer. Future hardware platforms might impose additional constraints on DMA transfer length. For these reasons, driver developers should design their drivers to correctly handle the case in which **MapTransferEx** cannot map an entire DMA data buffer in one call.

Before calling **MapTransferEx**, the caller sets the \**Length* parameter to the number of bytes in the DMA data buffer that still need to be mapped. Before returning, **MapTransferEx** sets \**Length* to the number of bytes in the buffer that were actually mapped by the call. When a **MapTransferEx** call cannot map the entire buffer length, as specified by the \**Length* input value, the output value of \**Length* is less than its input value. If a DMA transfer requires two or more **MapTransferEx** calls, the calling driver must obtain the \**Length* output value from one call before it can specify the \**Length* input value for the next call.

For example, if a **MapTransferEx** call can transfer only X bytes to or from a buffer for which *Offset* = B and \**Length* = N (on input), then, on return, \**Length* = X. For the next call to **MapTransferEx**, the driver should set *Offset* = B + X and \**Length* = N - X. In both calls, the same MDL chain is used without modification.

If the caller specifies a [*DmaCompletionRoutine*](https://msdn.microsoft.com/library/windows/hardware/hh450991), **MapTransferEx** writes the \**Length* output value before it schedules the *DmaCompletionRoutine* to run. This behavior ensures that the updated \**Length* value is always available before the *DmaCompletionRoutine* runs. For example, if a DMA transfer requires two **MapTransferEx** calls, the *DmaCompletionRoutine* that the first call schedules can obtain the \**Length* output value from the first call. The routine can then use this value to calculate the \**Length* input value for the second call. Typically, the *Length* parameter points to a location in the \**CompletionContext* value that is supplied to the *DmaCompletionRoutine* as a parameter.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20the%20MapTransferEx%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


