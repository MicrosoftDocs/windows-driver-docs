---
title: KSPROPERTY_BDA_ECM_MAP_STATUS
description: Clients use KSPROPERTY_BDA_ECM_MAP_STATUS to determine status on an ECM map node.
keywords: ["KSPROPERTY_BDA_ECM_MAP_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_ECM_MAP_STATUS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_ECM_MAP_STATUS

Clients use **KSPROPERTY_BDA_ECM_MAP_STATUS** to determine status on an ECM map node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ULONG |

## Remarks

The returned value specifies the ECM map node status.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSEVENT_BDA_PROGRAM_FLOW_STATUS_CHANGED**](ksevent-bda-program-flow-status-changed.md)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
