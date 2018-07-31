---
title: KSPROPERTY\_CONNECTION\_DATAFORMAT
description: Clients use the KSPROPERTY\_CONNECTION\_DATAFORMAT property to set the current data format.
ms.assetid: c5f37f1b-7dc6-46d2-aba2-b6c03f07228d
keywords: ["KSPROPERTY_CONNECTION_DATAFORMAT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_DATAFORMAT
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_DATAFORMAT


Clients use the KSPROPERTY\_CONNECTION\_DATAFORMAT property to set the current data format.

## <span id="ddk_ksproperty_connection_dataformat_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_DATAFORMAT_KS"></span>


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
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSDATAFORMAT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561656)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property takes a [**KSDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff561656) structure specifying the requested data format.

KS filters only need to support this property if they allow clients to reset the current property, or if connections can be made with the data format incompletely specified.

For more information about the KSPROPERTY\_CONNECTION\_DATAFORMAT property, see [KS Data Formats and Data Ranges](https://msdn.microsoft.com/library/windows/hardware/ff567632) and [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

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


[**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138)

[**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](ksproperty-connection-proposedataformat.md)

[**KSPROPERTY\_PIN\_PROPOSEDATAFORMAT**](ksproperty-pin-proposedataformat.md)

 

 






