---
title: NetRingBufferGetElementAtIndex method
description: Returns the element at the specified index in the ring buffer.
ms.assetid: 5b4d5e14-3e1f-425f-96e4-cc2a9d720b41
keywords: ["NetRingBufferGetElementAtIndex method Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NetRingBufferGetElementAtIndex
api_location:
- netringbuffer.h
api_type:
- HeaderDef
---

# NetRingBufferGetElementAtIndex method


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Returns the element at the specified index in the ring buffer.

Syntax
------

```ManagedCPlusPlus
__inline
VOID* NetRingBufferGetElementAtIndex(
  _In_ NET_RING_BUFFER *RingBuffer,
  _In_ UINT32          Index
);
```

Parameters
----------

*RingBuffer* \[in\]  
The [**NET\_RING\_BUFFER**](net-ring-buffer.md) to access

*Index* \[in\]  
The element index. Must be in the range \[0, RingBuffer-&gt;NumberOfElements).

Return value
------------

The specified element

Remarks
-------

NetRingBufferGetElementAtIndex uses the ElementStride member of the ring buffer to index into the buffer and returns the location of the specified element.

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
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

 

 





