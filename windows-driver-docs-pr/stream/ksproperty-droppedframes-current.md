---
title: KSPROPERTY\_DROPPEDFRAMES\_CURRENT
description: The KSPROPERTY\_DROPPED\_FRAMES\_CURRENT property dynamically retrieves the video capture minidriver for the number of frames captured, the number of frames dropped, and the average frame size. This property must be implemented.
ms.assetid: 43367858-4e3b-476e-aaa5-c9e665df8dc6
keywords: ["KSPROPERTY_DROPPEDFRAMES_CURRENT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DROPPEDFRAMES_CURRENT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DROPPEDFRAMES\_CURRENT


The KSPROPERTY\_DROPPED\_FRAMES\_CURRENT property dynamically retrieves the video capture minidriver for the number of frames captured, the number of frames dropped, and the average frame size. This property must be implemented.

## <span id="ddk_ksproperty_droppedframes_current_ks"></span><span id="DDK_KSPROPERTY_DROPPEDFRAMES_CURRENT_KS"></span>


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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565138" data-raw-source="[&lt;strong&gt;KSPROPERTY_DROPPEDFRAMES_CURRENT_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565138)"><strong>KSPROPERTY_DROPPEDFRAMES_CURRENT_S</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff565138" data-raw-source="[&lt;strong&gt;KSPROPERTY_DROPPEDFRAMES_CURRENT_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff565138)"><strong>KSPROPERTY_DROPPEDFRAMES_CURRENT_S</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S structure that specifies the current picture number, the count of dropped frames, and the average size of the frames captured.

Remarks
-------

The counts of frames captured and frames dropped should reset when the stream state transitions from stop to pause.

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

[**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565138)

 

 






