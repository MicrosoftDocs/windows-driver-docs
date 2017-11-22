---
title: KSPROPERTY\_STREAM\_TIMEFORMAT
description: The KSPROPERTY\_STREAM\_TIMEFORMAT property is used to retrieve the time format used on a particular pin connection.
MS-HAID:
- 'ks-prop\_72f78821-9460-4f9b-8652-6d4fa4f74f37.xml'
- 'stream.ksproperty\_stream\_timeformat'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bf8c32b2-401f-4f89-bcca-97a07c50cc45
keywords: ["KSPROPERTY_STREAM_TIMEFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_STREAM_TIMEFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_STREAM\_TIMEFORMAT


The KSPROPERTY\_STREAM\_TIMEFORMAT property is used to retrieve the time format used on a particular pin connection.

## <span id="ddk_ksproperty_stream_timeformat_ks"></span><span id="DDK_KSPROPERTY_STREAM_TIMEFORMAT_KS"></span>


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
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>GUID</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The property returns a GUID specifying the time format used in the connection and indicating the format of the presentation time and extent. The defined time formats correspond to those defined by DirectShow.

KSPROPERTY\_STREAM\_TIMEFORMAT is an optional property that should be implemented if the pin supports the rate, presentation time/extent, or skip degradation properties (For more information about these properties, see [Quality Management](https://msdn.microsoft.com/library/windows/hardware/ff568124)). This allows a client to determine the time format used for connection and the format of the time stamp information used in rate, presentation time/extent, and skip degradation operations.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_STREAM_TIMEFORMAT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





