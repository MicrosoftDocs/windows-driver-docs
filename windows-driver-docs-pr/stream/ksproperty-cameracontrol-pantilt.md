---
title: KSPROPERTY_CAMERACONTROL_PANTILT
description: The KSPROPERTY_CAMERACONTROL_PANTILT property specifies absolute pan and tilt settings.
keywords: ["KSPROPERTY_CAMERACONTROL_PANTILT Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_PANTILT
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CAMERACONTROL_PANTILT

The **KSPROPERTY_CAMERACONTROL_PANTILT** property specifies absolute pan and tilt settings.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2) or [**KSPROPERTY_CAMERACONTROL_NODE_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2) depending on whether the request is for a filter or a node | Pair of LONG integers |

The property value (operation data) is a pair of LONG integers that specify a camera's absolute pan and tilt settings. These values are expressed in arc-second units.

One arc second is 1/3600 of a degree. Acceptable values range from −180\*3600 to +180\*3600 arc seconds. If a pan or tilt value is not provided, the default is 0.

When making a pan request, specify a positive value to rotate the camera to the right and specify a negative value to rotate the camera to the left.

When making a tilt request, a positive value tilts the camera up and a negative value tilts the camera down.

## Remarks

The **Value1** member of the [**KSPROPERTY_CAMERACONTROL_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2) or [**KSPROPERTY_CAMERACONTROL_NODE_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2) structures specifies the pan setting. The **Value2** member specifies the tilt setting.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s2)

[**KSPROPERTY_CAMERACONTROL_NODE_S2**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s2)
