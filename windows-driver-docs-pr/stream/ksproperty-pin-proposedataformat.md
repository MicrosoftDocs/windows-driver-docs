---
title: KSPROPERTY\_PIN\_PROPOSEDATAFORMAT
description: Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.
MS-HAID:
- 'ks-prop\_74676c08-da12-45c7-8ae5-a304f92853fd.xml'
- 'stream.ksproperty\_pin\_proposedataformat'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f1657fd1-0988-48b8-95d0-c6026965848b
keywords: ["KSPROPERTY_PIN_PROPOSEDATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_PROPOSEDATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
---

# KSPROPERTY\_PIN\_PROPOSEDATAFORMAT


Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.

## <span id="ddk_ksproperty_pin_proposedataformat_ks"></span><span id="DDK_KSPROPERTY_PIN_PROPOSEDATAFORMAT_KS"></span>


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
<td><p>Filter</p></td>
<td><p>[<strong>KSP_PIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566722)</p></td>
<td><p>[<strong>KSDATAFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561656)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

[**KSPROPERTY\_TYPE\_GET**](https://msdn.microsoft.com/library/windows/hardware/ff564262) is only supported in Windows 7 and later versions of Windows. This function allows the audio driver to provide information about the default data format on a pin. In Windows Vista **KSPROPERTY\_TYPE\_GET** is *not supported*.

Specify this property using KSP\_PIN, where the member specifies the relevant pin factory.

KSPROPERTY\_PIN\_PROPOSEDATAFORMAT includes a structure of type [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656), specifying the proposed data format.

The KS filter returns STATUS\_SUCCESS if pins can be reset to the proposed data format, or an error code otherwise.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

This property does not actually change the data format. Clients use [**KSPROPERTY\_CONNECTION\_DATAFORMAT**](ksproperty-connection-dataformat.md) to change the data format.

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


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

[**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_PIN_PROPOSEDATAFORMAT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





