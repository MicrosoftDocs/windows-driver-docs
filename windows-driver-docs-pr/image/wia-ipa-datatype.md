---
title: WIA_IPA_DATATYPE
description: The WIA_IPA_DATATYPE property contains the current data type setting for a device. A WIA minidriver creates and maintains this property.
keywords: ["WIA_IPA_DATATYPE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_IPA_DATATYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/11/2023
---

# WIA_IPA_DATATYPE

The WIA_IPA_DATATYPE property contains the current data type setting for a device. A WIA minidriver creates and maintains this property.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

An application reads the WIA_IPA_DATATYPE property to determine the data type of an image. The application writes this property to set the current data type of the image that is about to be transferred.

The following table describes the constants that are valid with WIA_IPA_DATATYPE when the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property is not set to WiaImgFmt_RAW.

| Data type | Description |
|--|--|
| WIA_DATA_AUTO | This value is valid for all programmable image data source items, including the Flatbed and Feeder. When this value is supported by the WIA mini-driver the WIA application client can set: **WIA_IPA_DATATYPE** in order to enable automatic color detection at the device.<br><br>When WIA_DATA_AUTO is set, the WIA mini-driver must update [**WIA_IPA_DEPTH**](wia-ipa-depth.md) on the same item to WIA_DEPTH_AUTO (which must be a supported value if the device supports automatic color).<br><br>When the [**WIA_IPA_DEPTH**](wia-ipa-depth.md) value WIA_DEPTH_AUTO is supported, the **WIA_IPA_DATATYPE** value WIA_DATA_AUTO is no longer optional and becomes a required value. |
| WIA_DATA_COLOR | Scan data is red-green-blue (RGB). The full color format is described by using the following WIA properties:<br><br>[**WIA_IPA_CHANNELS_PER_PIXEL**](wia-ipa-channels-per-pixel.md)<br><br>[**WIA_IPA_BITS_PER_CHANNEL**](wia-ipa-bits-per-channel.md)<br><br>[**WIA_IPA_PLANAR**](wia-ipa-planar.md)<br><br>[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)<br><br>[**WIA_IPA_BYTES_PER_LINE**](wia-ipa-bytes-per-line.md)<br><br>[**WIA_IPA_NUMBER_OF_LINES**](wia-ipa-number-of-lines.md) |
| WIA_DATA_COLOR_DITHER | The same as WIA_DATA_COLOR, except that the data is dithered by using the currently selected dither pattern. |
| WIA_DATA_COLOR_THRESHOLD | Color threshold data. |
| WIA_DATA_DITHER | Scan data is dithered by using the currently selected dither pattern. |
| WIA_DATA_GRAYSCALE | Scan data represents intensity. The palette is a fixed, equally spaced grayscale with a depth that the [**WIA_IPA_DEPTH**](wia-ipa-depth.md) property specifies. |
| WIA_DATA_THRESHOLD | The threshold is one bit per pixel of black-and-white data. Data over the current value of [**WIA_IPS_THRESHOLD**](wia-ips-threshold.md) is converted to white; data under this value is converted to black. |

The WIA_IPA_DATATYPE property is also used to describe the type of RAW data transfer to be used when the application sets the [**WIA_IPA_FORMAT**](wia-ipa-format.md) property to the value WiaImgFmt_RAW. The driver should set the WIA_IPA_DATATYPE property to a list of allowed values from which the application can pick.

The following table lists the constants that are valid with WIA_IPA_DATATYPE when WIA_IPA_FORMAT is set to WiaImgFmt_RAW.

| Data type | Description |
|--|--|
| WIA_DATA_GRAYSCALE | Scan data represents intensity. The palette is a fixed, equally spaced grayscale with a depth that the [**WIA_IPA_DEPTH**](wia-ipa-depth.md) property specifies.<br><br>[**WIA_IPA_RAW_BITS_PER_CHANNEL**](wia-ipa-raw-bits-per-channel.md) property must be set to 1. |
| WIA_DATA_RAW_BGR | Scan data is in the BGR (blue-green-red) colorspace. The full color format is described by using the following WIA properties:<br><br>[**WIA_IPA_CHANNELS_PER_PIXEL**](wia-ipa-channels-per-pixel.md)<br><br>[**WIA_IPA_BITS_PER_CHANNEL**](wia-ipa-bits-per-channel.md)<br><br>[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)<br><br>[**WIA_IPA_BYTES_PER_LINE**](wia-ipa-bytes-per-line.md)<br><br>[**WIA_IPA_NUMBER_OF_LINES**](wia-ipa-number-of-lines.md)<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 3. |
| WIA_DATA_RAW_CMY | Scan data is in the cyan-magenta-yellow (CMY) colorspace. The full color format is described by using the same WIA properties that are listed for WIA_DATA_RAW_BGR.<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 3. |
| WIA_DATA_RAW_CMYK | Scan data is in the cyan-magenta-yellow-black (CMYK) colorspace. The full color format is described by using the same WIA properties that are listed for WIA_DATA_RAW_BGR.<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 4. |
| WIA_DATA_RAW_RGB | Scan data is in the red-green-blue (RGB) colorspace. The full color format is described using the same WIA properties as in WIA_DATA_RAW_BGR.<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 3. |
| WIA_DATA_RAW_YUV | Scan data is in the luminance-blue difference-red difference (YUV) colorspace. The full color format is described by using the same WIA properties that are listed for WIA_DATA_RAW_BGR.<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 3. |
| WIA_DATA_RAW_YUVK | Scan data is in the luminance-blue difference-red difference-black (YUVK) colorspace. The full color format is described by using the same WIA properties that are listed for WIA_DATA_RAW_BGR.<br><br>WIA_IPA_RAW_BITS_PER_CHANNEL must be set to 4. |

If you can set the device to only a single value, create a WIA_PROP_LIST type and place the valid value in it.

Check the [**WIA_IPA_DEPTH**](wia-ipa-depth.md) property to determine the bit depth.

The WIA_IPA_DATATYPE property usually contains a single value for cameras.

## Requirements

**Header:** wiadef.h (include Wiadef.h)

## See also

[**WIA_IPA_BITS_PER_CHANNEL**](wia-ipa-bits-per-channel.md)

[**WIA_IPA_BYTES_PER_LINE**](wia-ipa-bytes-per-line.md)

[**WIA_IPA_CHANNELS_PER_PIXEL**](wia-ipa-channels-per-pixel.md)

[**WIA_IPA_DEPTH**](wia-ipa-depth.md)

[**WIA_IPA_FORMAT**](wia-ipa-format.md)

[**WIA_IPA_NUMBER_OF_LINES**](wia-ipa-number-of-lines.md)

[**WIA_IPA_PIXELS_PER_LINE**](wia-ipa-pixels-per-line.md)

[**WIA_IPA_PLANAR**](wia-ipa-planar.md)

[**WIA_IPA_RAW_BITS_PER_CHANNEL**](wia-ipa-raw-bits-per-channel.md)

[**WIA_IPS_THRESHOLD**](wia-ips-threshold.md)
