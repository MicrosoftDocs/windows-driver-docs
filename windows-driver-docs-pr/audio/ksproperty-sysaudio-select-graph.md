---
title: KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH
description: The KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property is used to explicitly include an optional node in the graph that SysAudio builds for a pin instance on a virtual audio device.
ms.assetid: 1107e20e-9ba8-4fda-8457-c357426a9cda
keywords: ["KSPROPERTY_SYSAUDIO_SELECT_GRAPH Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SYSAUDIO_SELECT_GRAPH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH


The KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property is used to explicitly include an optional node in the graph that SysAudio builds for a pin instance on a virtual audio device.

## <span id="ddk_ksproperty_sysaudio_select_graph_ks"></span><span id="DDK_KSPROPERTY_SYSAUDIO_SELECT_GRAPH_KS"></span>


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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff538500" data-raw-source="[&lt;strong&gt;SYSAUDIO_SELECT_GRAPH&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538500)"><strong>SYSAUDIO_SELECT_GRAPH</strong></a></p></td>
<td align="left"><p>None</p></td>
</tr>
</tbody>
</table>

 

The property descriptor (instance data) is a structure of type SYSAUDIO\_SELECT\_GRAPH that specifies the property, pin ID, and node ID. The property is specified by an embedded structure of type [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262). The pin ID is an index identifying a pin factory in the KS filter that wraps the virtual audio device. The node ID is an index identifying an optional node in the specified pin's data path. For more information, see the following Remarks section.

No property value (operation data) is defined for this property. Specify the property value's buffer pointer as **NULL** and its size as zero.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

This property is typically used to force an AEC node into the graph for a pin instance.

When instantiating a rendering pin on the filter for a virtual audio device, SysAudio starts at the pin and by default selects the graph that represents the simplest path through the filter. This graph excludes any optional nodes such as AEC controls.

You can override SysAudio's default behavior by first sending SysAudio a KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH set-property request that specifies the optional node that is to be included in the graph. When SysAudio subsequently creates the pin instance, the pin's graph will include the optional node that was specified in the request.

A KSPROPERTY\_SYSAUDIO\_SELECT\_GRAPH set-property request affects only pin instances that are created after the request. The request has no effect on any previously instantiated pins.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**SYSAUDIO\_SELECT\_GRAPH**](https://msdn.microsoft.com/library/windows/hardware/ff538500)

[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

 

 






