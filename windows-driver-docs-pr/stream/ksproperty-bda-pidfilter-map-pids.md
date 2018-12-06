---
title: KSPROPERTY\_BDA\_PIDFILTER\_MAP\_PIDS
description: Clients use KSPROPERTY\_BDA\_PIDFILTER\_MAP\_PIDS to inform the PID filter node about the list of MPEG2 PIDs of transport stream packets that should be passed to the downstream filter or node.
ms.assetid: 33d2775c-308a-4af0-81ae-b174990926ad
keywords: ["KSPROPERTY_BDA_PIDFILTER_MAP_PIDS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIDFILTER_MAP_PIDS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_PIDFILTER\_MAP\_PIDS


Clients use KSPROPERTY\_BDA\_PIDFILTER\_MAP\_PIDS to inform the PID filter node about the list of MPEG2 PIDs of transport stream packets that should be passed to the downstream filter or node. This property also informs the PID filter node what output type (for example table sections or transport stream) to use when delivering data on the node's output.

## <span id="ddk_ksproperty_bda_pidfilter_map_pids_ks"></span><span id="DDK_KSPROPERTY_BDA_PIDFILTER_MAP_PIDS_KS"></span>


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
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p>KSP_NODE</p></td>
<td><p>BDA_PID_MAP</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **NodeId** member of KSP\_NODE specifies the identifier of the PID filter node.

The BDA\_PID\_MAP structure describes a map of the data to filter out of the input stream.

The PID filter node merges the list that is provided with this property with the list of PIDs that the node currently passes downstream. If a PID in the provided list is already in the PID filter node's list, then the output type of the provided list takes precedence. This property is also used to retrieve the type of data that the node outputs. The BDA\_PID\_MAP structure describes a map of this output data.

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
<td>Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

## See also


[**BDA\_PID\_MAP**](https://msdn.microsoft.com/library/windows/hardware/ff556534)

[**KSP\_NODE**](https://msdn.microsoft.com/library/windows/hardware/ff566720)

 

 






