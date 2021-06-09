---
title: KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY
description: The KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property specifies the geometry of the microphone array.
keywords: ["KSPROPERTY_AUDIO_MIC_ARRAY_GEOMETRY Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIO_MIC_ARRAY_GEOMETRY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY


The KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property specifies the geometry of the microphone array.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Get</p></td>
<td align="left"><p>Set</p></td>
<td align="left"><p>Target</p></td>
<td align="left"><p>Property descriptor type</p></td>
<td align="left"><p>Property value type</p></td>
</tr>
<tr class="even">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></td>
<td align="left"><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry" data-raw-source="[&lt;strong&gt;KSAUDIO_MIC_ARRAY_GEOMETRY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry)"><strong>KSAUDIO_MIC_ARRAY_GEOMETRY</strong></a></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type KSAUDIO\_MIC\_ARRAY\_GEOMETRY. See the definition of the [**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry) structure for details.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property request returns a STATUS\_SUCCESS upon successful completion of the request.

If the pin indicated by the PinId member of the [**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure does not support a mic array request, the property request will return STATUS\_NOT\_SUPPORTED.

If the buffer size of the request is set to zero, the property request will return a STATUS\_BUFFER\_OVERFLOW status. Additionally, the request will use the return status block to indicate the size of the KSAUDIO\_MIC\_ARRAY\_GEOMETRY structure supported by the pin.

If the buffer size of the request is set to any buffer size that is too small to accommodate the returned structure, the request returns a status of STATUS\_BUFFER\_TOO\_SMALL. The request will then use the return status block to indicate the size of the [**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry) structure that is supported by the pin.

## Remarks

The KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property only supports KSPROPERTY\_TYPE\_GET requests. In order for the client to determine the correct size of buffer necessary to accommodate the entire geometry structure, it must first make the request with a zero buffer size. The client can then use the value returned in the status block to set the buffer size correctly and then make another property request with the correctly sized buffer.

For more information about how to process a microphone array in Windows, refer to the following resources:

[Microphone Array Geometry Property](./microphone-array-geometry-property.md)

[Microphone Array Support in Windows (white paper)](/previous-versions/windows/hardware/design/dn613960(v=vs.85))

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


[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksaudio_mic_array_geometry)

[**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

