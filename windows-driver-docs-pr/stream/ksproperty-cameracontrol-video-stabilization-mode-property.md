---
title: KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY
description: User-mode clients use this property to get or set a camera's video stabilization characteristics. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY

User-mode clients use this property to get or set a camera's video stabilization characteristics. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s) |

## Remarks

The property ID is **KSPROPERTY_CAMERACONTROL_VIDEO_STABILIZATION_MODE_PROPERTY_ID**.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_VIDEOSTABILIZATION_MODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_videostabilization_mode_s)
