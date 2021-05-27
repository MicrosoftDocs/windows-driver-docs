---
title: KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID
description: The KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID property is used to inform a GFX filter of the Plug and Play device ID of the audio device that renders the final audio mix.
keywords: ["KSPROPERTY_AUDIOGFX_RENDERTARGETDEVICEID Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOGFX_RENDERTARGETDEVICEID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID


The KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID property is used to inform a GFX filter of the Plug and Play device ID of the audio device that renders the final audio mix.

## <span id="ddk_ksproperty_audiogfx_rendertargetdeviceid_ks"></span><span id="DDK_KSPROPERTY_AUDIOGFX_RENDERTARGETDEVICEID_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/previous-versions/ff564262(v=vs.85)" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/previous-versions/ff564262(v=vs.85))"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>WCHAR array</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a WCHAR array that contains the device ID. The device ID is a null-terminated string of Unicode characters.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIOGFX\_RENDERTARGETDEVICEID property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Remarks

The target for this set-only property request is a GFX filter that is configured for use as either a render- or render/capture-GFX filter.

To determine the size of the buffer needed to hold the property value, see [Basic Support Queries for Audio Properties](./basic-support-queries-for-audio-properties.md).

For additional information about device IDs, see [Device Identification Strings](../install/device-identification-strings.md).

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


[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

