---
title: ENCAPIPARAM_BITRATE
description: The ENCAPIPARAM_BITRATE property is used to describe the bit rate supported by the device.
ms.date: 10/08/2021
---

# ENCAPIPARAM_BITRATE

The ENCAPIPARAM_BITRATE property is used to describe the bit rate (bits per second) supported by the device.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSPROPERTY | ULONG |

The property value (operation data) is a VT_UI4 stepped range of the bit rates supported by the device, specified in the **PropertyItem.Values** member of [**KSPROPERTY_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure.

## Comments

For a sample of how to use this property, see [Encoder Code Examples](./encoder-code-examples.md).

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**VIDEOENCODER_BITRATE_MODE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-videoencoder_bitrate_mode)
