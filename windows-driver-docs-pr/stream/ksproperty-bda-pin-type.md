---
title: KSPROPERTY\_BDA\_PIN\_TYPE
description: Clients use KSPROPERTY\_BDA\_PIN\_TYPE to retrieve the value that specifies the type of a pin.
MS-HAID:
- 'bdaref\_fb0061b5-732a-4b13-8f34-20a82bc001ef.xml'
- 'stream.ksproperty\_bda\_pin\_type'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3d2a976b-67ff-4469-aa96-7aa8bd5f229e
keywords: ["KSPROPERTY_BDA_PIN_TYPE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIN_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_BDA\_PIN\_TYPE


Clients use KSPROPERTY\_BDA\_PIN\_TYPE to retrieve the value that specifies the type of a pin.

## <span id="ddk_ksproperty_bda_pin_type_ks"></span><span id="DDK_KSPROPERTY_BDA_PIN_TYPE_KS"></span>


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
<td><p>KSPROPERTY</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The returned value specifies the pin type.

When the network provider creates a pin for a filter using KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY, it specifies a pin type from the list of pin types included in the filter's BDA template topology. KSPROPERTY\_BDA\_PIN\_TYPE returns this pin type. In the filter's BDA template topology each pin type can only occur once, but it can occur multiple times in an actual topology. The value for the pin type corresponds to the index of the element in the zero-based array of pin types. This array of pin types is an array of KSPIN\_DESCRIPTOR\_EX structures.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY**](ksmethod-bda-create-pin-factory.md)

[**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_BDA_PIN_TYPE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





