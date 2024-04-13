---
title: KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE
description: The KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE property specifies a camera's aperture setting.
keywords: ["KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE

The **KSPROPERTY_CAMERACONTROL_IRIS_RELATIVE** property specifies a camera's aperture setting.

## Usage Summary Table

| Get | Set | Target | Property Descriptor Type | Property Value Type |
|--|--|--|--|--|
| No | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's relative iris setting. Note that both the iris step size and the iris step default value are implementation-specific.

| Value | Description |
|--|--|
| 0 | Set the iris to the default opening. This default value is implementation-specific and supplied in hardware. |
| Positive value | Open the iris one step. |
| Negative value | Close the iris one step. |

## Remarks

When making a set request, you should provide one of the values in the preceding table in the **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure.

Set requests will fail if the Auto-Exposure mode control is in Auto mode or Shutter Priority mode.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
