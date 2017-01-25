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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_RING_BUFFER%20structure%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




