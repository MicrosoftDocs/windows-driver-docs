---
title: NetRingBufferReturnCompletedPacketsThroughIndex method
description: Sets the BeginIndex value of the specified ring buffer to the first packet that is not completed.
ms.assetid: 5c6899e2-5d68-404c-b45e-bf052205ec2a
keywords: ["NetRingBufferReturnCompletedPacketsThroughIndex method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRingBufferReturnCompletedPacketsThroughIndex
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferReturnCompletedPacketsThroughIndex method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Sets the BeginIndex value of the specified ring buffer to the first packet that is not completed.

Syntax
------

```ManagedCPlusPlus
__inline
void NetRingBufferReturnCompletedPacketsThroughIndex(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          EndIndex
);
```

Parameters
----------

*RingBuffer* \[in\]  

*EndIndex* \[in\]  

Return value
------------

This method does not return a value.

Remarks
-------

Typically, when it marks a packet as completed, the client driver sets the **Completed** flag in the starting fragment of the packet. Then, in its [*EVT\_RXQUEUE\_ADVANCE*](evt-rxqueue-advance.md) or [*EVT\_TXQUEUE\_ADVANCE*](evt-txqueue-advance.md) callback, the client calls **NetRingBufferReturnCompletedPacketsThroughIndex** to transfer ownership of completed packets in the ring buffer back to NetAdapterCx.

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
<td align="left">Netadapterpacket.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NetRingBufferReturnCompletedPacketsThroughIndex%20method%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




