---
title: KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER
description: Clients use KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER along with KSPROPERTY_BDA_RF_TUNER_FREQUENCY to control the frequency setting of the tuner node.
keywords: ["KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER

Clients use **KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER** along with **KSPROPERTY_BDA_RF_TUNER_FREQUENCY** to control the frequency setting of the tuner node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the tuner node.

The property value specifies the frequency multiplier to set.

If the **KSPROPERTY_BDA_RF_TUNER_FREQUENCY_MULTIPLIER** property specified a multiplier of **BDA_FREQUENCY_MULTIPLIER_NOT_SET** (−1) or **BDA_FREQUENCY_MULTIPLIER_NOT_DEFINED** (0), then the **KSPROPERTY_BDA_RF_TUNER_FREQUENCY** property specifies the frequency in kilohertz (kHz). In addition, if the minidriver's set handler ([*KStrSetPropertyHandler*](/previous-versions/ff567200(v=vs.85))) for the frequency multiplier property is not called, the minidriver must determine that the supplied frequency is expressed in units of kHz (1Hz x 1000). In effect, the default multiplier value is 1000. For more information, see [Accessing Frequency Properties of a BDA Tuner Node](./accessing-frequency-properties-of-a-bda-tuner-node.md).

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**KSPROPERTY_BDA_RF_TUNER_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)
