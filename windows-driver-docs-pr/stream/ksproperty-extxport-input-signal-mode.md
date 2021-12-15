---
title: KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE
description: The KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE property sets or gets an external device's current input signal mode. For example DV-SD/NTSC/PAL, DV-SL/NTSC/PAL, MPEG2-TS, etc.
keywords: ["KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/20/2021
---

# KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE

The **KSPROPERTY_EXTXPORT_INPUT_SIGNAL_MODE** property sets or gets an external device's current input signal mode. For example, DV-SD/NTSC/PAL, DV-SL/NTSC/PAL, MPEG2-TS, and so on.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Device | [**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s) | ULONG |

The property value (operation data) is a ULONG that specifies the current input signal mode of the external transport.

## Remarks

The **SignalMode** member of the **KSPROPERTY_EXTXPORT_S** structure specifies the input signal mode.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_EXTXPORT_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_extxport_s)
