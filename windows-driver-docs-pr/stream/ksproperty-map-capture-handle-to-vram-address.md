---
title: KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS
description: The KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS property returns the capture driver's mapping of a VRAM surface handle to a VRAM physical address.To use VRAM transport, a capture minidriver must support this property.
MS-HAID:
- 'ks-prop\_d7abc26a-1e5b-4384-ac76-42a1058e2edd.xml'
- 'stream.ksproperty\_map\_capture\_handle\_to\_vram\_address'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 071c9152-12f9-4ec1-80d7-6b42fce51bbb
keywords: ["KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS


The KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS property returns the capture driver's mapping of a VRAM surface handle to a VRAM physical address.

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
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>VRAM_SURFACE_INFO_PROPERTY_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568785)</p></td>
<td><p>DWORD</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_MAP\_CAPTURE\_HANDLE\_TO\_VRAM\_ADDRESS returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error code.

Remarks
-------

The capture driver should perform the mapping in the handler for this property.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_MAP_CAPTURE_HANDLE_TO_VRAM_ADDRESS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





