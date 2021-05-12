---
title: KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT
description: Clients can use the KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT property to propose a new data format for the connection.
keywords: ["KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT


Clients can use the KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT property to propose a new data format for the connection.

## <span id="ddk_ksproperty_connection_proposedataformat_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_PROPOSEDATAFORMAT_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat" data-raw-source="[&lt;strong&gt;KSDATAFORMAT&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)"><strong>KSDATAFORMAT</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

This property returns a [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) specifying the proposed data format.

The KS filter returns STATUS\_SUCCESS if the pin can be reset to the proposed data format, or an error code otherwise. Note that this property request does not change the data format. Clients use [**KSPROPERTY\_CONNECTION\_DATAFORMAT**](ksproperty-connection-dataformat.md) to change the format.

Also see [KS Data Formats and Data Ranges](./ks-data-formats-and-data-ranges.md).

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


[**KSPROPERTY\_CONNECTION\_DATAFORMAT**](ksproperty-connection-dataformat.md)

[*AVStrMiniPinSetDataFormat*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspinsetdataformat)

