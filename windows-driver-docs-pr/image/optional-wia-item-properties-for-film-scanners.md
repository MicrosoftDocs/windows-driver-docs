---
title: Optional WIA Item Properties for Film Scanners
description: Optional WIA Item Properties for Film Scanners
ms.assetid: 6c17deed-7840-4ec0-bc19-d695b3e80c38
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Optional WIA Item Properties for Film Scanners





The WIA film scanner item can optionally support the following WIA properties:

[**WIA\_IPA\_FILENAME\_EXTENSION**](https://msdn.microsoft.com/library/windows/hardware/ff551549)

[**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641)

[**WIA\_IPS\_AUTO\_DESKEW**](https://msdn.microsoft.com/library/windows/hardware/ff552564)

[**WIA\_IPS\_DESKEW\_X**](https://msdn.microsoft.com/library/windows/hardware/ff552581)

[**WIA\_IPS\_DESKEW\_Y**](https://msdn.microsoft.com/library/windows/hardware/ff552587)

[**WIA\_IPS\_LAMP**](https://msdn.microsoft.com/library/windows/hardware/ff552603)

[**WIA\_IPS\_LAMP\_AUTO\_OFF**](https://msdn.microsoft.com/library/windows/hardware/ff552605)

[**WIA\_IPS\_PREVIEW\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff552646)

[**WIA\_IPS\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552648)

[**WIA\_IPS\_SEGMENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552649)

[**WIA\_IPS\_SHOW\_PREVIEW\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff552652)

[**WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION**](https://msdn.microsoft.com/library/windows/hardware/ff552653)

[**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655)

[**WIA\_IPS\_WARM\_UP\_TIME**](https://msdn.microsoft.com/library/windows/hardware/ff552660)

[**WIA\_IPS\_XSCALING**](https://msdn.microsoft.com/library/windows/hardware/ff552667)

[**WIA\_IPS\_YSCALING**](https://msdn.microsoft.com/library/windows/hardware/ff552676)

**Note**   The [**WIA\_IPA\_RAW\_BITS\_PER\_CHANNEL**](https://msdn.microsoft.com/library/windows/hardware/ff551641) property is required if the WiaImgFmt\_RAW format is supported. The [**WIA\_IPA\_Format**](https://msdn.microsoft.com/library/windows/hardware/ff551553) property must support the WiaImgFmt\_BMP format. The [**WIA\_IPS\_THRESHOLD**](https://msdn.microsoft.com/library/windows/hardware/ff552655) property is required when the [**WIA\_IPA\_DEPTH**](https://msdn.microsoft.com/library/windows/hardware/ff551546) property is set to 1 BPP or when the [**WIA\_IPA\_DATATYPE**](https://msdn.microsoft.com/library/windows/hardware/ff551543) property is set to WIA\_DATA\_THRESHOLD.

 

 

 




