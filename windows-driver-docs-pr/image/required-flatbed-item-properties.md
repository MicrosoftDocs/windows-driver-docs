---
title: Required Flatbed Item Properties
description: Required Flatbed Item Properties
ms.assetid: 5af295de-b5ad-47c7-b1db-9d5685ed8d19
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required Flatbed Item Properties





The WIA flatbed scanner item is required to support the following WIA properties:

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-access-rights)

[**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-bits-per-channel)

[**WIA\_IPA\_BUFFER\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-buffer-size)

[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-channels-per-pixel)

[**WIA\_IPA\_COLOR\_PROFILE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-color-profile)

[**WIA\_IPA\_COMPRESSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-compression)

[**WIA\_IPA\_DATATYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-datatype)

[**WIA\_IPA\_DEPTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-depth)

[**WIA\_IPA\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-full-item-name)

[**WIA\_IPA\_ICM\_PROFILE\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-icm-profile-name)

[**WIA\_IPA\_ITEM\_CATEGORY**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-category)

[**WIA\_IPA\_ITEM\_NAME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-name)

[**WIA\_IPA\_ITEM\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-item-size)

[**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-max-horizontal-size)

[**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-max-vertical-size)

[**WIA\_IPS\_MIN\_HORIZONTAL\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-min-horizontal-size)

[**WIA\_IPS\_MIN\_VERTICAL\_SIZE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-min-vertical-size)

[**WIA\_IPA\_NUMBER\_OF\_LINES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-number-of-lines)

[**WIA\_IPA\_PIXELS\_PER\_LINE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-pixels-per-line)

[**WIA\_IPA\_PLANAR**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-planar)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-preferred-format)

[**WIA\_IPA\_PROP\_STREAM\_COMPAT\_ID**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-prop-stream-compat-id)

[**WIA\_IPA\_TYMED**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-tymed)

[**WIA\_IPS\_BRIGHTNESS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-brightness)

[**WIA\_IPS\_CONTRAST**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-contrast)

[**WIA\_IPS\_CUR\_INTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-cur-intent)

[**WIA\_IPS\_OPTICAL\_XRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-optical-xres)

[**WIA\_IPS\_OPTICAL\_YRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-optical-yres)

[**WIA\_IPS\_PREVIEW**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-preview)

[**WIA\_IPS\_XEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xextent)

[**WIA\_IPS\_XPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xpos)

[**WIA\_IPS\_XRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xres)

[**WIA\_IPS\_YEXTENT**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yextent)

[**WIA\_IPS\_YPOS**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-ypos)

[**WIA\_IPS\_YRES**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yres)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-raw-bits-per-channel) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-threshold) property is required when the [**WIA\_IPA\_DEPTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-depth) property is set to 1 bits per pixel (BPP) or when the [**WIA\_IPA\_DATATYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-datatype) property is set to WIA\_DATA\_THRESHOLD.

 

 

 




