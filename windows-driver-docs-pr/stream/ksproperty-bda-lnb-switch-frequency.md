---
title: KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY
description: Clients use KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.
keywords: ["KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/13/2021
---

# KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY

Clients use **KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY** to inform the RF tuner node about the frequency of incoming RF signals at which the tuner should inform the low-noise block (LNB) device to switch from using low-band local oscillator frequency (LOF) to using high-band LOF or vice versa when the LNB shifts the frequency of RF signals.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSP_NODE | ULONG |

## Remarks

The **NodeId** member of KSP_NODE specifies the identifier of the RF tuner node.

The property value specifies the frequency of incoming RF signals at which the LNB should switch from using low-band LOF to using high-band LOF.

If a client sends a **KSPROPERTY_BDA_RF_TUNER_FREQUENCY** request to tune an RF tuner to a specific frequency and this frequency is greater than or equal to the switch frequency specified using **KSPROPERTY_BDA_LNB_SWITCH_FREQUENCY**, then the RF tuner should send a command to the LNB to switch to the high-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the high-band LOF amount, which was specified using **KSPROPERTY_BDA_LNB_LOF_HIGH_BAND**.

Likewise, if a client sends a **KSPROPERTY_BDA_RF_TUNER_FREQUENCY** request to tune an RF tuner to a specific frequency and this frequency is less than the switch frequency, then the RF tuner should send a command to the LNB to switch to the low-band LOF. The RF tuner should then expect that the LNB device shifts the frequency of the incoming RF signal by the low-band LOF amount, which was specified using **KSPROPERTY_BDA_LNB_LOF_LOW_BAND**.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**KSPROPERTY_BDA_LNB_LOF_HIGH_BAND**](ksproperty-bda-lnb-lof-high-band.md)

[**KSPROPERTY_BDA_LNB_LOF_LOW_BAND**](ksproperty-bda-lnb-lof-low-band.md)

[**KSPROPERTY_BDA_RF_TUNER_FREQUENCY**](ksproperty-bda-rf-tuner-frequency.md)
