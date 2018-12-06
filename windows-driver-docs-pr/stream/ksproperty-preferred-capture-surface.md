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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE


The KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE property returns the capture driver's preferred memory target for capture, either VRAM or a type of system memory.

To use VRAM transport, a capture minidriver must support this property.

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
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p><a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)"><strong>KSPROPERTY</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff557647" data-raw-source="[&lt;strong&gt;CAPTURE_MEMORY_ALLOCATION_FLAGS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff557647)"><strong>CAPTURE_MEMORY_ALLOCATION_FLAGS</strong></a></p></td>
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

## See also


[**CAPTURE\_MEMORY\_ALLOCATION\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff557647)

[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






