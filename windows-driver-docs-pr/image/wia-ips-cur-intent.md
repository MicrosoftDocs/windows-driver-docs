---
title: WIA_IPS_CUR_INTENT
description: The WIA_IPS_CUR_INTENT property contains the current settings for an application's intended use of an image. The WIA minidriver creates and maintains this property.
keywords: ["WIA_IPS_CUR_INTENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_CUR_INTENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 10/05/2021
ms.localizationpriority: medium
---

# WIA_IPS_CUR_INTENT

The WIA_IPS_CUR_INTENT property contains the current settings for an application's intended use of an image. The WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_FLAG

Access Rights: Read/write

## Remarks

A driver uses the intent settings to pre-set item properties based on an application's intended use of an image. These properties might include, for example, maximum quality and minimum size.

The following table contains the image-type flags and their definitions. These flags are used to set which type of image is intended: color, grayscale, and so on.

| Image type flags | Definition |
|--|--|
| WIA_INTENT_IMAGE_TYPE_COLOR | The application intends to prepare the device for a color scan. |
| WIA_INTENT_IMAGE_TYPE_GRAYSCALE | The application intends to prepare the device for a grayscale scan. |
| WIA_INTENT_IMAGE_TYPE_TEXT | The application intends to prepare the device for scanning text. |
| WIA_INTENT_IMAGE_TYPE_MASK | This flag is a mask for all of the image-type flags. |
| WIA_INTENT_NONE | Default value. No intent is specified. |

The following table contains the image size and quality flags and their definitions. These flags are used to set the size and quality of an image scan.

| Image size/quality Flags | Definition |
|--|--|
| WIA_INTENT_BEST_PREVIEW | The application intends to prepare the device for scanning a preview. |
| WIA_INTENT_MAXIMIZE_QUALITY | The application intends to prepare the device for scanning a high-quality image. |
| WIA_INTENT_MINIMIZE_SIZE | The application intends to prepare the device for scanning an image that results in a small scan. |
| WIA_INTENT_SIZE_MASK | This flag is a mask for all of the size and quality flags. |

The driver chooses the bit depth, in dots per inch, and other settings that it determines are appropriate for the selected intent. The application must read the current settings to determine which properties were changed.

An application sets the WIA_IPS_CUR_INTENT property to auto-set the WIA properties for specific acquisition intent. Note that flags can be combined with a bitwise OR operator, but an image cannot be both grayscale and color.

WIA_IPS_CUR_INTENT is required for all image acquisition enabled items; it is not available for storage items or stored image items.

## Requirements

**Header:** wiadef.h (include Wiadef.h)
