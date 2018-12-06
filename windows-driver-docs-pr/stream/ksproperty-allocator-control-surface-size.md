---
title: KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE
description: The KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE property informs client filters that provide DirectDraw surface allocators (such as the Overlay Mixer) that a capture operation is in progress and that Microsoft DirectDraw surfaces must be allocated at a fixed size regardless of the present size of the overlay. This property is optional.
ms.assetid: fc759013-9dd7-44fc-a0d7-fd2585975966
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE


The KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE property informs client filters that provide DirectDraw surface allocators (such as the Overlay Mixer) that a capture operation is in progress and that Microsoft DirectDraw surfaces must be allocated at a fixed size regardless of the present size of the overlay. This property is optional.

## <span id="ddk_ksproperty_allocator_control_surface_size_ks"></span><span id="DDK_KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_KS"></span>


### Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564280" data-raw-source="[&lt;strong&gt;KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564280)"><strong>KSPROPERTY_ALLOCATOR_CONTROL_SURFACE_SIZE_S</strong></a></p></td>
<td><p>Pair of ULONGs</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a pair of ULONGs that specify the width and height of overlay surfaces.

Remarks
-------

Minidrivers that support this property return a KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE\_S structure that describes the width and height of the required overlay surface. The Overlay Mixer allocates overlay surfaces of this size. If this is not the size specified in the MediaType during pin connection, then the video is scaled at the video port to this size. No other scaling at the video port occurs regardless of the scaling abilities of the VGA chip.

The Overlay Mixer always queries this new property if the mixer is connected to this property's upstream filter through a video port on its primary input pin. If that filter does not implement this property, the Overlay Mixer assumes that it is not capturing data and scales the video at the video port as necessary to keep the video displayed correctly.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_SURFACE\_SIZE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564280)

 

 






