---
title: KSPROPERTY\_BDA\_PIDFILTER\_UNMAP\_PIDS
description: Clients use KSPROPERTY\_BDA\_PIDFILTER\_UNMAP\_PIDS to inform the PID filter node about packets identified with specific PIDs to filter from the input stream (that is, stop passing from input to output).
keywords: ["KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_BDA\_PIDFILTER\_UNMAP\_PIDS


Clients use KSPROPERTY\_BDA\_PIDFILTER\_UNMAP\_PIDS to inform the PID filter node about packets identified with specific PIDs to filter from the input stream (that is, stop passing from input to output).

## <span id="ddk_ksproperty_bda_pidfilter_unmap_pids_ks"></span><span id="DDK_KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS_KS"></span>


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
<td><p>BDA_PID_UNMAP</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The **NodeId** member of KSP\_NODE specifies the identifier of the PID filter node.

The BDA\_PID\_UNMAP structure describes a map of packets identified with specific PIDs to filter from the input stream.

Any PID in this list that is not passed by the node is ignored.

## Requirements

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


[**BDA\_PID\_UNMAP**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_pid_unmap)

[**KSP\_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

 

