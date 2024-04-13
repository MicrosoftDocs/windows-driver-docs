---
title: KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL
description: The KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL property is used to get or set all the DirectSound 3D-buffer properties for the specified buffer.
keywords: ["KSPROPERTY_DIRECTSOUND3DBUFFER_ALL Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_DIRECTSOUND3DBUFFER_ALL
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL


The KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL property is used to get or set all the DirectSound 3D-buffer properties for the specified buffer.

## <span id="ddk_ksproperty_directsound3dbuffer_all_ks"></span><span id="DDK_KSPROPERTY_DIRECTSOUND3DBUFFER_ALL_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_buffer_all" data-raw-source="[&lt;strong&gt;KSDS3D_BUFFER_ALL&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_buffer_all)"><strong>KSDS3D_BUFFER_ALL</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSDS3D\_BUFFER\_ALL that specifies the 3D characteristics of the buffer.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DIRECTSOUND3DBUFFER\_ALL property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

The KSDS3D\_BUFFER\_ALL structure is similar to the DS3DBUFFER structure, which is described in the Microsoft Windows SDK documentation.

DirectSound uses this property to implement the **IDirectSound3DBuffer::GetAllParameters** and **IDirectSound3DBuffer::SetAllParameters** methods, which are described in the Windows SDK documentation.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSNODEPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)

[**KSDS3D\_BUFFER\_ALL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_buffer_all)

