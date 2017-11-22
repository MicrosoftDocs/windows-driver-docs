---
title: KSPROPERTY\_DISPLAY\_ADAPTER\_GUID
description: The KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns the adapter GUID from the capture minidriver.To use VRAM transport, a capture minidriver must support this property.
MS-HAID:
- 'ks-prop\_6ed43eaa-e5e9-49a2-9f9b-0f65325c6302.xml'
- 'stream.ksproperty\_display\_adapter\_guid'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 419aa86e-f1c2-4fca-a9e4-87dcaaeaa2bb
keywords: ["KSPROPERTY_DISPLAY_ADAPTER_GUID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DISPLAY_ADAPTER_GUID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_DISPLAY\_ADAPTER\_GUID


The KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns the adapter GUID from the capture minidriver.

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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>GUID</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns STATUS\_SUCCESS to indicate that it has completed successfully. If the Property Type Value is incorrect, it returns STATUS\_INVALID\_PARAMETER.

Remarks
-------

The minidriver should return the adapter identifier of the first head on the GPU.

The capture GUID uniquely identifies a VRAM subsystem with which the capture device is compatible. The system-supplied kernel-streaming (KS) proxy module (KsProxy) uses this GUID to allocate surfaces on a compatible VRAM subsystem.

AVStream matches this GUID with the GUID of the downstream render pin to verify that both capture and render pins are on the same graphics adapter.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_DISPLAY_ADAPTER_GUID%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





