---
title: NetRingBufferGetNumberOfElementsInRange method
topic_type:
- apiref
api_name:
- NetRingBufferGetNumberOfElementsInRange
api_location:
- netringbuffer.h
api_type:
- HeaderDef
---

# NetRingBufferGetNumberOfElementsInRange method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Calculates the number of elements contained in a range of the specified net ring buffer.

Syntax
------

```cpp
__inline
UINT32 NetRingBufferGetNumberOfElementsInRange(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          StartIndex,
  _In_ UINT32          EndIndex
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

*StartIndex* [in]  
The inclusive start of the range to measure.

*EndIndex* [in]  
The exclusive end of the range to measure.

Return value
------------

The number of elements in the given range.

Remarks
-------

For example, consider a net ring buffer containing a total of 8 elements. Index values for the elements are zero through 7. The number of elements in the range [1, 4) is 3. This is because the EndIndex value is not included, so the range includes elements at index values 1, 2, and 3.

Similarly, the range [4, 1) includes elements at index values 4, 5, 6, 7, and 0 (looping back to the beginning of the ring), for a total of 5 elements.

Finally, note that an empty range like [2, 2) returns zero elements.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Universal</td>
</tr>
<tr class="even">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Netringbuffer.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;=DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





