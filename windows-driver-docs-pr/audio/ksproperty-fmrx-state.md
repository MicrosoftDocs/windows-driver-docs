---
title: KSPROPERTY\_FMRX\_STATE
description: The KSPROPERTY\_FMRX\_STATE property specifies whether FM radio is enabled.
ms.assetid: A975221C-3300-4A44-9E8C-9AB4B4C54C32
keywords: ["KSPROPERTY_FMRX_STATE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_FMRX_STATE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_FMRX\_STATE


The **KSPROPERTY\_FMRX\_STATE** property specifies whether FM radio is enabled.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value is of type BOOL and specifies whether FM radio is enabled.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_FMRX\_STATE** property request returns **TRUE** if FM radio is enabled and **FALSE** if FM radio is disabled.

Remarks
-------

FM radio can be enabled or disabled by setting the **KSPROPERTY\_FMRX\_STATE** property on the wave filter. The FM volume and routing (endpoint selection) is controlled by the [**KSPROPERTY\_FMRX\_VOLUME**](ksproperty-fmrx-volume.md) and [**KSPROPERTY\_FMRX\_ENDPOINTID**](ksproperty-fmrx-endpointid.md) properties on the topology filter. Basic support for the **KSPROPERTY\_FMRX\_VOLUME** property should return the minimum volume, maximum volume, and the volume ranges.

A new [**KSNODETYPE\_FM\_RX**](ksnodetype-fm-rx.md) topology node endpoint is implemented as any other audio endpoint is in the system, and it supports all audio endpoint properties. This endpoint also supports jack properties that are defined under the [KSPROPSETID\_Jack](kspropsetid-jack.md) property set. This endpoint is in the unplugged state at boot. If capturing FM radio is supported by driver, this endpoint becomes active when FM radio is enabled. Creating a capture pin on the **KSNODETYPE\_FM\_RX** topology node allows audio capture that comes over from FM receiver.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Client</p></td>
<td align="left"><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 





