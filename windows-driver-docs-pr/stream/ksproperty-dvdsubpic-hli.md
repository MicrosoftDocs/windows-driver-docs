---
title: KSPROPERTY_DVDSUBPIC_HLI
description: The KSPROPERTY_DVDSUBPIC_HLI property specifies the rectangle of the subpicture or screen to change, including the color or contrast.
keywords: ["KSPROPERTY_DVDSUBPIC_HLI Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_HLI
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDSUBPIC_HLI

The **KSPROPERTY_DVDSUBPIC_HLI** property specifies the rectangle of the subpicture or screen to change, including the color or contrast.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSPROPERTY_SPHLI**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sphli) |

The property value (operation data) is a **KSPROPERTY_SPHLI** structure that describes the DVD highlight information to change.

## Remarks

The [**KSPROPERTY_SPHLI**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sphli) structure describes the currently selected button from the DVD highlight information.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_SPHLI**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sphli)