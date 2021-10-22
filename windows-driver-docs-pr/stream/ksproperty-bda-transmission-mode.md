---
title: KSPROPERTY_BDA_TRANSMISSION_MODE
description: Clients use KSPROPERTY_BDA_TRANSMISSION_MODE to control the setting on a demodulator node for how broadcast signals are transmitted.
keywords: ["KSPROPERTY_BDA_TRANSMISSION_MODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_TRANSMISSION_MODE
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_BDA_TRANSMISSION_MODE

Clients use **KSPROPERTY_BDA_TRANSMISSION_MODE** to control the setting on a demodulator node for how broadcast signals are transmitted.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | [**TransmissionMode**](/previous-versions/windows/desktop/mstv/transmissionmode) |

## Remarks

The returned value from the **TransmissionMode** enumerated type identifies a setting for how broadcast signals are transmitted.

The **NodeId** member of **KSP_NODE** specifies the identifier of the demodulator node.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**TransmissionMode**](/previous-versions/windows/desktop/mstv/transmissionmode)
