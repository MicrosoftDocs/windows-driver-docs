---
title: KSPROPERTY_CAMERACONTROL_SCANMODE
description: The KSPROPERTY_CAMERACONTROL_SCANMODE property specifies the scanning mode of the camera sensor.
keywords: ["KSPROPERTY_CAMERACONTROL_SCANMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_SCANMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/18/2021
ms.localizationpriority: medium
---

# KSPROPERTY_CAMERACONTROL_SCANMODE

The **KSPROPERTY_CAMERACONTROL_SCANMODE** property specifies the scanning mode of the camera sensor.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter or node | [**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s) or [**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s) | LONG |

The property value (operation data) is a LONG that specifies whether interlace mode should be enabled. A value of 0 indicates that the interlace mode is enabled, and a value of 1 indicates that the progressive (or non-interlace) mode is enabled.

## Remarks

The **Value** member of the **KSPROPERTY_CAMERACONTROL_NODE_S** structure specifies whether interlace mode should be enabled.

## Requirements

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSPROPERTY_CAMERACONTROL_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_s)

[**KSPROPERTY_CAMERACONTROL_NODE_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_s)
