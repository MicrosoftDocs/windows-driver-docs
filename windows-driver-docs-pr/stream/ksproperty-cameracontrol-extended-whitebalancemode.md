---
title: KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE
description: The white balance mode property specifies the whether auto processing occurs for white balance or a manual temperature value is used instead.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 10/14/2021
---

# KSPROPERTY_CAMERACONTROL_EXTENDED_WHITEBALANCEMODE

The white balance mode property specifies the whether auto processing occurs for white balance or a manual temperature value is used instead.

## Usage Summary Table

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | [**KSPROPERTY**](./ksproperty-structure.md) | [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) |

The property value (operation data) contains a [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure and a [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure.

The total property data size is **sizeof**(KSCAMERA_EXTENDEDPROP_HEADER) + **sizeof**(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING). The **Size** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) is set to this total property data size.

The **Capability** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains a bitwise OR combination of one or more of the following video processing options.

| Processing mode | Description |
|--|--|
| KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO | Camera driver uses its own processing logic for video. |
| KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL | Camera driver uses a preset processing method or a temperature based method. |
| KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK | The current video processing method is locked. |

The **Flags** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) contains the video processing flag currently set for the camera. The KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO setting may be combined with KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK.

This property control is asynchronous and not cancelable.

## Remarks

### Processing modes

**KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO**  
This indicates that auto processing is supported. The driver will use its internal logic to optimize the video processing. For a **KSPROPERTY_TYPE_GET** request, the **VideoProc** member of [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) must contain the current driver determined value for the video processing. In the case of White Balance, it must contain the current temperature in Kelvin. The **Mode** member is ignored for auto operation.

This flag may be combined with **KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK** as a bitwise OR value. When locked, the expected behavior of the camera driver is to converge on white balance and lock the white balance value to the converged value, not attempting to auto-white balance again, until a new white balance command is received.

Locking, without combining Auto mode, an already locked control should be treated as a no-op by the camera driver. Locking, in combination with Auto mode, an already locked control should trigger a new convergence.

**KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_MANUAL**  
Manual indicates that for this video processing, the specific values are provided. In the case of white balance, if the **Mode** member of [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) indicates **KSCAMERA_EXTENDEDPROP_WHITEBALANCE_TEMPERATURE**, the **VideoProc.Value.ul** will contain the temperature value in degrees Kelvin.

**KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK**
The lock option flag indicates that the current video processing is locked to whatever value is currently programmed. For example, an application may request auto mode until a specific white balance is determined, At that point the application will decide to take a sequence of photos all with the same white balance setting. In such a case, the application may specify the **KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_LOCK** flag. The camera driver will ensure the white balance information does not change across the different photos.

### Getting the property

When responding to a **KSPROPERTY_TYPE_GET** request, the driver sets the members of the [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) to the following.

| Member | Value |
|--|--|
| Version | 1 |
| PinId | KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF) |
| Size | sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING) |
| Result | 0 |
| Capability | KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL OR'd with (Video processing mode supported) |
| Flags | The current video processing mode. |

If no white balance mode was previously set, then the driver sets **Flags** to KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO (default). The members of the [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) structure that follows [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) are set according to the requirements of the processing mode.

### Setting the property

When the property is set, a KSPROPERTY_TYPE_SET request, the **Flags** member of [**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) will contain the white balance mode to set. The **VideoProc.Value** member of [**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting) must be ignored when **Flags** contains the KSCAMERA_EXTENDEDPROP_VIDEOPROCFLAG_AUTO mode flag.

## Requirements

**Version:** Available starting with Windows 8.1

**Header:** ksmedia.h (include Ksmedia.h)

## See also

[**KSCAMERA_EXTENDEDPROP_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header)

[**KSCAMERA_EXTENDEDPROP_VIDEOPROCSETTING**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_videoprocsetting)

[**KSPROPERTY_CAMERACONTROL_EXTENDED_EXPOSUREMODE**](ksproperty-cameracontrol-extended-exposuremode.md)