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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CONNECTION\_PRIORITY


Clients use the KSPROPERTY\_CONNECTION\_PRIORITY property to get or set the priority of a connection.

## <span id="ddk_ksproperty_connection_priority_ks"></span><span id="DDK_KSPROPERTY_CONNECTION_PRIORITY_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564250" data-raw-source="[&lt;strong&gt;KSPRIORITY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564250)"><strong>KSPRIORITY</strong></a></p></td>
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

## See also


[**KSPRIORITY**](https://msdn.microsoft.com/library/windows/hardware/ff564250)

[**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531)

 

 






