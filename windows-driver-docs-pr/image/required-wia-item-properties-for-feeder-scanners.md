---
title: Required WIA Item Properties for Feeder Scanners
description: Required WIA Item Properties for Feeder Scanners
ms.assetid: f9868f05-3c1f-4042-9820-9c1c38af3432
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required WIA Item Properties for Feeder Scanners





The WIA feeder scanner item is required to support the following WIA properties:

[**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384)

[**WIA\_DPS\_PAGE\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551417)

[**WIA\_IPA\_ACCESS\_RIGHTS**](https://msdn.microsoft.com/library/windows/hardware/ff551518)

[**WIA\_IPA\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551526)

[**WIA\_IPA\_ITEM\_CATEGORY**](https://msdn.microsoft.com/library/windows/hardware/ff551581)

[**WIA\_IPA\_CHANNELS\_PER\_PIXEL**](https://msdn.microsoft.com/library/windows/hardware/ff551535)

[**WIA\_IPA\_COMPRESSION**](https://msdn.microsoft.com/library/windows/hardware/ff551540)

[**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543)

[**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546)

[**WIA\_IPA\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551553)

[**WIA\_IPA\_FULL\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551561)

[**WIA\_IPA\_ITEM\_NAME**](https://msdn.microsoft.com/library/windows/hardware/ff551590)

[**WIA\_IPA\_ITEM\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff551594)

[**WIA\_IPA\_PREFERRED\_FORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff551623)

[**WIA\_IPA\_TYMED**](https://msdn.microsoft.com/library/windows/hardware/ff551656)

[**WIA\_IPS\_BRIGHTNESS**](https://msdn.microsoft.com/library/windows/hardware/ff552567)

[**WIA\_IPS\_CONTRAST**](https://msdn.microsoft.com/library/windows/hardware/ff552573)

[**WIA\_IPS\_CUR\_INTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552579)

[**WIA\_IPS\_MAX\_HORIZONTAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552607)

[**WIA\_IPS\_MAX\_VERTICAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552611)

[**WIA\_IPS\_MIN\_HORIZONTAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552612)

[**WIA\_IPS\_MIN\_VERTICAL\_SIZE**](https://msdn.microsoft.com/library/windows/hardware/ff552614)

[**WIA\_IPS\_OPTICAL\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552620)

[**WIA\_IPS\_OPTICAL\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552622)

[**WIA\_IPS\_PAGES**](https://msdn.microsoft.com/library/windows/hardware/ff552630)

[**WIA\_IPS\_PAGE\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552632)

[**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636)

[**WIA\_IPS\_PHOTOMETRIC\_INTERP**](https://msdn.microsoft.com/library/windows/hardware/ff552640)

[**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661)

[**WIA\_IPS\_XPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552663)

[**WIA\_IPS\_XRES**](https://msdn.microsoft.com/library/windows/hardware/ff552665)

[**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669)

[**WIA\_IPS\_YPOS**](https://msdn.microsoft.com/library/windows/hardware/ff552671)

[**WIA\_IPS\_YRES**](https://msdn.microsoft.com/library/windows/hardware/ff552673)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655) property is required when the [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) property is set to 1 bit per pixel (BPP) or when the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property is set to WIA\_DATA\_THRESHOLD.

 

 

 




