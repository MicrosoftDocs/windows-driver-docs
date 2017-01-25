---
title: NetRingBufferGetNumberOfElementsInRange method
description: Calculates the number of elements contained in a range of the specified net ring buffer.
ms.assetid: 0cf45968-4204-4891-82cd-e1fd0e02d62d
keywords: ["NetRingBufferGetNumberOfElementsInRange method Network Drivers Starting with Windows Vista"]
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

```ManagedCPlusPlus
__inline
UINT32 NetRingBufferGetNumberOfElementsInRange(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          StartIndex,
  _In_ UINT32          EndIndex
);
```

Parameters
----------

*RingBuffer* \[in\]  
The [**NET\_RING\_BUFFER**](net-ring-buffer.md) to access

*StartIndex* \[in\]  
The inclusive start of the range to measure

*EndIndex* \[in\]  
The exclusive end of the range to measure

Return value
------------

The number of elements in the given range

Remarks
-------

For example, consider a net ring buffer containing a total of 8 elements. Index values for the elements are zero through 7. The number of elements in the range \[1, 4\] is 3. This is because the EndIndex value is not included, so the range includes elements at index values 1, 2, and 3.

Similarly, the range \[4, 1\] includes elements at index values 4, 5, 6, 7, and 0 (looping back to the beginning of the ring), for a total of 5.

Finally, the range \[7, 7\] returns zero elements.

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetRingBufferGetNumberOfElementsInRange%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




