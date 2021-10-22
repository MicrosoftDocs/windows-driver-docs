---
title: KSPROPERTY_BDA_MODULATION_TYPE
description: Clients use KSPROPERTY_BDA_MODULATION_TYPE to control the demodulator type such as QPSK or 8VSB.
keywords: ["KSPROPERTY_BDA_MODULATION_TYPE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_MODULATION_TYPE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_MODULATION_TYPE

Clients use KSPROPERTY_BDA_MODULATION_TYPE to control the demodulator type such as QPSK or 8VSB.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ModulationType |

## Remarks

The returned value from the ModulationType enumerated type identifies a demodulator type.

The **NodeId** member of KSP_NODE specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**ModulationType**](/previous-versions/windows/desktop/mstv/modulationtype)
