---
title: ENCAPIPARAM_BITRATE_MODE
description: The ENCAPIPARAM_BITRATE property is used to describe the encoding mode of the device.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# ENCAPIPARAM_BITRATE_MODE

The ENCAPIPARAM_BITRATE property is used to describe the encoding mode of the device.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | Yes | Filter | KSPROPERTY | LONG |

The property value (operation data) is a VT_I4 value specified in the **PropertyItem.Values** member of the [**KSPROPERTY_SET**](/windows-hardware/drivers/ddi/ks/ns-ks-ksproperty_set) structure with a discrete list of supported values out of the [**VIDEOENCODER_BITRATE_MODE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-videoencoder_bitrate_mode) enumeration.

## Comments

For a sample of how to use this property, see [Encoder Code Examples](./encoder-code-examples.md).

The minidriver is required to either provide a static **PropertyItem.Values** description in the property item or handle a basic support query and fill the values in. The minidriver must also specify the defaults for this property.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)

[**VIDEOENCODER_BITRATE_MODE**](/windows-hardware/drivers/ddi/ksmedia/ne-ksmedia-videoencoder_bitrate_mode)
