---
title: KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES
description: The KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES property specifies the list of data ranges currently supported by pins instantiated on the pin factory.
ms.assetid: 6328a128-c6f8-4de1-a86a-0a7c8a940e18
keywords: ["KSPROPERTY_PIN_CONSTRAINEDDATARANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_CONSTRAINEDDATARANGES
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES


The KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES property specifies the list of data ranges currently supported by pins instantiated on the pin factory.

## <span id="ddk_ksproperty_pin_constraineddataranges_ks"></span><span id="DDK_KSPROPERTY_PIN_CONSTRAINEDDATARANGES_KS"></span>


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
<td><p>[<strong>KSP_PIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566722)</p></td>
<td><p>[<strong>KSMULTIPLE_ITEM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563441) and [<strong>KSDATARANGE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561658)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **PinId** member of the [**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722) structure specifies the pin factory for which to query.

This property returns a [**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure, followed by a sequence of 64-bit aligned [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) structures.

A KS filter uses this property to report the data ranges currently supported by pins instantiated on this pin factory, based on any constraints imposed by the current internal state of the KS filter. Use the [**KSPROPERTY\_PIN\_DATARANGES**](ksproperty-pin-dataranges.md) property to report the complete list of all data ranges supported by the KS filter, regardless of dynamic constraints.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

For more information, see [KS Data Formats and Data Ranges](https://msdn.microsoft.com/library/windows/hardware/ff567632).

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


[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

[**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658)

[**KSPROPERTY\_PIN\_DATARANGES**](ksproperty-pin-dataranges.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_PIN_CONSTRAINEDDATARANGES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





