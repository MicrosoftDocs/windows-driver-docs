---
title: KSPROPERTY_DVDSUBPIC_PALETTE
description: The KSPROPERTY_DVDSUBPIC_PALETTE property specifies the color palette that the subpicture stream uses.
keywords: ["KSPROPERTY_DVDSUBPIC_PALETTE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_DVDSUBPIC_PALETTE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 10/19/2021
---

# KSPROPERTY_DVDSUBPIC_PALETTE

The **KSPROPERTY_DVDSUBPIC_PALETTE** property specifies the color palette that the subpicture stream uses.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSPROPERTY_SPPAL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sppal) |

The property value (operation data) is a **KSPROPERTY_SPPAL** structure that describes the color palette to use for the subpicture display in the YUV color format.

## Remarks

The [**KSPROPERTY_SPPAL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sppal) structure contains an array of 16 YUV elements. These elements correspond to the 4-bit color numbers requested within the subpicture command stream.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_SPPAL**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ksproperty_sppal)