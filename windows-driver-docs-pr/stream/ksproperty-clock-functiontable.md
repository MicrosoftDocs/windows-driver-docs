---
title: KSPROPERTY\_CLOCK\_FUNCTIONTABLE
description: Clients use the KSPROPERTY\_CLOCK\_FUNCTIONTABLE property to retrieve the entry points for querying time at DISPATCH\_LEVEL, which enables filters to perform precise rate matching.
keywords: ["KSPROPERTY_CLOCK_FUNCTIONTABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_FUNCTIONTABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CLOCK\_FUNCTIONTABLE


Clients use the KSPROPERTY\_CLOCK\_FUNCTIONTABLE property to retrieve the entry points for querying time at DISPATCH\_LEVEL, which enables filters to perform precise rate matching. This property fills in a [**KSCLOCK\_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable) structure with function pointers that are valid until the file object for the clock is released.

## <span id="ddk_ksproperty_clock_functiontable_ks"></span><span id="DDK_KSPROPERTY_CLOCK_FUNCTIONTABLE_KS"></span>


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
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable" data-raw-source="[&lt;strong&gt;KSCLOCK_FUNCTIONTABLE&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable)"><strong>KSCLOCK_FUNCTIONTABLE</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

The *FileObject* parameter that the client supplies when it makes calls to these entry points specifies the file object underlying the file handle that was returned when the clock instance was created.

The *SystemTime* parameter points to the location to store the correlated system time. The system time is acquired using the function **KeQueryInterruptTime**.

Also see [KS Clocks](./ks-clocks.md).

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


[**KSCLOCK\_FUNCTIONTABLE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksclock_functiontable)

[**KeQueryInterruptTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequeryinterrupttime)

