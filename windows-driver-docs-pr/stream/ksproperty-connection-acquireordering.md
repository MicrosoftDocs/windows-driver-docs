---
title: KSPROPERTY\_CONNECTION\_ACQUIREORDERING
description: The KSPROPERTY\_CONNECTION\_ACQUIREORDERING property is an optional property that should be implemented on a pin when state change order is significant.
ms.assetid: b0d27615-bece-49b1-8497-f3c389ea37fc
keywords: ["KSPROPERTY_CONNECTION_ACQUIREORDERING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_ACQUIREORDERING
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

# KSPROPERTY\_CONNECTION\_ACQUIREORDERING


The KSPROPERTY\_CONNECTION\_ACQUIREORDERING property is an optional property that should be implemented on a pin when state change order is significant. For example, the property should be implemented on communication sink pins if the sink requires pins connected to its communication source pins to be set to an Acquire state before the sink pins are set.

## <span id="ddk_ksproperty_connection_acquireordering_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_ACQUIREORDERING_KS"></span>


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
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns **TRUE** if state change ordering is significant. If **FALSE** is to be returned, the property need not be implemented.

This read-only property is used to determine whether the Stop-to-Acquire state change is significant for this communication sink pin. If the property is not implemented, the assumption is that ordering is not significant. For IRP-based data flow, this would be implemented by a pin when it forwards streaming IRPs rather than creating new IRPs for requests, and thus needs to indicate correct stack depth to the connected source pin. If the pin did not forward IRPs, then recalculation of stack depth would not be important, as the stack depth for the filter would be static.

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


[KSPROPSETID\_Connection](kspropsetid-connection.md)

 

 






