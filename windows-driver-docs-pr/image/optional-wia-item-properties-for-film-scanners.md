---
title: Optional WIA Item Properties for Film Scanners
description: Optional WIA Item Properties for Film Scanners
ms.assetid: 6c17deed-7840-4ec0-bc19-d695b3e80c38
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optional WIA Item Properties for Film Scanners





The WIA film scanner item can optionally support the following WIA properties:

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-filename-extension)

[**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-raw-bits-per-channel)

[**WIA\_IPS\_AUTO\_DESKEW**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-auto-deskew)

[**WIA\_IPS\_DESKEW\_X**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-deskew-x)

[**WIA\_IPS\_DESKEW\_Y**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-deskew-y)

[**WIA\_IPS\_LAMP**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-lamp)

[**WIA\_IPS\_LAMP\_AUTO\_OFF**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-lamp-auto-off)

[**WIA\_IPS\_PREVIEW\_TYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-preview-type)

[**WIA\_IPS\_ROTATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-rotation)

[**WIA\_IPS\_SEGMENTATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-segmentation)

[**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-show-preview-control)

[**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-supports-child-item-creation)

[**WIA\_IPS\_THRESHOLD**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-threshold)

[**WIA\_IPS\_WARM\_UP\_TIME**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-warm-up-time)

[**WIA\_IPS\_XSCALING**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-xscaling)

[**WIA\_IPS\_YSCALING**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-yscaling)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-raw-bits-per-channel) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-format) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ips-threshold) property is required when the [**WIA\_IPA\_DEPTH**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-depth) property is set to 1 BPP or when the [**WIA\_IPA\_DATATYPE**](https://docs.microsoft.com/windows-hardware/drivers/image/wia-ipa-datatype) property is set to WIA\_DATA\_THRESHOLD.

 

 

 




