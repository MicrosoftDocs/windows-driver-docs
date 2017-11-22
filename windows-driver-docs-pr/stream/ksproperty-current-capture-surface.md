---
title: KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE
description: The KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE property gets or sets the type of capture memory used by a given pin.To use VRAM transport, a capture minidriver must support this property.
MS-HAID:
- 'ks-prop\_179fde8b-2bb4-405b-800d-5b1ebdc28741.xml'
- 'stream.ksproperty\_current\_capture\_surface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fcb07f74-d43a-4850-b8be-c349c92f9f9f
keywords: ["KSPROPERTY_CURRENT_CAPTURE_SURFACE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CURRENT_CAPTURE_SURFACE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE


The KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE property gets or sets the type of capture memory used by a given pin.

To use VRAM transport, a capture minidriver must support this property.

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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>CAPTURE_MEMORY_ALLOCATION_FLAGS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557647)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_CURRENT\_CAPTURE\_SURFACE returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error code.

Remarks
-------

Zero is an invalid value for [**CAPTURE\_MEMORY\_ALLOCATION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff557647).

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


[**CAPTURE\_MEMORY\_ALLOCATION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff557647)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CURRENT_CAPTURE_SURFACE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





