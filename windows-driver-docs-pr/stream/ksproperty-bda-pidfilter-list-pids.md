---
title: KSPROPERTY_BDA_PIDFILTER_LIST_PIDS
description: Clients use KSPROPERTY_BDA_PIDFILTER_LIST_PIDS to retrieve from a PID filter node the list of its PIDs that identify groups of packets that the node delivers from the input stream to the output stream.
keywords: ["KSPROPERTY_BDA_PIDFILTER_LIST_PIDS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_PIDFILTER_LIST_PIDS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_PIDFILTER_LIST_PIDS

Clients use **KSPROPERTY_BDA_PIDFILTER_LIST_PIDS** to retrieve from a PID filter node the list of its PIDs that identify groups of packets that the node delivers from the input stream to the output stream.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | List of PIDs |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the PID filter node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
