---
title: KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES
description: The KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES property specifies the list of data ranges currently supported by pins instantiated on the pin factory.
keywords: ["KSPROPERTY_PIN_CONSTRAINEDDATARANGES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_CONSTRAINEDDATARANGES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES


The KSPROPERTY\_PIN\_CONSTRAINEDDATARANGES property specifies the list of data ranges currently supported by pins instantiated on the pin factory.

## <span id="ddk_ksproperty_pin_constraineddataranges_ks"></span><span id="DDK_KSPROPERTY_PIN_CONSTRAINEDDATARANGES_KS"></span>


### Usage Summary Table

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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)"><strong>KSMULTIPLE_ITEM</strong></a> and <a href="/previous-versions/ff561658(v=vs.85)" data-raw-source="[&lt;strong&gt;KSDATARANGE&lt;/strong&gt;](/previous-versions/ff561658(v=vs.85))"><strong>KSDATARANGE</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **PinId** member of the [**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure specifies the pin factory for which to query.

This property returns a [**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure, followed by a sequence of 64-bit aligned [**KSDATARANGE**](/previous-versions/ff561658(v=vs.85)) structures.

A KS filter uses this property to report the data ranges currently supported by pins instantiated on this pin factory, based on any constraints imposed by the current internal state of the KS filter. Use the [**KSPROPERTY\_PIN\_DATARANGES**](ksproperty-pin-dataranges.md) property to report the complete list of all data ranges supported by the KS filter, regardless of dynamic constraints.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

For more information, see [KS Data Formats and Data Ranges](./ks-data-formats-and-data-ranges.md).

## Requirements

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

## See also


[**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)

[**KSDATARANGE**](/previous-versions/ff561658(v=vs.85))

[**KSPROPERTY\_PIN\_DATARANGES**](ksproperty-pin-dataranges.md)

