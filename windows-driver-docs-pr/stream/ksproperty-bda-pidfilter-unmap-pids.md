---
title: KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS
description: Clients use KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS to inform the PID filter node about packets identified with specific PIDs to filter from the input stream (that is, stop passing from input to output).
keywords: ["KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS

Clients use **KSPROPERTY_BDA_PIDFILTER_UNMAP_PIDS** to inform the PID filter node about packets identified with specific PIDs to filter from the input stream (that is, stop passing from input to output).

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**BDA_PID_UNMAP**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_pid_unmap) |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the PID filter node.

The **BDA_PID_UNMAP** structure describes a map of packets identified with specific PIDs to filter from the input stream.

Any PID in this list that is not passed by the node is ignored.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BDA_PID_UNMAP**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_pid_unmap)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
