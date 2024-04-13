---
title: KSPROPERTY\_FMRX\_ANTENNAENDPOINTID
description: The KSTOPOLOGY\_ENDPOINTID property contains information about the endpoint to be used as FM antenna.
keywords: ["KSPROPERTY_FMRX_ANTENNAENDPOINTID Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_FMRX_ANTENNAENDPOINTID
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 03/06/2023
---


# KSPROPERTY\_FMRX\_ANTENNAENDPOINTID


The [**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid) property contains information about the endpoint to be used as FM antenna.

## <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table


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
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid" data-raw-source="[&lt;strong&gt;KSTOPOLOGY_ENDPOINTID&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid)"><strong>KSTOPOLOGY_ENDPOINTID</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value is of type [**KSTOPOLOGY\_ENDPOINTID**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_tagkstopology_endpointid) and specifies the name and the pin ID of the topology endpoint associated with FM radio receive antenna.

## <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value


A KSPROPERTY\_FMRX\_ANTENNAENDPOINTID property request returns the name and the pin id of the endpoint to be used as FM radio antenna.

## Requirements

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
