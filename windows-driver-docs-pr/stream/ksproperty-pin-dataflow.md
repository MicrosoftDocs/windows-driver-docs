---
title: KSPROPERTY\_PIN\_DATAFLOW
description: The KSPROPERTY\_PIN\_DATAFLOW property specifies the direction of data flow on pins instantiated by the pin factory. Sink pins are entry points into a filter; source pins output from a filter.
keywords: ["KSPROPERTY_PIN_DATAFLOW Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_DATAFLOW
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_DATAFLOW


The KSPROPERTY\_PIN\_DATAFLOW property specifies the direction of data flow on pins instantiated by the pin factory. Sink pins are entry points into a filter; source pins output from a filter.

## <span id="ddk_ksproperty_pin_dataflow_ks"></span><span id="DDK_KSPROPERTY_PIN_DATAFLOW_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow" data-raw-source="[&lt;strong&gt;KSPIN_DATAFLOW&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow)"><strong>KSPIN_DATAFLOW</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

Specify the pin factory in the **PinId** member of the [**KSP\_PIN**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_pin) structure.

KSPROPERTY\_PIN\_DATAFLOW returns an enumeration of type [**KSPIN\_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow), set to either **KSPIN\_DATAFLOW\_IN** or KSPIN\_DATAFLOW\_OUT.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

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

[**KSPIN\_DATAFLOW**](/windows-hardware/drivers/ddi/ks/ne-ks-kspin_dataflow)

