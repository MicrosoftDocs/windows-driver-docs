---
title: KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE
description: The KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE property returns the capture driver's preferred memory target for capture, either VRAM or a type of system memory.To use VRAM transport, a capture minidriver must support this property.
ms.assetid: ed41c456-279d-4728-a85b-f651361ef8e9
keywords: ["KSPROPERTY_PREFERRED_CAPTURE_SURFACE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PREFERRED_CAPTURE_SURFACE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE


The KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE property returns the capture driver's preferred memory target for capture, either VRAM or a type of system memory.

To use VRAM transport, a capture minidriver must support this property.

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
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>CAPTURE_MEMORY_ALLOCATION_FLAGS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557647)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error code.

Remarks
-------

Zero is an invalid value for [**CAPTURE\_MEMORY\_ALLOCATION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff557647).

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
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**CAPTURE\_MEMORY\_ALLOCATION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff557647)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






