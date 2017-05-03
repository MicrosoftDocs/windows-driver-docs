---
title: NetRingBufferIncrementIndex method
topic_type:
- apiref
api_name:
- NetRingBufferIncrementIndex
api_location:
- netringbuffer.h
api_type:
- HeaderDef
---

# NetRingBufferIncrementIndex method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Returns the next index value after the specified index value, wrapping around to the beginning of the ring buffer if necessary.

Syntax
------

```cpp
UINT32 NetRingBufferIncrementIndex(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          Index
);
```

Parameters
----------

*RingBuffer* [in]  
A pointer to a [**NET_RING_BUFFER**](net-ring-buffer.md).

*Index* [in]  
An index value to increment.

Return value
------------

Returns the next index value after the specified index value, wrapping around to the beginning of the ring buffer if necessary.

Remarks
-------

This routine is equivalent to `Index++`, except it accounts for the wraparound of a ring buffer.

For example, you can use this routine to return a packet to the operating system by incrementing **BeginIndex**:

```cpp
NET_RING_BUFFER *ringBuffer = . . .;
ringBuffer->BeginIndex = NetRingBufferIncrementIndex(ringBuffer, ringBuffer->BeginIndex);
```

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

 

 





