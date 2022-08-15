---
title: KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE property specifies the electronic shutter speed.
keywords: ["KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE

The **KSPROPERTY_CAMERACONTROL_EXPOSURE_RELATIVE** property specifies the electronic shutter speed.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's relative exposure setting. Step size is hardware-dependent. To determine the step size, you can make a get request on the [**KSPROPERTY_CAMERACONTROL_EXPOSURE**](ksproperty-cameracontrol-exposure.md) property.

| Value | Description |
|--|--|
| 0 | Set the exposure time to the implementation-specific default value. |
| Positive value | Increment the exposure time by one step. |
| Negative value | Decrement the exposure time by one step. |

## Remarks

When making a set request, you should provide one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure.

When making a get request, the client receives one of the values in the preceding table in the Value member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure. The value indicates the current exposure time setting for the camera.

Set requests will fail if the Auto-Exposure mode control is in Auto mode or Aperture Priority mode.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
