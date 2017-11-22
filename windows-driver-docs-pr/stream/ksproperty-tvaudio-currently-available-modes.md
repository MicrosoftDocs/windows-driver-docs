---
title: KSPROPERTY\_TVAUDIO\_CURRENTLY\_AVAILABLE\_MODES
description: The KSPROPERTY\_TVAUDIO\_CURRENTLY\_AVAILABLE\_MODES property retrieves TV audio modes that are available for the device. This property must be implemented.
MS-HAID:
- 'vidcapprop\_b7c3e8ee-d2b9-47a2-ac1c-5100be43ccf4.xml'
- 'stream.ksproperty\_tvaudio\_currently\_available\_modes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9c98771a-7a41-469d-a441-da5c1ac5a697
keywords: ["KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_TVAUDIO\_CURRENTLY\_AVAILABLE\_MODES


The KSPROPERTY\_TVAUDIO\_CURRENTLY\_AVAILABLE\_MODES property retrieves TV audio modes that are available for the device. This property must be implemented.

## <span id="ddk_ksproperty_tvaudio_currently_available_modes_ks"></span><span id="DDK_KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES_KS"></span>


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
<td><p>[<strong>KSPROPERTY_TVAUDIO_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565953)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies the currently available TV audio modes, such as stereo or mono audio and multiple language settings.

Remarks
-------

The **Mode** member of the KSPROPERTY\_TVAUDIO\_S structure specifies the audio mode. It contains a bitwise ORing of the KS\_TVAUDIO\_MODE\_\* flags indicating the modes supported by the device at the time the information was requested.

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

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KSPROPERTY\_TVAUDIO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565953)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_TVAUDIO_CURRENTLY_AVAILABLE_MODES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





