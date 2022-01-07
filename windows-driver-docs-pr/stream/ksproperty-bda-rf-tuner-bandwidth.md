---
title: KSPROPERTY_BDA_RF_TUNER_BANDWIDTH
description: Clients use KSPROPERTY_BDA_RF_TUNER_BANDWIDTH to control the bandwidth setting of the tuner node.
keywords: ["KSPROPERTY_BDA_RF_TUNER_BANDWIDTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_RF_TUNER_BANDWIDTH
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_RF_TUNER_BANDWIDTH

Clients use **KSPROPERTY_BDA_RF_TUNER_BANDWIDTH** to control the bandwidth setting of the tuner node.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | ULONG |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the tuner node.

The property value specifies the bandwidth to set. Bandwidth is the range of frequencies used to transmit a signal or group of interrelated signals. In other words, the amount of information that can be transmitted at one time.

Specifying the **KSPROPERTY_BDA_RF_TUNER_BANDWIDTH** property with:

- **BDA_CHAN_BANDWIDTH_NOT_SET** (−1) indicates that the bandwidth is not set.

- **BDA_CHAN_BANDWIDTH_NOT_DEFINED** (0) indicates that the bandwidth is not defined.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
