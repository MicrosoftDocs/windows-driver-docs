---
title: KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT
description: The KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT property specifies the upper limit for the amount of digital zoom that can be applied to the image.
MS-HAID:
- 'vidcapprop\_2b0cb709-3323-46c4-8f74-3be23fb6df1c.xml'
- 'stream.ksproperty\_videoprocamp\_digital\_multiplier\_limit'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 66cc1dd5-3e07-47d8-bb30-b64b90b07ad9
keywords: ["KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT


The KSPROPERTY\_VIDEOPROCAMP\_DIGITAL\_MULTIPLIER\_LIMIT property specifies the upper limit for the amount of digital zoom that can be applied to the image.

## <span id="ddk_ksproperty_videoprocamp_digital_multiplier_limit_ks"></span><span id="DDK_KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT_KS"></span>


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
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOPROCAMP_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566089) or [<strong>KSPROPERTY_VIDEOPROCAMP_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566080)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a camera's upper digital multiplier limit. The value specifies the maximum value of the digital multiplier that the device can apply to the optical image.

Remarks
-------

When making a set request, the client should supply a digital multiplier value in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

A client might use a set request to establish a user-defined upper limit for digital zoom.

When making a get request, the client receives one of the preceding values in the **Value** member of the KSPROPERTY\_VIDEOPROCAMP\_NODE\_S structure.

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

[**KSPROPERTY\_VIDEOPROCAMP\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566089)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_VIDEOPROCAMP_DIGITAL_MULTIPLIER_LIMIT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





