---
title: KSPROPERTY\_CONNECTION\_PRIORITY
description: Clients use the KSPROPERTY\_CONNECTION\_PRIORITY property to get or set the priority of a connection.
ms.assetid: 2037fe95-e176-4714-ad36-65a0e25b29e0
keywords: ["KSPROPERTY_CONNECTION_PRIORITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CONNECTION_PRIORITY
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

# KSPROPERTY\_CONNECTION\_PRIORITY


Clients use the KSPROPERTY\_CONNECTION\_PRIORITY property to get or set the priority of a connection.

## <span id="ddk_ksproperty_connection_priority_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_PRIORITY_KS"></span>


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
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSPRIORITY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564250)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a structure of type [**KSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff564250) that contains a priority class and subclass.

One priority is greater than another if the **PriorityClass** member is greater, or if the **PriorityClass** members are identical and the **PrioritySubClass** member is greater.

The following predefined values of **PriorityClass** are available: KSPRIORITY\_LOW, KSPRIORITY\_NORMAL, KSPRIORITY\_HIGH, and KSPRIORITY\_EXCLUSIVE. Priority defaults to KSPRIORITY\_NORMAL. KSPRIORITY\_EXCLUSIVE indicates the connection has exclusive access to resources used by a pin.

The priority values have global significance: a client can use the reported values to set priorities between two different pins on two unrelated kernel streaming filters.

KSPROPERTY\_CONNECTION\_PRIORITY is optional. Clients treat pins that do not support it as having priority KSPRIORITY\_NORMAL.

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


[**KSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff564250)

[**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531)

 

 






