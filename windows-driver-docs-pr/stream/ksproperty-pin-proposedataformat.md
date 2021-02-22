---
title: KSPROPERTY\_PIN\_PROPOSEDATAFORMAT
description: Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.
keywords: ["KSPROPERTY_PIN_PROPOSEDATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_PROPOSEDATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 12/28/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_PROPOSEDATAFORMAT

Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.

## Usage Summary Table

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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)"><strong>KSP_PIN</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat" data-raw-source="[&lt;strong&gt;KSDATAFORMAT&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)"><strong>KSDATAFORMAT</strong></a></p></td>
</tr>
</tbody>
</table>

## Remarks

KSPROPERTY_PIN_PROPOSEDATAFORMAT includes a structure of type KSDATAFORMAT, specifying the proposed data format. Specify this property using KSP_PIN, where the member specifies the relevant pin factory.

KSPROPERTY\_PIN\_PROPOSEDATAFORMAT includes a structure of type [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat), specifying the proposed data format.

[**KSPROPERTY\_TYPE\_GET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier) is supported in Windows 7 and later versions of Windows. In Windows Vista **KSPROPERTY\_TYPE\_GET** is *not supported*.

**KSPROPERTY_TYPE_GET** with this property allows the audio driver to provide information about the default data format on a pin. **KSPROPERTY_TYPE_GET** 
is optional to implement for this property unless the driver supports [**KSEVENT_PINCAPS_FORMATCHANGE**](../audio/ksevent-pincaps-formatchange.md).

The KS filter returns STATUS\_SUCCESS when using this property with KSPROPERTY_TYPE_SET if pins can be set to or opened with the proposed data format. If the pin cannot be set to the proposed data format, then it returns STATUS_NO_MATCH. For any other failures, an appropriate error is returned. If the driver supports [**KSPROPERTY_AUDIOSIGNALPROCESSING_MODES**](../audio/ksproperty-audiosignalprocessing-modes.md), this property should return STATUS_SUCCESS if the format is supported by any of the Audio signal processing modes.

Using KSPROPERTY_TYPE_SET with this property does not actually change the data format. Clients use [**KSPROPERTY\_CONNECTION\_DATAFORMAT**](ksproperty-connection-dataformat.md) to change the data format. **KSPROPERTY_TYPE_SET** is optional to implement for this property.

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

[**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin)

[**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)

[**KSEVENT_PINCAPS_FORMATCHANGE**](../audio/ksevent-pincaps-formatchange.md)

[**KS Properties**](./ks-properties.md)

[**KSPROPERTY\_TYPE\_GET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)

[**KSPROPERTY_AUDIOSIGNALPROCESSING_MODES**](../audio/ksproperty-audiosignalprocessing-modes.md)
