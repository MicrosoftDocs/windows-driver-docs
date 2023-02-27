---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE (assistant flash)
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE property is extended to support assistant flash.
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FLASHMODE (assistant flash)
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 07/08/2020
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE

The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property is extended to support assistant flash.

## Usage summary table

| Scope | Control | Type |
|--|--|--|
| Version 1 | Filter | Synchronous |

The capability flags are defined as follows.

```cpp
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_ON               0x0000000000000080
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_AUTO             0x0000000000000100
#define KSCAMERA_EXTENDEDPROP_FLASH_ASSISTANT_OFF              0x0000000000000000
```

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_ON**

This flag indicates that the AF assistant light is turned on.

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_AUTO**

This flag is similar to the **ASSISTANT\_ON** flag. Instead of always turning on the AF assistant light, the camera driver will determine if the AF assistant light should be turned on based on the current lighting condition.

**KSCAMERA\_EXTENDEDPROP\_FLASH\_ASSISTANT\_OFF**

This flag indicates that AF assistant light is off.

The descriptions for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header) structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE** property are the same as the Windows 8.1 DDI.

## Requirements

**Header:** Ksmedia.h (include Ksmedia.h)
