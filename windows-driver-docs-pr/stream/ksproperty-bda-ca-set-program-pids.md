---
title: KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS
description: Clients use KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS to set the list of packet identifiers in a particular program.
keywords: ["KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS

Clients use **KSPROPERTY_BDA_CA_SET_PROGRAM_PIDS** to set the list of packet identifiers in a particular program.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | BDA_PROGRAM_PID_LIST |

## Remarks

The BDA_PROGRAM_PID_LIST structure contains the list of packet identifiers for a specified program.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**BDA_PROGRAM_PID_LIST**](/windows-hardware/drivers/ddi/bdatypes/ns-bdatypes-_bda_program_pid_list)

[**KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED**](ksevent-bda-program-flow-status-changed.md)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
