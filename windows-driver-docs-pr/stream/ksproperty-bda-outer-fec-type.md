---
title: KSPROPERTY_BDA_OUTER_FEC_TYPE
description: Clients use KSPROPERTY_BDA_OUTER_FEC_TYPE to control the outer forward error correction (FEC) type of a demodulator node.
keywords: ["KSPROPERTY_BDA_OUTER_FEC_TYPE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_OUTER_FEC_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_OUTER_FEC_TYPE

Clients use **KSPROPERTY_BDA_OUTER_FEC_TYPE** to control the outer forward error correction (FEC) type of a demodulator node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**FECMethod**](/previous-versions/windows/desktop/mstv/fecmethod) |

## Remarks

The returned value from the FECMethod enumerated type identifies an FEC type.

The **NodeId** member of **KSP_NODE** specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**FECMethod**](/previous-versions/windows/desktop/mstv/fecmethod)

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
