---
title: KSPROPERTY_CROSSBAR_CAPS
description: The KSPROPERTY_CROSSBAR_CAPS property retrieves the crossbar capabilities of the device (the number of input and output pins on the crossbar). This property must be implemented.
keywords: ["KSPROPERTY_CROSSBAR_CAPS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CROSSBAR_CAPS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
---

# KSPROPERTY_CROSSBAR_CAPS

The **KSPROPERTY_CROSSBAR_CAPS** property retrieves the crossbar capabilities of the device (the number of input and output pins on the crossbar). This property must be implemented.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY_CROSSBAR_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_caps_s) | Pair of ULONGs |

The property value (operation data) is a pair of ULONGs that specify the number of audio and video input pins on the crossbar, and the number of audio and video output pins on the crossbar.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CROSSBAR_CAPS_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_crossbar_caps_s)
