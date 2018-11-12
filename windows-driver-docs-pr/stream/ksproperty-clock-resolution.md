---
title: KSPROPERTY\_CLOCK\_RESOLUTION
description: Clients use the KSPROPERTY\_CLOCK\_RESOLUTION property to determine the precision of a clock.
ms.assetid: 3e92a4fb-207f-449a-bc70-aa8028b4f8f1
keywords: ["KSPROPERTY_CLOCK_RESOLUTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_RESOLUTION
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CLOCK\_RESOLUTION


Clients use the KSPROPERTY\_CLOCK\_RESOLUTION property to determine the precision of a clock.

## <span id="ddk_ksproperty_clock_resolution_ks"></span><span id="DDK_KSPROPERTY_CLOCK_RESOLUTION_KS"></span>


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
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566806" data-raw-source="[&lt;strong&gt;KSRESOLUTION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566806)"><strong>KSRESOLUTION</strong></a></p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The delay introduced in the **Error** member is in addition to that in the **Granularity** member. For example, a clock with a **Granularity** of one and **Error** of two would be able to issue clock event notifications every 300 nanoseconds.

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


[**KSCLOCK\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff561017)

[**KSRESOLUTION**](https://msdn.microsoft.com/library/windows/hardware/ff566806)

[**KSPROPERTY\_CLOCK\_PHYSICALTIME**](ksproperty-clock-physicaltime.md)

 

 






