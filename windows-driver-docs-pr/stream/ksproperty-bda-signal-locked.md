---
title: KSPROPERTY_BDA_SIGNAL_LOCKED
description: Clients use KSPROPERTY_BDA_SIGNAL_LOCKED to determine whether a signal can be locked.
keywords: ["KSPROPERTY_BDA_SIGNAL_LOCKED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_BDA_SIGNAL_LOCKED
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_BDA_SIGNAL_LOCKED

Clients use **KSPROPERTY_BDA_SIGNAL_LOCKED** to determine whether a signal can be locked.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Pin or Filter | [**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node) | BOOL |

## Remarks

The **NodeId** member of **KSP_NODE** specifies the identifier of the control node or is set to −1 to specify a pin.

The returned value indicates whether a signal can be locked. Returns **TRUE** if a signal can be locked and **FALSE** otherwise.

If an RF tuner node returns **TRUE**, a phase-lock-loop (PLL) lock is typically indicated.

If a demodulator node returns **TRUE**, a signal quality of at least 20% is indicated.

## Requirements

**Header:** bdamedia.h (include Bdamedia.h)

## See also

[**KSP_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-ksp_node)

[**KSPROPERTY_BDA_SIGNAL_QUALITY**](ksproperty-bda-signal-quality.md)
