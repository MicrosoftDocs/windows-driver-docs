---
title: ENCAPIPARAM_PEAK_BITRATE
description: The ENCAPIPARAM_BITRATE property is used to describe the supported peak bit rate range of the device.
ms.date: 11/28/2017
---

# ENCAPIPARAM_PEAK_BITRATE

The ENCAPIPARAM_BITRATE property is used to describe the supported peak bit rate (bits per second) range of the device.

| Get | Set | Target | Property descriptor type | Property value type |
| ----- | ----- | -------- | -------------------------- | --------------------- |
| Yes | Yes | Filter | KSPROPERTY | ULONG |

The property value (operation data) is a VT_UI4 stepped range of peak bit rates of the device, specified in the **PropertyItem.Values** member of [**KSPROPERTY_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure.

## Comments

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**VIDEOENCODER_BITRATE_MODE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-videoencoder_bitrate_mode)
