---
title: KSPROPERTY_BDA_PIDFILTER_MAP_PIDS
description: Clients use KSPROPERTY_BDA_PIDFILTER_MAP_PIDS to inform the PID filter node about the list of MPEG2 PIDs of transport stream packets that should be passed to the downstream filter or node.
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
---

# KSPROPERTY_BDA_PIDFILTER_MAP_PIDS

Clients use **KSPROPERTY_BDA_PIDFILTER_MAP_PIDS** to inform the PID filter node about the list of MPEG2 PIDs of transport stream packets that should be passed to the downstream filter or node. This property also informs the PID filter node what output type (for example table sections or transport stream) to use when delivering data on the node's output.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**BDA_PID_MAP**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_pid_map) |

## Remarks

The **NodeId** member of KSP_NODE specifies the identifier of the PID filter node.

The BDA_PID_MAP structure describes a map of the data to filter out of the input stream.

The PID filter node merges the list that is provided with this property with the list of PIDs that the node currently passes downstream. If a PID in the provided list is already in the PID filter node's list, then the output type of the provided list takes precedence. This property is also used to retrieve the type of data that the node outputs. The **BDA_PID_MAP** structure describes a map of this output data.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BDA_PID_MAP**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_pid_map)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
