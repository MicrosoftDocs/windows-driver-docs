---
title: KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY
description: User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. If they are mutually exclusive, then when the record pin is active, the image pin cannot be active, and vice-versa.
keywords: ["KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY
api_type:
- NA
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_PROPERTY

User-mode clients use this property to identify whether the camera's image pin and record pin are mutually exclusive. If they are mutually exclusive, then when the record pin is active, the image pin cannot be active, and vice-versa.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | [**KSPROPERTY**](/windows-hardware/drivers/stream/ksproperty-structure) | [**KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s) |

## Remarks

If a driver implements this property and identifies that the image pin is exclusive with the record pin, the media streaming pipeline prevents a "take photo" command from coming to the driver while a recording is taking place.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_IMAGE_PIN_CAPABILITY_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_image_pin_capability_s)
