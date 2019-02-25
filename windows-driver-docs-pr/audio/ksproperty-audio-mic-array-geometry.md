---
title: KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY
description: The KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property specifies the geometry of the microphone array.
ms.assetid: c9153c65-06d1-4968-8d70-64aafc760a8c
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
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537087" data-raw-source="[&lt;strong&gt;KSAUDIO_MIC_ARRAY_GEOMETRY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537087)"><strong>KSAUDIO_MIC_ARRAY_GEOMETRY</strong></a></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type KSAUDIO\_MIC\_ARRAY\_GEOMETRY. See the definition of the [**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537087) structure for details.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property request returns a STATUS\_SUCCESS upon successful completion of the request.

If the pin indicated by the PinId member of the [**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722) structure does not support a mic array request, the property request will return STATUS\_NOT\_SUPPORTED.

If the buffer size of the request is set to zero, the property request will return a STATUS\_BUFFER\_OVERFLOW status. Additionally, the request will use the return status block to indicate the size of the KSAUDIO\_MIC\_ARRAY\_GEOMETRY structure supported by the pin.

If the buffer size of the request is set to any buffer size that is too small to accommodate the returned structure, the request returns a status of STATUS\_BUFFER\_TOO\_SMALL. The request will then use the return status block to indicate the size of the [**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537087) structure that is supported by the pin.

Remarks
-------

The KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY property only supports KSPROPERTY\_TYPE\_GET requests. In order for the client to determine the correct size of buffer necessary to accommodate the entire geometry structure, it must first make the request with a zero buffer size. The client can then use the value returned in the status block to set the buffer size correctly and then make another property request with the correctly sized buffer.

For more information about how to process a microphone array in Windows, refer to the following resources:

[Microphone Array Support in Windows (white paper)](https://go.microsoft.com/fwlink/p/?linkid=120592)

[Microphone Array Geometry Property](https://msdn.microsoft.com/library/windows/hardware/ff537516.aspx)

Requirements
------------

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


[**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537087)

[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

 

 






