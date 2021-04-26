---
title: KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH
description: The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.
keywords: ["KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 06/18/2020
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH

The KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH property retrieves focal length information for a camera.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter or node | [**KSPROPERTY_CAMERACONTROL_FOCAL_LENGTH_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_focal_length_s) or [**KSPROPERTY_CAMERACONTROL_NODE_FOCAL_LENGTH_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_focal_length_s) | LONG |

The property value (operation data) is a LONG that specifies a camera's focal length.

## Remarks

You can use this property request to interpret zoom values. The range of zoom should be between **lObjectiveFocalLengthMin**/**lOcularFocalLength** and **lObjectiveFocalLengthMax**/**lOcularFocalLength**. (**lOcularFocalLength**, **lObjectiveFocalLengthMin**, and **lObjectiveFocalLengthMax** are members of the [**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_focal_length_s) and [**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_focal_length_s) structures.)

For example, if **lObjectiveFocalLengthMax** = 105 and **lOcularFocalLength** = 35, then this camera is capable of a maximum optical zoom ratio of 105/35, or 3.

Also see the *Optical Zoom* section of the USB Video Class Device Class specification. This specification is available at the [USB Implementers Forum](https://www.usb.org/) website.

## Requirements

| &nbsp; | &nbsp; |
| --- | --- |
| **Header** | Ksmedia.h (include Ksmedia.h) |

## See also

[**KSPROPERTY\_CAMERACONTROL\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_focal_length_s)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_FOCAL\_LENGTH\_S**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-ksproperty_cameracontrol_node_focal_length_s)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM**](ksproperty-cameracontrol-zoom.md)

[**KSPROPERTY\_CAMERACONTROL\_ZOOM\_RELATIVE**](ksproperty-cameracontrol-zoom-relative.md)
