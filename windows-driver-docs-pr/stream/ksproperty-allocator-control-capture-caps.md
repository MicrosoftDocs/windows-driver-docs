---
title: KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS
description: The KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS property informs the Overlay Mixer of the capture capabilities of the video port (that is if capture support is available).
ms.assetid: 9e2947a3-ef5b-4a2a-a607-6c0c4be44b1c
keywords: ["KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS


The KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS property informs the Overlay Mixer of the capture capabilities of the video port (that is if capture support is available).

## <span id="ddk_ksproperty_allocator_control_capture_caps_ks"></span><span id="DDK_KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564269" data-raw-source="[&lt;strong&gt;KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564269)"><strong>KSPROPERTY_ALLOCATOR_CONTROL_CAPTURE_CAPS_S</strong></a></p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG the specifies whether interleaved capture is supported.

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

[**KSPROPERTY\_ALLOCATOR\_CONTROL\_CAPTURE\_CAPS\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564269)

 

 






