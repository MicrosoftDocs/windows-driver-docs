---
title: KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR
description: The audio driver for the offload-capable hardware solution uses KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR to provide information about the node that represents the hardware audio engine.
ms.assetid: 1D912155-6DB2-4AFF-949F-47C19E47678C
keywords: ["KSPROPERTY_AUDIOENGINE_DESCRIPTOR Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AUDIOENGINE_DESCRIPTOR
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR


The audio driver for the offload-capable hardware solution uses **KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR** to provide information about the node that represents the hardware audio engine.

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Yes</p></td>
<td align="left"><p>No</p></td>
<td align="left"><p>Node via filter</p></td>
<td align="left"><p>KSP_NODE</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/hh450862" data-raw-source="[&lt;strong&gt;KSAUDIOENGINE_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/hh450862)"><strong>KSAUDIOENGINE_DESCRIPTOR</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value is of type **KSAUDIOENGINE\_DESCRIPTOR** and it indicates the static properties of the audio engine node.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The **KSPROPERTY\_AUDIOENGINE\_DESCRIPTOR** property request returns **STATUS\_SUCCESS** to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Windows 8</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSAUDIOENGINE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/hh450862)

[**KSPROPERTY\_AUDIOENGINE**](ksproperty-audioengine.md)

 

 






