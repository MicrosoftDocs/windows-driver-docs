---
title: KSPROPERTY_DVDSUBPIC_COMPOSIT_ON
description: The KSPROPERTY_DVDSUBPIC_COMPOSIT_ON property enables or disables the display of the subpicture.
keywords: ["KSPROPERTY_DVDSUBPIC_COMPOSIT_ON Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_COMPOSIT_ON
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDSUBPIC_COMPOSIT_ON

The **KSPROPERTY_DVDSUBPIC_COMPOSIT_ON** property enables or disables the display of the subpicture.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | **KSPROPERTY_COMPOSIT_ON** |

  [**KSPROPERTY**]: /windows-hardware/drivers/stream/ksproperty-structure

The property value (operation data) is a **KSPROPERTY_COMPOSIT_ON** (a type-defined Boolean). Specify **TRUE** to turn on the subpicture display, or specify **FALSE** to turn off the subpicture display.

## Remarks

If subpicture display is disabled then the decoder must still decode the subpicture data but not display it. This facilitates instant display when a subpicture-enable command is received.

There is a force-display subpicture command in the subpicture data command stream that can override the **KSPROPERTY_DVDSUBPIC_COMPOSIT_ON** property.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)