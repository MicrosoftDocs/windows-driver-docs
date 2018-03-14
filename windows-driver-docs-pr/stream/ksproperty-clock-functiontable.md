---
title: KSPROPERTY\_CLOCK\_FUNCTIONTABLE
description: Clients use the KSPROPERTY\_CLOCK\_FUNCTIONTABLE property to retrieve the entry points for querying time at DISPATCH\_LEVEL, which enables filters to perform precise rate matching.
ms.assetid: 6dac5688-fd69-416c-a4e4-da9ccc45c32a
keywords: ["KSPROPERTY_CLOCK_FUNCTIONTABLE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CLOCK_FUNCTIONTABLE
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CLOCK\_FUNCTIONTABLE


Clients use the KSPROPERTY\_CLOCK\_FUNCTIONTABLE property to retrieve the entry points for querying time at DISPATCH\_LEVEL, which enables filters to perform precise rate matching. This property fills in a [**KSCLOCK\_FUNCTIONTABLE**](https://msdn.microsoft.com/library/windows/hardware/ff561020) structure with function pointers that are valid until the file object for the clock is released.

## <span id="ddk_ksproperty_clock_functiontable_ks"></span><span id="DDK_KSPROPERTY_CLOCK_FUNCTIONTABLE_KS"></span>


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
<td><p>[<strong>KSCLOCK_FUNCTIONTABLE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561020)</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The *FileObject* parameter that the client supplies when it makes calls to these entry points specifies the file object underlying the file handle that was returned when the clock instance was created.

The *SystemTime* parameter points to the location to store the correlated system time. The system time is acquired using the function **KeQueryInterruptTime**.

Also see [KS Clocks](https://msdn.microsoft.com/library/windows/hardware/ff567307).

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


[**KSCLOCK\_FUNCTIONTABLE**](https://msdn.microsoft.com/library/windows/hardware/ff561020)

[**KeQueryInterruptTime**](https://msdn.microsoft.com/library/windows/hardware/ff553025)

 

 






