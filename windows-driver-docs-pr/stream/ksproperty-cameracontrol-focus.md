---
title: KSPROPERTY_CAMERACONTROL_FOCUS
description: User-mode clients use the KSPROPERTY_CAMERACONTROL_FOCUS property to get or set a camera's focus setting. This property is optional.
keywords: ["KSPROPERTY_CAMERACONTROL_FOCUS Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_FOCUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_FOCUS

User-mode clients use the **KSPROPERTY_CAMERACONTROL_FOCUS** property to get or set a camera's focus setting. This property is optional.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies the focus setting. This value is expressed in millimeters.

> [!CAUTION]
> When writing or testing an app, you should be aware that in practice, some drivers define a custom range of focus values and custom step values that might not be based on typical units. Drivers might implement the focus control either physically or digitally.

## Remarks

The **Value** member of the **KSPROPERTY_CAMERACONTROL_S** structure specifies the focus setting.

Every video capture minidriver that supports this property must define its own range and default value for this property.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)
