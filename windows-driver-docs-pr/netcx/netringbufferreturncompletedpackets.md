---
title: NetRingBufferReturnCompletedPackets method
topic_type:
- apiref
api_name:
- NetRingBufferReturnCompletedPackets
api_location:
- netadapterpacket.h
api_type:
- HeaderDef
---

# NetRingBufferReturnCompletedPackets method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Calls [**NetRingBufferReturnCompletedPacketsThroughIndex**](netringbufferreturncompletedpacketsthroughindex.md) with the NextIndex value of the specified ring buffer.

Syntax
------

```ManagedCPlusPlus
__inline
void NetRingBufferReturnCompletedPackets(
  _In_ NET_RING_BUFFER *RingBuffer
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

Return value
------------

This method does not return a value.

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
<td align="left">Netadapterpacket.h (include Netadaptercx.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





