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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td align="left">[<strong>KSP_PIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566722)</td>
<td align="left">[<strong>KSAUDIO_MIC_ARRAY_GEOMETRY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff537087)</td>
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

For more information about how to process a microphone array in Windows, see the [Audio Technologies for Windows](http://go.microsoft.com/fwlink/p/?linkid=8751) page on the WHDC website and refer to the following resources:

[Microphone Array Support in Windows (white paper)](http://go.microsoft.com/fwlink/p/?linkid=120592)

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSPROPERTY_AUDIO_MIC_ARRAY_GEOMETRY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





