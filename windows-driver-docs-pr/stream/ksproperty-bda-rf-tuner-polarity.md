---
title: KSPROPERTY_BDA_RF_TUNER_POLARITY
description: Clients use KSPROPERTY_BDA_RF_TUNER_POLARITY to control the polarity setting of the tuner node.
keywords: ["KSPROPERTY_BDA_RF_TUNER_POLARITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_POLARITY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_RF_TUNER_POLARITY

Clients use **KSPROPERTY_BDA_RF_TUNER_POLARITY** to control the polarity setting of the tuner node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the tuner node.

The property value specifies the polarity to set for the transmitted signal.

For some transmissions, particularly satellite transmissions, the signal may be polarized. This property informs the tuner node about the polarization of the transmitted signal. The Polarization enumerated type contains values that specify the polarity of the signal.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**Polarization**](/previous-versions/windows/hardware/drivers/ff567780(v=vs.85))
