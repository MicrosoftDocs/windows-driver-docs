---
title: KSPROPERTY\_DISPLAY\_ADAPTER\_GUID
description: The KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns the adapter GUID from the capture minidriver.To use VRAM transport, a capture minidriver must support this property.
ms.assetid: 419aa86e-f1c2-4fca-a9e4-87dcaaeaa2bb
keywords: ["KSPROPERTY_DISPLAY_ADAPTER_GUID Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DISPLAY_ADAPTER_GUID
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_DISPLAY\_ADAPTER\_GUID


The KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns the adapter GUID from the capture minidriver.

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
<td><p>GUID</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_DISPLAY\_ADAPTER\_GUID property returns STATUS\_SUCCESS to indicate that it has completed successfully. If the Property Type Value is incorrect, it returns STATUS\_INVALID\_PARAMETER.

Remarks
-------

The minidriver should return the adapter identifier of the first head on the GPU.

The capture GUID uniquely identifies a VRAM subsystem with which the capture device is compatible. The system-supplied kernel-streaming (KS) proxy module (KsProxy) uses this GUID to allocate surfaces on a compatible VRAM subsystem.

AVStream matches this GUID with the GUID of the downstream render pin to verify that both capture and render pins are on the same graphics adapter.

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


[**KSPROPERTY**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ks/ns-ks-ksidentifier)

 

 






