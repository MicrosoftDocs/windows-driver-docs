---
title: KSPROPERTY_BDA_CA_MODULE_STATUS
description: Clients use KSPROPERTY_BDA_CA_MODULE_STATUS to determine status on the CA module associated with an ECM map node.
keywords: ["KSPROPERTY_BDA_CA_MODULE_STATUS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_CA_MODULE_STATUS
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_CA_MODULE_STATUS

Clients use **KSPROPERTY_BDA_CA_MODULE_STATUS** to determine status on the CA module associated with an ECM map node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ULONG |

## Remarks

The returned value specifies the CA module status.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSEVENT_BDA_CA_MODULE_STATUS_CHANGED**](ksevent-bda-ca-module-status-changed.md)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
