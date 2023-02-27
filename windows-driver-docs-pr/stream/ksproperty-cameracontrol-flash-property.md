---
title: KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY
description: User-mode clients use this property to get or set a camera's flash control characteristics. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY

User-mode clients use this property to get or set a camera's flash control characteristics. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSPROPERTY_CAMERACONTROL_FLASH_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_flash_s) |

## Remarks

The property ID is **KSPROPERTY_CAMERACONTROL_FLASH_PROPERTY_ID**.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_FLASH_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_flash_s)