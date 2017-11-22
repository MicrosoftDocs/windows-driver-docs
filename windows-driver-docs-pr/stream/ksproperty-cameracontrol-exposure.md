---
title: KSPROPERTY\_CAMERACONTROL\_EXPOSURE
description: User-mode clients use the KSPROPERTY\_CAMERACONTROL\_EXPOSURE property to get or set a digital camera's exposure time. This property is optional.
MS-HAID:
- 'vidcapprop\_a1a94759-119b-40f1-846b-885ad4c0d6ac.xml'
- 'stream.ksproperty\_cameracontrol\_exposure'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e9ad7a82-0c2d-46e5-a5d5-9f33848f129c
keywords: ["KSPROPERTY_CAMERACONTROL_EXPOSURE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXPOSURE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXPOSURE


User-mode clients use the KSPROPERTY\_CAMERACONTROL\_EXPOSURE property to get or set a digital camera's exposure time. This property is optional.

## <span id="ddk_ksproperty_cameracontrol_exposure_ks"></span><span id="DDK_KSPROPERTY_CAMERACONTROL_EXPOSURE_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564439) or [<strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564420)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies the length of exposure.

This value is expressed in log base 2 seconds, thus, for values less than zero, the exposure time is 1/2n seconds. For positive values and zero, the exposure time is 2n seconds. For example:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Seconds</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>-7</p></td>
<td><p>1/128</p></td>
</tr>
<tr class="even">
<td><p>-6</p></td>
<td><p>1/64</p></td>
</tr>
<tr class="odd">
<td><p>-5</p></td>
<td><p>1/32</p></td>
</tr>
<tr class="even">
<td><p>-4</p></td>
<td><p>1/16</p></td>
</tr>
<tr class="odd">
<td><p>-3</p></td>
<td><p>1/8</p></td>
</tr>
<tr class="even">
<td><p>-2</p></td>
<td><p>1/4</p></td>
</tr>
<tr class="odd">
<td><p>-1</p></td>
<td><p>1/2</p></td>
</tr>
<tr class="even">
<td><p>0</p></td>
<td><p>1</p></td>
</tr>
<tr class="odd">
<td><p>1</p></td>
<td><p>2</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **Value** member of the KSPROPERTY\_CAMERACONTROL\_S structure specifies the length of exposure.

Every video capture minidriver that supports this property must define its own range and default value for this property.

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

[**KSPROPERTY\_CAMERACONTROL\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564439)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXPOSURE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





