---
title: KSPROPERTY\_VIDEOCOMPRESSION\_WINDOWSIZE
description: The KSPROPERTY\_VIDEOCOMPRESSION\_WINDOWSIZE property controls the data rate that describes the average frame size. This property must be implemented.
MS-HAID:
- 'vidcapprop\_c9f0b78a-f9d6-4f7d-bf8a-40597c5293a5.xml'
- 'stream.ksproperty\_videocompression\_windowsize'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 44cf4bb6-7ddb-4a72-8a77-7dc390aa8c12
keywords: ["KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_VIDEOCOMPRESSION\_WINDOWSIZE


The KSPROPERTY\_VIDEOCOMPRESSION\_WINDOWSIZE property controls the data rate that describes the average frame size. This property must be implemented.

## <span id="ddk_ksproperty_videocompression_windowsize_ks"></span><span id="DDK_KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE_KS"></span>


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
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY_VIDEOCOMPRESSION_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566018)</p></td>
<td><p>LONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a LONG that specifies a data rate that represents the average frame size.

Remarks
-------

The **Value** member of the KSPROPERTY\_VIDEOCOMPRESSION\_S structure specifies the window size.

Minidrivers that support this property should set the **KS\_CompressionCaps\_CanWindow** flag in the **Capabilities** member of the [**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565979) structure that retrieves the minidriver's video compression capabilities. If a minidriver sets the **KS\_CompressionCaps\_CanWindow** flag, it should provide both get and set support for the property.

For a window of size *n,* the average frame size of any consecutive *n* frames must not exceed the stream's specified data rate, although *individual* frames may be larger or smaller. For example, if the data rate has been set to 150 kilobytes per second (KBps) on a 15 frame per second (fps) movie, the *average* size of each frame must therefore be less than or equal to 10 kilobytes. Individual frames may be larger or smaller just so long as the average size (calculated across 15 frames per second of movie) is less than or equal to 10 kilobytes.

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

[**KSPROPERTY\_VIDEOCOMPRESSION\_S**](https://msdn.microsoft.com/library/windows/hardware/ff566018)

[**KSPROPERTY\_VIDEOCOMPRESSION\_GETINFO\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565979)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_VIDEOCOMPRESSION_WINDOWSIZE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





