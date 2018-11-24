---
title: KSPROPERTY\_PIN\_PROPOSEDATAFORMAT
description: Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_PROPOSEDATAFORMAT


Clients use the KSPROPERTY\_PIN\_PROPOSEDATAFORMAT property to determine if pins instantiated by the pin factory support a specific data format.

## <span id="ddk_ksproperty_pin_proposedataformat_ks"></span><span id="DDK_KSPROPERTY_PIN_PROPOSEDATAFORMAT_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561656" data-raw-source="[&lt;strong&gt;KSDATAFORMAT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561656)"><strong>KSDATAFORMAT</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

[**KSPROPERTY\_TYPE\_GET**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier) is only supported in Windows 7 and later versions of Windows. This function allows the audio driver to provide information about the default data format on a pin. In Windows Vista **KSPROPERTY\_TYPE\_GET** is *not supported*.

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

## See also


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

[**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656)

 

 






