---
title: KSPROPERTY_BDA_LNB_LOF_HIGH_BAND
description: Clients use KSPROPERTY_BDA_LNB_LOF_HIGH_BAND to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming high-band RF signals.
keywords: ["KSPROPERTY_BDA_LNB_LOF_HIGH_BAND Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_LNB_LOF_HIGH_BAND
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_LNB_LOF_HIGH_BAND

Clients use **KSPROPERTY_BDA_LNB_LOF_HIGH_BAND** to inform the RF tuner node about the local oscillator frequency (LOF) that is used by the low-noise block (LNB) device for shifting the frequency of incoming high-band RF signals.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ULONG |

## Remarks

The **NodeId** member of KSP_NODE specifies the identifier of the RF tuner node.

The property value specifies the LOF that is used by the LNB for high-band signals.

The LNB gathers the RF signal reflected by the satellite dish, shifts the frequency of the RF signal down by the high-band LOF amount, and sends the resulting signal to the RF tuner.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)
