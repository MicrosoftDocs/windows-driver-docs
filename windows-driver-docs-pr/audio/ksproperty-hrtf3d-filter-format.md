---
title: KSPROPERTY\_HRTF3D\_FILTER\_FORMAT
description: The KSPROPERTY\_HRTF3D\_FILTER\_FORMAT property retrieves the filter format used by the HRTF algorithm.
keywords: ["KSPROPERTY_HRTF3D_FILTER_FORMAT Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_HRTF3D_FILTER_FORMAT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_HRTF3D\_FILTER\_FORMAT


The KSPROPERTY\_HRTF3D\_FILTER\_FORMAT property retrieves the filter format used by the HRTF algorithm.

## <span id="ddk_ksproperty_hrtf3d_filter_format_ks"></span><span id="DDK_KSPROPERTY_HRTF3D_FILTER_FORMAT_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksnodeproperty)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg" data-raw-source="[&lt;strong&gt;KSDS3D_HRTF_FILTER_FORMAT_MSG&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg)"><strong>KSDS3D_HRTF_FILTER_FORMAT_MSG</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a structure of type KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG that specifies the HRTF algorithm's filter method and coefficient format.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_HRTF3D\_FILTER\_FORMAT property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

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

[**KSDS3D\_HRTF\_FILTER\_FORMAT\_MSG**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksds3d_hrtf_filter_format_msg)

