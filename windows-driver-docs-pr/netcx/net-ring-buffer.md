---
title: NET_RING_BUFFER structure
description: Call NET\_RING\_BUFFER\_INIT to initialize this structure.
ms.assetid: 8a265659-599f-48e0-a1c3-add49ba9acdc
keywords: ["NET_RING_BUFFER structure Network Drivers Starting with Windows Vista", "PNET_RING_BUFFER structure pointer Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_RING_BUFFER
api_location:
- netringbuffer.h
api_type:
- HeaderDef
---

# NET\_RING\_BUFFER structure


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Call NET\_RING\_BUFFER\_INIT to initialize this structure.

Syntax
------

```ManagedCPlusPlus
typedef struct _NET_RING_BUFFER {
  UINT16                                              OSReserved1;
  UINT16                                              ElementStride;
  UINT32                                              NumberOfElements;
  UINT32                                              ElementIndexMask;
  UINT32                                              BeginIndex;
  UINT32                                              NextIndex;
  UINT32                                              EndIndex;
  VOID                                                *NetAdapterScratch[2];
  VOID                                                *OSReserved2[3];
  _Field_size_(NumberOfElements * ElementStride) BYTE Buffer;
} NET_RING_BUFFER, *PNET_RING_BUFFER;
```

Members
-------

**OSReserved1**  

**ElementStride**  

**NumberOfElements**  

**ElementIndexMask**  

**BeginIndex**  

**NextIndex**  

**EndIndex**  

**NetAdapterScratch**  

**OSReserved2**  

**Buffer**  

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netringbuffer.h</td>
</tr>
</tbody>
</table>

 

 





